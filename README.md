# Tipología y ciclo de vida de los datos: 
# PR1: ¿Cómo podemos capturar los datos de la web?

## Descripción 

Este proyecto utiliza Selenium, Requests y BeautifulSoup para automatizar la extracción de datos desde el sitio web de Fleet Europa de la Unión Europea y el registro nacional de la flota pesquera española. El script automatiza la búsqueda de todos los barcos registrados, navega a través de las páginas de resultados y guarda los datos en un archivo CSV.

## Estructura del Proyecto

WEB SCRAPPING CFRs EU/  
│  
|── 0. Teoria/                            
│   ├── M2.851_GuiaAprendizaje_Bloque2.pdf  
│   ├── Richard Lawson - Web Scraping with Python.pdf  
│   └── WebScrapping.pdf  
│  
|── 1. Scripts  
│   └── src/                                                   
|        └── main.py                                           
|   	└── scrapping_fleet_ESP.py               
│        └──scrapping_fleet_EU.py                  
│   └── notebook/                                          
	└── scrapping_CFRs_EU-ESP.ipynb   
│  
|── 3. Enunciado PR 1/                                
│   └── M2.851_20242_Practica1.pdf  
│  
|── 4. Solucion/                                             
│   ├── data/                                                  
│       └── resultados_fleet.csv  
│   └── memoria/                                           
│       └── PR1_Ubeda_Quesada_Julio-Zamora_Vera_Lucas.pdf  
│  
|── 5. Literatura/                                             
│   └── Dialnet-ExpansionYModernizacionDeLaFlotaPesquera.pdf  
│  
|── 6. Figura y graficos/                                
│   └── openart-image_IBbRrax9_174290720241...  
│  
|── LICENSE.txt                                            
|── README.md                                          
|── requirements.txt                                      
  

## Uso

Para capturar los datos desde la web de [Fleet Europa de la Unión Europea]("https://webgate.ec.europa.eu/fleet-europa/search_en") sigue estos pasos:

### 1.  Abre la terminal en VSCode:

Haz clic en el menú "Terminal" y selecciona "Nueva terminal".

Asegúrate de que estás en el directorio del proyecto donde se encuentran los subdirectorios listados arriba.

Puedes ejecutar: 
```bash
cd ../WebScrapping con Selenium y BeautifulSoup - Registro General de la Flota Pesquera
```
### 2. Instala las dependencias:

Asegúrate de haber instalado las dependencias listadas en `requirements.txt` antes de ejecutar el archivo principal:

```bash
pip install -r requirements.txt
```
### 3. Ejecuta el archivo principal:

#### 3.1. Ejecuta el script de la siguiente manera:

- Si lo ejecutas desde Windows simplemente ejecuta el siguiente comando en la terminal: 

```bash
python main.py
```

- Si usas macos y quieres evitar mensajes de warnings ejecuta: 

```bash
QT_LOGGING_RULES="*.debug=false" main.py
```

#### 3.2. El script realizará lo siguiente:

- Accederá a la página de Fleet Europa.
- Seleccionará la opción "EU" y "All Vessels".
- Iniciará la búsqueda de barcos registrados.
- Ajustará el número de resultados por página a 100.
- Recorrerá todas las páginas de resultados.
- Extraerá los datos y los guardará en ./data/resultados_scrapping_fleet.csv.
- Generará una lista con los CFRs de los buques españoles.
- Accede a la página del registro español.
- Por cada CFR de la lista realiza una petición a la web y almacena los datos en un DataFrame.
- Guarda el DataFrame generado en ./4. Solucion/data/datos_buques_ESP.csv

#### 3.3. Scrapping solo de buques españoles

- Si deseas scrapear datos técnicos de buques españoles únicamente, se puede utilizar el fichero 

```bash
python main.py
```


## Licencia

Este proyecto está bajo la Licencia ‘Creative Commons Attribution 4.0 International’. Esta licencia permite que el dataset sea usado, compartido, adaptado y redistribuido, siempre que se cumplan tres condiciones fundamentales:
- Atribución (BY): Se debe reconocer adecuadamente la autoría del trabajo, mencionando tanto al autor del scraping como a las fuentes oficiales (Ministerio de Agricultura, Pesca y Alimentación de España y la Comisión Europea).
- No Comercial (NC): Restringe el uso del dataset a fines no comerciales, protegiendo así su uso en contextos educativos, investigativos o de divulgación sin que se explote con fines lucrativos.
- Compartir Igual (SA): Si se generan obras derivadas o se modifica el dataset, estas deben compartirse bajo la misma licencia, garantizando que el conocimiento permanezca abierto y libre para futuras reutilizaciones.
 
Consulta el archivo [`LICENSE`](./LICENSE.txt) o [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) para más detalles.

