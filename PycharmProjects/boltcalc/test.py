import xlrd
from tinydb import TinyDB

wkbk = xlrd.open_workbook('boltdb.xlsx')
db = TinyDB('boltdata.json')

for i in range(0, wkbk.nsheets):
    sheet = wkbk.sheet_by_index(i)
    table = db.table(sheet.name)
    for x in range(1, sheet.nrows):
        l = []
        for y in range(0, sheet.ncols):
            l.append(sheet.cell_value(x, y))
        table.insert({'size': l[0], 'dia':l[1], 'pitch':l[2], 'dw':l[3], 'k':l[4]})