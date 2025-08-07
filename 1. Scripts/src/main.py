import pandas as pd
import scrapping_fleet_EU as scrap
import scrapping_fleet_ESP as scrap_esp

##------------------------------------------------------------------------------------------------------------------##
# Scraping de datos de buques de Europa y España
# Autor: Julio Úbeda Quesada y Lucas Zamora Vera
# Fecha: 2025-04-04

# El tiempo estimado para la ejecución es aproximadamente 8h:
# 4h para obtener el total de los datos de Europa y 4h para el scraping de los buques de España.
##------------------------------------------------------------------------------------------------------------------##

# 1. Obtener y guardar datos de los buques europeos
scrap.get_data_EU()

# 2. Cargar el dataset europeo
file_path = "./4. Solucion/data/datos_buques_EU.csv"
df = pd.read_csv(file_path, dtype=str)  # Leer como string para evitar problemas de formato

# 3. Filtrar solo los buques de España
df_esp = df[df["Flag"] == "ESP"].copy()

# 4. Obtener la lista de CFRs únicos
cfr_list = df_esp["CFR"].dropna().unique().tolist()

# 5. Ejecutar el scraping de España con los CFRs
scrap_esp.scrap_fleet_ESP(cfr_list)
