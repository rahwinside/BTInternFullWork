import xlrd

try:
    loadcasesheet = xlrd.open_workbook("Book 2.xlsx")
    sheet = loadcasesheet.sheet_by_index(0)
    nlcount = sheet.ncols-2 #no of load counter
    nlcase = sheet.nrows-3 #no of load cases

    new_tcl = open("new.tcl", 'w')

    #code to write lst set in tcl sh
    LCount = []
    for i in range (3, nlcase+3):
        x = []
        for j in range(2, nlcount+2):
            x.append(sheet.cell_value(i, j))
        LCount.append(x)

    #transpose LCount
    tLCount = [[LCount[j][i] for j in range(len(LCount))] for i in range(len(LCount[0]))]

    #iter to write lst data to tcl file
    ctr=0
    for x in tLCount:
        ctr = ctr + 1
        lstdata = str(x)[1:-1]
        new_tcl.write("set lst"+str(ctr)+' [split "'+lstdata+'" ","]\n')

    #iter to get loadcase names
    lcase_name = []
    for i in range(3, nlcase+3):
        lcase_name.append(sheet.cell_value(i, 0))

    #iter to find maxID value and construct IDList array
    IDList = []
    highestIDVal = int(sheet.cell_value(2,2))
    for i in range(0, nlcount):
        t = int(sheet.cell_value(2,i+2))
        IDList.append(t)
        if(highestIDVal<t):
            highestIDVal = t

    #iter to write tcl script for each case
    for i in range(0, nlcase):
        new_tcl.write("set name "+lcase_name[i]+"\n")
        new_tcl.write("set j [expr "+str(i+1)+"+"+str(highestIDVal)+"]\n") #tcl: j is the ID of the loadcase being created (not nlcount+2)
        k = nlcount-LCount[i].count(0)  #tcl: k is no. of non-zero scaling factors in a loadcase (non-zero cells in a excel row)
        new_tcl.write("set k "+str(k)+"\n")
        new_tcl.write('*startnotehistorystate {Created loadcollector $name}\n')
        new_tcl.write('*collectorcreate loadcols $name "" 11\n')
        new_tcl.write('*createmark loadcols 2 $name\n')
        new_tcl.write(
            '*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"\n')
        new_tcl.write('*startnotehistorystate {Attached attributes to loadcol $name}\n')
        new_tcl.write('*attributeupdateint loadcols $j 3240 1 2 0 1\n')
        new_tcl.write('*attributeupdatedouble loadcols $j 379 1 2 0 1\n')
        new_tcl.write('*attributeupdateint loadcols $j 3236 1 0 0 1\n')
        new_tcl.write('*createdoublearray 1 0\n')
        new_tcl.write('*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1\n')
        new_tcl.write('*createarray 1 0\n')
        new_tcl.write('*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1\n')
        new_tcl.write('*endnotehistorystate {Attached attributes to loadcol $name}\n')
        new_tcl.write('*startnotehistorystate {Attached attributes to loadcol $name}\n')
        new_tcl.write('*attributeupdateint loadcols $j 3236 1 0 0 $k\n')

        #iter to get all non-zero scaling factor indices
        nonzerolistindices = [x for x in range(len(LCount[i])) if LCount[i][x] != 0]
        for x in range(0, len(nonzerolistindices)):
            nonzerolistindices[x] += 1
        loadNumStr = ""
        for j in range(1, k+1):
            new_tcl.write("set load"+str(j)+" [lindex $lst"+str(nonzerolistindices[j-1])+" [expr " + str(i+1) + "-1]]\n")
            loadNumStr += "$load" + str(j) + " "

        #iter to form IDList (non-zero ones)
        RefIDList = []
        for t in nonzerolistindices:
            RefIDList.append(int(sheet.cell_value(2, t+1)))

        new_tcl.write('*createdoublearray $k ' + loadNumStr[:-1] + '\n')
        new_tcl.write('*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k\n')
        new_tcl.write("*createarray $k " + str(RefIDList)[1:-1].replace(",", "") + "\n")
        new_tcl.write('*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k\n')
        new_tcl.write('*endnotehistorystate {Attached attributes to loadcol $name}\n')
        new_tcl.write('*endnotehistorystate {Created loadcollector $name}\n')
        new_tcl.write('#iteration ' + str(i+1) + ' ends\n')

    print("New TCL file generated!")
    new_tcl.close()

except Exception as e:
    print("Error generating TCL file!!")
    print(e)
