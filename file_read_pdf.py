import os
import tabula
import pandas as pd

pdf_path = "D:/Desktop/hijg_http/pdf"
xls_path = "D:/Desktop/hijg_http/excel"

for file in os.listdir(pdf_path):
    if file.endswith(".pdf"):
        file_path_from = os.path.join(pdf_path, file)
        file_path_to = os.path.join(xls_path, file.replace('pdf', 'xlsx'))
        pg_data = tabula.read_pdf(file_path_from, stream=True)
        pd_final = pd.concat(pg_data)
        pd_final.to_excel(file_path_to, index=False)
