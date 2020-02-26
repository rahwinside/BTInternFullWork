source = open('tcl.tcl', 'r')
destination = open('cmd.tcl', 'w')
for line in source.readlines():
    print(str(line.rstrip('\n')))
    destination.write("file.write('" + line.rstrip('\n') + repr('\n').strip("'") + "')\n")