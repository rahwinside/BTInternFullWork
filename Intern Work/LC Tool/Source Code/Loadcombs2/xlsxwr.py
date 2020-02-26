import xlsxwriter, os
try:
    try:
        raw_data = open(
            os.path.expanduser("~").replace(repr('\n').strip("'").strip('n'), "/") + "/Documents/collector.txt", 'r')
    except:
        pass
    wkbook = 'data.xlsx'
    entity_name = raw_data.readline().split()
    entity_id = raw_data.readline().split()
    temp_list = []
    for i in range(0, len(entity_name)):
        temp_dict = dict(temp_list)
        temp_list.append((entity_name[i], entity_id[i]))

    wkbk = xlsxwriter.Workbook(wkbook)
    ldcase = wkbk.add_worksheet('LoadcaseSheet')
    ldstep = wkbk.add_worksheet('LoadstepSheet')

    i = 0
    for x in entity_name:
        if not (x.startswith('SPC')):
            ldcase.write(0, i + 2, str(x))
            ldcase.write(2, i + 2, int(temp_dict[x]))
            i += 1
    ldcase.write(2, 0, 'Loadcase name')
    ldcase.write(2, 1, 'Load IDs')
    i = 0
    for x in entity_name:
        if (x.startswith('SPC')):
            ldstep.write(0, i + 4, str(x))
            ldstep.write(2, i + 4, int(temp_dict[x]))
            i += 1
    ldstep.write(1, 0, 'Loadstep name')
    ldstep.write(1, 1, 'Loadstep type')
    ldstep.write(1, 2, 'Pretension')
    ldstep.write(1, 3, 'SPC ID')
    ldstep.write(0, 3, 'Loadcomb name')

    ldstep.data_validation('B3:B1048576', {'validate': 'list',
                                           'source': ['linear static', 'non-linear quasi-static']})
    ldstep.data_validation('C3:C1048576', {'validate': 'list',
                                           'source': ['Yes', 'No']})
    for j in range(0, 16370):
        ldstep.write(0, j + i + 4, '=IF(LoadcaseSheet!A' + str(j + 4) + '="", "", LoadcaseSheet!A' + str(j + 4) + ')')
    wkbk.close()
except:
    pass