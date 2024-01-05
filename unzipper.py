# Importar la librería zipfile
import zipfile

# Definir la función para descomprimir un archivo zip
def unzip_file(dir_name, zip_file_name, dir_destination):
    # Crear un objeto ZipFile con el archivo zip
    with zipfile.ZipFile(f"{dir_name}/{zip_file_name}", 'r') as zip_obj:
        # Extraer todos los archivos en la carpeta destino
        zip_obj.extractall(dir_destination)


if __name__ == "__main__":
    dir_name_zip = "zipped_data"
    zip_file_name = "victims.zip"
    dir_name_xlsx = "unzipped_data"
    unzip_file(dir_name_zip, zip_file_name, dir_name_xlsx)
    