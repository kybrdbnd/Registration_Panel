from tkinter import messagebox
from xlsxwriter.workbook import Workbook
import sqlite3


class MakeDatabase():
    def __init__(self):
        self.makedb()
        return

    def makedb(self):
        conn = sqlite3.connect("registration.db")
        c = conn.cursor()
        table = "new_entries"
        try:
            query = "select * from %s" % table
            c.execute(query)
            workbook = Workbook("output.xlsx")
            sheet = workbook.add_worksheet()
            bold = workbook.add_format({'bold': True})
            sheet.set_column('A:A', 5)
            sheet.set_column('B:B', 18)
            sheet.set_column('C:C', 8)
            sheet.set_column('D:D', 8)
            sheet.set_column('E:E', 13)
            sheet.set_column('F:F', 17)
            sheet.set_column('G:G', 5)
            sheet.write("A1", 'S.No', bold)
            sheet.write("B1", 'Name', bold)
            sheet.write("C1", 'Branch', bold)
            sheet.write("D1", 'Section', bold)
            sheet.write("E1", 'Phone no', bold)
            sheet.write("F1", 'Email', bold)
            sheet.write("G1", 'Size', bold)
            for r, row in enumerate(c.fetchall()):
                for c, col in enumerate(row):
                    sheet.write(r + 1, c, col)
            workbook.close()
            conn.close()
            messagebox.showinfo(title="Registration", message="Successfully made excel file")
        except:
            messagebox.showerror(title="Registration", message="Database doesn't exist")

        return


myapp = MakeDatabase()
