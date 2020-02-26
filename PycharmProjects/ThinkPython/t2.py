import xlrd

excel_input = xlrd.open_workbook('Book 3.xlsx')
nLCase = int(input("LCase count"))
nSPC = input("SPC count")
loadstep_sheet = excel_input.sheet_by_index(0)

nLoadsteps = loadstep_sheet.nrows-2
nLoadcombs = loadstep_sheet.ncols-4

loadstep_matrix = [[loadstep_sheet.cell_value(i+2, j+4) for j in range(nLoadcombs)] for i in range(nLoadsteps)]

pretension = []
try:
    for i in range(0, nLoadsteps):
        if(loadstep_sheet.cell_value(i+2, 2)=='Yes'):
            pretension.append(1)
        elif(loadstep_sheet.cell_value(i+2, 2)=='No'):
            pretension.append(0)
        else:
            raise Exception
except Exception as e:
    print("Invalid Pretension Value!")
    exit(1)

tcl_file_name = 'out.tcl'
new_tcl = open(tcl_file_name, 'w')

print(pretension)
if(1 in pretension):
    pretspcid = input("Enter SPC ID for Pret")
    pretloadid = input("Enter Pret ID for Pret")
    new_tcl.write('*startnotehistorystate {LoadSteps Creation}\n')
    new_tcl.write('*createmark loadcols 1\n')
    new_tcl.write('*createmark outputblocks 1\n')
    new_tcl.write('*createmark groups 1\n')
    new_tcl.write('*loadstepscreate "Pretension" 1\n')
    new_tcl.write('*attributeupdateint loadsteps 1 4143 1 1 0 1\n')
    new_tcl.write('*attributeupdateint loadsteps 1 4709 1 1 0 1\n')
    new_tcl.write('*attributeupdateentity loadsteps 1 4145 1 1 0 loadcols '+pretspcid+'\n')
    new_tcl.write('*attributeupdateint loadsteps 1 3800 1 1 0 0\n')
    new_tcl.write('*attributeupdateint loadsteps 1 707 1 1 0 0\n')
    new_tcl.write('*attributeupdateint loadsteps 1 2396 1 1 0 0\n')
    new_tcl.write('*attributeupdateint loadsteps 1 8134 1 1 0 0\n')
    new_tcl.write('*attributeupdateentity loadsteps 1 2159 1 1 0 loadcols '+pretloadid+'\n')
    new_tcl.write('*attributeupdateint loadsteps 1 2160 1 1 0 0\n')
    new_tcl.write('*attributeupdateint loadsteps 1 10212 1 1 0 0\n')
    new_tcl.write('*endnotehistorystate {LoadSteps Creation}\n')
    new_tcl.write('#Pretension Created!\n')

