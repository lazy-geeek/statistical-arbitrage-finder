import pandas as pd

def saveDFasExcel(df,fileName,sheetName):

    fileName = fileName + ".xlsx"
        
    writer = pd.ExcelWriter(fileName,engine='xlsxwriter') # type: ignore
    df.to_excel(writer, sheet_name=sheetName, index=False)

    workbook  = writer.book
    worksheet = writer.sheets[sheetName]

    # Add cell formats.
    #priceFormat = workbook.add_format({'num_format': '#,##0.00'}) # type: ignore
    #volumeFormat = workbook.add_format({'num_format': '#,##0'}) # type: ignore
    #percentFormat = workbook.add_format({'num_format': '0.0000'}) # type: ignore

    worksheet.autofilter('A1:AB1')
    worksheet.freeze_panes(1, 0)
        
    workbook.close()    