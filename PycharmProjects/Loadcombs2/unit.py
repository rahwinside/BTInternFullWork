import xlrd

wkbk = xlrd.open_workbook('test.xlsx')
sheet = wkbk.sheet_by_index(1)
print(str(sheet.cell_value(0, 10)))
nLoadcombs = 0
i = 4
print(sheet.ncols)
while(i<16377):
    if not(sheet.cell_value(0, i) in [0, '']):
        print(sheet.cell_value(0, i))
        i += 1
        nLoadcombs+=1
    else:
        break
print(nLoadcombs)
print(sheet.ncols)