for i in range(0, len(loadstep_matrix)):
    new_tcl.write('*startnotehistorystate {LoadSteps Creation}\n')
    if (loadstep_matrix[i].count(1) == 2):
        print(2)
        line = '*createmark loadcols 1 "' + str(loadstep_sheet.cell_value(0, loadstep_matrix[i].index(1) + 4)) + '" "'
        line += str(loadstep_sheet.cell_value(0, len(loadstep_matrix[i]) - loadstep_matrix[i][::-1].index(
            1) - 1 + 4)) + '"' + '\n'
    else:
        line = '*createmark loadcols 1 "' + str(
            loadstep_sheet.cell_value(0, loadstep_matrix[i].index(1) + 4)) + '"' + '\n'
    new_tcl.write(line)
    new_tcl.write('*createmark outputblocks 1\n')
    new_tcl.write('*createmark groups 1\n')
    new_tcl.write('*loadstepscreate "' + str(loadstep_sheet.cell_value(i + 2, 0)) + '" 1' + '\n')

    #check for linear static
    if(loadstep_sheet.cell_value(i+2, 1)=='linear static'):
        new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 4143 1 1 0 1' + '\n')
        new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 4709 1 1 0 1' + '\n')

        #run if only SPC or Load available
        if(loadstep_matrix[i].count(1) == 1):
            #run if only Load is available
            if(loadstep_matrix[i].index(1) in range(0, nLCase)):
                line = '*attributeupdateentity loadsteps ' + str(i + 2) + ' 4147 1 1 0 loadcols ' + str(
                    int(loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 4))) + '\n'
                new_tcl.write(line)
            #run if only SPC is available
            else:
                line = '*attributeupdateentity loadsteps ' + str(i + 2) + ' 4145 1 1 0 loadcols ' + str(
                    int(loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 4))) + '\n'
                new_tcl.write(line)

        #run if SPC&Load is available
        try:
            if(loadstep_matrix[i].count(1)==2):
                try:
                    if (loadstep_matrix[i].index(1) in range(0, nLCase)):
                        line = '*attributeupdateentity loadsteps ' + str(i + 2) + ' 4147 1 1 0 loadcols ' + str(
                            int(loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 4))) + '\n'
                        new_tcl.write(line)
                    else:
                        raise Exception
                    if (len(loadstep_matrix[i]) - loadstep_matrix[i][::-1].index(1) - 1 in range(nLCase, nLoadcombs)):
                        line = '*attributeupdateentity loadsteps ' + str(i+2) + ' 4145 1 1 0 loadcols ' + str(
                            int(loadstep_sheet.cell_value(1, len(loadstep_matrix[i]) - loadstep_matrix[i][::-1].index(1) - 1+4))) + '\n'
                        new_tcl.write(line)
                    else:
                        raise Exception
                except Exception as e:
                    print("Error in Excel sheet, check whether SPC and Loadcases are selected properly for step "+str(i + 2)+"! \n Loadstep TCl !Gen")
                    exit(1)
            elif(loadstep_matrix[i].count(1)>2):
                raise Exception
        except Exception as e:
            print("error: Load+SPC count >2! in step "+str(i + 2)+"\n Loadstep TCl !Gen")
            exit(1)

        #check pretension==yes
        if(pretension[i]==0):
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 3800 1 1 0 1' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 707 1 1 0 1' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 2396 1 1 0 1' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 8134 1 1 0 1' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 2160 1 1 0 1' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 10212 1 1 0 1' + '\n')
        else:
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 3800 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 707 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 2396 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 8134 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 2160 1 1 0 0' + '\n')
            new_tcl.write('*createarray '+str(i+2)+' 1\n')
            new_tcl.write('*attributeupdateentityidarray loadsteps '+str(i+2)+' 2161 1 1 0 loadsteps 1 1\n')
            new_tcl.write('*attributeupdateint loadsteps '+str(i+2)+' 10212 1 1 0 0\n')

    elif(loadstep_sheet.cell_value(i+2, 1)=='non-linear quasi-static'):
        new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 4143 1 1 0 1' + '\n')
        new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 4709 1 1 0 9' + '\n')

        #run if only SPC or Load available
        if (loadstep_matrix[i].count(1) == 1):
            #run if only load is available
            if (loadstep_matrix[i].index(1) in range(0, nLCase)):
                line = '*attributeupdateentity loadsteps ' + str(i + 2) + ' 4147 1 1 0 loadcols ' + str(
                    int(loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 4))) + '\n'
                new_tcl.write(line)
            #run if only SPC is available
            else:
                line = '*attributeupdateentity loadsteps ' + str(i + 2) + ' 4145 1 1 0 loadcols ' + str(
                    int(loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 4))) + '\n'
                new_tcl.write(line)
        try:
            if (loadstep_matrix[i].count(1) == 2):
                try:
                    if (loadstep_matrix[i].index(1) in range(0, nLCase)):
                        line = '*attributeupdateentity loadsteps ' + str(i + 2) + ' 4147 1 1 0 loadcols ' + str(
                            int(loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 4))) + '\n'
                        new_tcl.write(line)
                    else:
                        raise Exception
                    if (len(loadstep_matrix[i]) - loadstep_matrix[i][::-1].index(1) - 1 in range(nLCase, nLoadcombs)):
                        line = '*attributeupdateentity loadsteps ' + str(i + 2) + ' 4145 1 1 0 loadcols ' + str(
                            int(loadstep_sheet.cell_value(1, len(loadstep_matrix[i]) - loadstep_matrix[i][::-1].index(
                                1) - 1 + 4))) + '\n'
                        new_tcl.write(line)
                    else:
                        raise Exception
                except Exception as e:
                    print("Error in Excel sheet, check whether SPC and Loadcases are selected properly for step " + str(
                        i + 1) + "! \n Loadstep TCl !Gen")
                    exit(1)
            elif (loadstep_matrix[i].count(1) > 2):
                print("here")
                raise Exception
        except Exception as e:
            print("error: Load+SPC count >2! in step " + str(i + 2) + "\n Loadstep TCl !Gen")
            exit(1)
        if(pretension[i]==0):
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 3800 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 707 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 2396 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 8134 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 2160 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 10212 1 1 0 0' + '\n')
        else:
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 3800 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 707 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 2396 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 8134 1 1 0 0' + '\n')
            new_tcl.write('*attributeupdateint loadsteps ' + str(i + 2) + ' 2160 1 1 0 1' + '\n')
            new_tcl.write('*createarray '+str(i+2)+' 1\n')
            new_tcl.write('*attributeupdateentityidarray loadsteps '+str(i+2)+' 2161 1 1 0 loadsteps 1 1\n')
            new_tcl.write('*attributeupdateint loadsteps '+str(i+2)+' 10212 1 1 0 0\n')
    else:
        print("Check Loadstep Type!!")
    new_tcl.write('*endnotehistorystate {LoadSteps Creation}\n')
    new_tcl.write("#end of iter " + str(i + 1) + '\n')
new_tcl.close()
print('LOADSTEP TCL FILE IS GENERATED')