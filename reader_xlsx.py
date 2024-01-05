# Importar la librería pandas
import pandas as pd

def reader_xlsx(dir_name, xlsx_file_name, csv_file_name, dir_destination):
    # Cargar el archivo xlsx en un DataFrame
    df = pd.read_excel(f"{dir_name}/{xlsx_file_name}", skipfooter=1)  # Para omitir el footer
    # Eliminar la columna de índice si no es necesaria
    df.to_csv(f"{dir_destination}/{csv_file_name}", index=False)  # Guardar sin índice

if __name__ == "__main__":
    dir_name = "unzipped_data"
    xlsx_file_name = "Victims_Age_by_Offense_Category_2022.xlsx"
    csv_file_name = "Victims_Age_by_Offense_Category_2022.csv"
    dir_destination = "csv_data"
    reader_xlsx(dir_name, xlsx_file_name, csv_file_name, dir_destination)
    df = pd.read_csv(f"{dir_destination}/{csv_file_name}")
    print(df.head())