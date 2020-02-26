import os

print(os.path.expanduser("~").replace(repr('\n').strip("'").strip('n'), "/")+"/Documents/collector.data", 'r')