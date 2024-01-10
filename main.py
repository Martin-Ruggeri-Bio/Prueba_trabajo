from unzipper import unzip_file
from reader_xlsx import reader_xlsx
from formatter_csv import formatter_csv
from web_scraping import scraping
import pandas as pd

def main():
    dir_destination = "zipped_data/"
    dir_name_zip = "zipped_data"
    zip_file_name = "victims.zip"
    dir_name_xlsx = "unzipped_data"
    xlsx_file_name = "Victims_Age_by_Offense_Category_2022.xlsx"
    csv_file_name = "Victims_Age_by_Offense_Category_2022.csv"
    dir_name_csv = "csv_data"

    zip = scraping(dir_destination)
    if zip:
        unzip_file(dir_name_zip, zip_file_name, dir_name_xlsx)
        reader_xlsx(dir_name_xlsx, xlsx_file_name, csv_file_name, dir_name_csv)
        formatter_csv(dir_name_csv, csv_file_name, dir_name_csv)

    df = pd.read_csv(f"{dir_name_csv}/{csv_file_name}")
    print(df.head())

if __name__ == "__main__":
    main()