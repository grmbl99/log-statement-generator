#!/usr/bin/env python3
import sys
import json

if len(sys.argv) < 3:
  print("Usage: %s <input_file> <output_file>" % sys.argv[0])
  exit(1)

with open(sys.argv[1], 'r') as ifile:
  with open(sys.argv[2], 'w') as ofile:
    loggingDSL = json.load(ifile)

    ofile.write('#include <iostream>\n')
    ofile.write('using namespace std;\n\n')

    for logStatement in loggingDSL['log_statements']:
      ofile.write('void %s (' % (logStatement['readable_id']))

      # write function arguments
      for idx, arg in enumerate(logStatement['arguments']):
        if idx != 0:
          ofile.write(', ')
        ofile.write('%s %s' % (arg['type'], arg['name']))

      ofile.write(') {\n')

      # write function body
      ofile.write('\tcout << "%s" << endl\n' % (logStatement['description']))
      for idx, arg in enumerate(logStatement['arguments']):
        if idx != 0:
          ofile.write('\n')
        ofile.write('\t\t<< "\t%s: " << %s << endl' % (arg['name'], arg['name']))

      ofile.write(';\n}\n\n')
