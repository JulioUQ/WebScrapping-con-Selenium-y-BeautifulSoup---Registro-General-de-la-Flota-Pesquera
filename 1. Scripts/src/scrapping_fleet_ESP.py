import requests
from bs4 import BeautifulSoup
import pandas as pd

##------------------------------------------------------------------------------------------------------------------##
# Scraping de datos de buques de España desde el censo de buques del Ministerio de Agricultura, Pesca y Alimentación
# Este script permite buscar buques por su CFR (Código de Flota de Registro) y extraer información relevante.
# El script utiliza la librería requests para realizar solicitudes HTTP y BeautifulSoup para analizar el HTML.

# Autor: Julio Úbeda Quesada y Lucas Zamora Vera
# Fecha: 2023-10-23

def scrap_fleet_ESP(cfr_list):
    """
    Realiza el scraping del censo de buques españoles a partir de una lista de CFRs.
    Guarda los datos en './data/datos_buques_ESP.csv'
    """
    base_url = "https://servicio.pesca.mapama.es/censo/ConsultaBuqueRegistro/Buques/Search"
    session = requests.Session()
    
    data = []
    cfrs_sin_buque = []
    total_cfrs = len(cfr_list)

    for index, cfr in enumerate(cfr_list, start=1):
        print(f"Procesando {index}/{total_cfrs}: CFR {cfr}")
        params = {"text": cfr}
        response = session.get(base_url, params=params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            buque_link = soup.find("a", class_="apply--emphasize")

            if buque_link:
                buque_url = "https://servicio.pesca.mapama.es" + buque_link["href"]
                buque_response = session.get(buque_url)

                if buque_response.status_code == 200:
                    buque_soup = BeautifulSoup(buque_response.text, "html.parser")
                    nombre_buque = buque_soup.find("h2", class_="title--vessel-details").text.split("Nombre: ")[-1]
                    datos_buque = {"CFR": cfr, "Nombre": nombre_buque}

                    for div in buque_soup.find_all("div"):
                        label = div.find("dt", class_="info-field--label")
                        value = div.find("dd", class_="info-field--value")
                        if label and value:
                            datos_buque[label.text.strip()] = value.text.strip()

                    data.append(datos_buque)
                    print(f"✔️ Datos extraídos para {cfr} ({nombre_buque})")
                else:
                    print(f"❌ Error {buque_response.status_code}: No se pudo acceder a la página del buque {cfr}")
                    cfrs_sin_buque.append(cfr)
            else:
                print(f"⚠️ No se encontró un buque asociado para CFR {cfr}")
                cfrs_sin_buque.append(cfr)
        else:
            print(f"❌ Error {response.status_code}: No se pudo acceder a la página de búsqueda para CFR {cfr}")
            cfrs_sin_buque.append(cfr)

    # Crear DataFrame con los datos obtenidos
    df = pd.DataFrame(data)
    print("\nExtracción finalizada.")
    print(df)

    if cfrs_sin_buque:
        print("\nCFRs sin buque asociado:")
        print(cfrs_sin_buque)

    # Guardar los datos en un archivo CSV
    output_file = "./data/datos_buques_ESP.csv"
    df.to_csv(output_file, encoding="utf-8", index=False)
    print(f"\nDatos guardados en {output_file}")

# Permite ejecutar el script directamente si se desea
if __name__ == "__main__":
    # Esto solo se ejecuta si ejecutas este archivo directamente (no desde main.py)
    import pandas as pd
    df = pd.read_csv("./4. Solucion/data/datos_buques_EU.csv", dtype=str)
    cfr_list = df[df["Flag"] == "ESP"]["CFR"].dropna().unique().tolist()
    scrap_fleet_ESP(cfr_list)
