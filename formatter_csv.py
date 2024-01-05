import pandas as pd

def formatter_csv(dir_name, file_name, dir_destination):
    # Leer el archivo CSV como un DataFrame
    df = pd.read_csv(f"{dir_name}/{file_name}", skiprows=[1])
    # eliminar columna 1 de totales
    df = df.drop(df.columns[1], axis=1)
    # eliminar filas de totales y valores nulos y node deseados
    df = df.iloc[2:]
    # eliminar la fila 1
    df = df.drop(df.index[1])
    # Asignar el valor "Age of victims" a la fila NaN
    df.iloc[0, 0] = "Age of victims"
    # Configurar la primera fila como encabezado de columnas
    df.columns = df.iloc[0]
    # Eliminar la fila que es el encabezado
    df = df.iloc[1:]
    df.to_csv(f"{dir_destination}/{file_name}", index=False)  # Guardar sin índice


if __name__ == "__main__":
    dir_name = "csv_data"
    file_name = "Victims_Age_by_Offense_Category_2022.csv"
    dir_destination = "csv_data"
    formatter_csv(dir_name, file_name, dir_destination)
    df = pd.read_csv(f"{dir_name}/{file_name}")
    print(df.head())