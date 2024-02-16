import re
import os
from pdfminer.high_level import extract_pages, extract_text
import tabula



current_directory = os.getcwd() # Get the current working directory

pdf_file = os.path.join(current_directory, "test_files/Citycon_Financial Review_2022_1.pdf")
csv_file = "test.csv"
excel_file = "test.xlsx"

# TODO: Very Slow??
# Only take usable table data? No Pure text things?
# Check if theres a space/numbers after text?? only then add it? Can be spaces IF there will be numbers eventually
# FutureWarning: errors='ignore' is deprecated and will raise in a future version. Use to_numeric without passing `errors` and catch exceptions explicitly instead df[c] = pd.to_numeric(df[c], errors="ignore")
tables = tabula.read_pdf(pdf_file, pages="all")
df = tables[4] # 3 text + table, 4 Shows false data on second table??
clean_df = df.dropna(axis=1, how='all')# Remove empty columns
print(clean_df)
#df.to_csv(csv_file, sep=',', index=False, encoding='utf-8') # Saves to a CSV file.
clean_df.to_excel(excel_file) #openpyxl

# TODO: Loop for every table, then clean it
#for table in tables:
#    print(table)


def test():
    for page_layout in extract_pages(pdf_file):
        for element in page_layout:
            print(element)




def main():
    print("Main")
    print(pdf_file)
    #print(os.path.exists(pdf_file))
    #test()


if __name__ == '__main__':
    main()