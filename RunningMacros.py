import os.path
import win32com.client

def callmacro(macroname):

    if os.path.exists("Data Analytics.xlsm"):
        xl=win32com.client.Dispatch("Excel.Application")
        wb=xl.Workbooks.Open(os.path.abspath("Data Analytics.xlsm"))
        xl.Application.Run("'Data Analytics.xlsm'!DataCleaning.{}".format(macroname))
        wb.Close(SaveChanges=1)
        xl.Application.Quit()
        del xl

