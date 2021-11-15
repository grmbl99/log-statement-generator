#!/usr/bin/env python3
import sys
import json
import pathlib
from typing import Match

def writeFunctionHeader(file,logStatement):
  file.write('void %s (string context, ' % (logStatement['readable_id']))

  for idx, arg in enumerate(logStatement['arguments']):
    if idx != 0:
      file.write(', ')
    file.write('%s %s' % (arg['type'], arg['name']))

  file.write(')')

def writeFunctionBody_cout(file,logStatement):
  file.write('\tcout\n\t\t<< msTimeStamp() << endl\n')
  file.write('\t\t<< "context: " << context << endl\n')
  file.write('\t\t<< "%s" << endl\n' % (logStatement['description']))

  for idx, arg in enumerate(logStatement['arguments']):
    if idx != 0:
      file.write('\n')
    file.write('\t\t<< "\t%s: " << %s << endl' % (arg['name'], arg['name']))

  file.write(';\n')

mypath=(pathlib.Path(__file__).parent.resolve())

if len(sys.argv) < 4:
  print("Usage: %s <input_json_file> <output_src_file> <output_h_file>" % sys.argv[0])
  exit(1)

with open(sys.argv[1], 'r') as json_file, \
     open(sys.argv[2], 'w') as src_file, \
     open(sys.argv[3], 'w') as h_file, \
     open(mypath/'boilerplate-cpp.txt', 'r') as src_boilerplate, \
     open(mypath/'boilerplate-h.txt', 'r') as h_boilerplate:
  loggingDSL = json.load(json_file)

  src_file.write(src_boilerplate.read())
  h_file.write(h_boilerplate.read())

  for logStatement in loggingDSL['log_statements']:
    writeFunctionHeader(h_file,logStatement)
    h_file.write(';\n')

    writeFunctionHeader(src_file,logStatement)
    src_file.write(' {\n')

    for output in logStatement['output']:
      if output == 'cout':
        writeFunctionBody_cout(src_file,logStatement)
      else:
        print('Unsupported output type: %s' % output)

    src_file.write('}\n\n')

  h_file.write('\n#endif\n')
