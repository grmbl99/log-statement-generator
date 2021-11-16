#!/usr/bin/env python3
import sys
import json
import pathlib

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
     open(sys.argv[2], 'w') as cpp_file, \
     open(sys.argv[3], 'w') as h_file, \
     open(mypath/'boilerplate-cpp.txt', 'r') as cpp_boilerplate, \
     open(mypath/'boilerplate-h.txt', 'r') as h_boilerplate:
  loggingDSL = json.load(json_file)

  cpp_file.write(cpp_boilerplate.read())
  h_file.write(h_boilerplate.read())

  for logStatement in loggingDSL['log_statements']:
    writeFunctionHeader(h_file,logStatement)
    h_file.write(';\n')

    writeFunctionHeader(cpp_file,logStatement)
    cpp_file.write(' {\n')

    for output in logStatement['output']:
      if output == 'cout':
        writeFunctionBody_cout(cpp_file,logStatement)
      else:
        print('Unsupported output type: %s' % output)

    cpp_file.write('}\n\n')

  h_file.write('\n#endif\n')
