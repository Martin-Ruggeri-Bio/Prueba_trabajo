# Prueba_trabajo
Este script de Python se encarga de procesar datos sobre víctimas de delitos. Realiza tres operaciones principales: descomprimir un archivo ZIP, leer un archivo XLSX y formatear un archivo CSV. La aplicación utiliza las funciones proporcionadas por los módulos unzipper, reader_xlsx, y formatter_csv.

# Instalación
## Clonar el repositorio:

`$ git clone https://github.com/tu_usuario/tu_repo.git`
`$ cd Prueba_trabajo`

## Configurar un entorno virtual:
`$ python -m venv venv`
`$ source venv/bin/activate`

## Instalar los requisitos:
`$ pip install -r requirements.txt`

## Uso
Ejecutar el script principal:
`$ python main.py`
Este comando ejecutará el script principal que realiza las siguientes operaciones:

    Descomprime el archivo ZIP en la carpeta unzipped_data.
    Lee el archivo XLSX y guarda un archivo CSV en la carpeta csv_data.
    Formatea el archivo CSV resultante.
    Verificar los resultados:
    Después de ejecutar el script, puedes verificar los resultados imprimiendo las primeras filas del DataFrame resultante.


## Estructura del Proyecto
main.py: Script principal que orquesta las operaciones.
unzipper.py: Módulo para descomprimir archivos ZIP.
reader_xlsx.py: Módulo para leer archivos XLSX y convertirlos a CSV.
formatter_csv.py: Módulo para formatear archivos CSV.