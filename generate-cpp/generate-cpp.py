#!/usr/bin/env python3
import sys
import json
import pathlib

mypath=(pathlib.Path(__file__).parent.resolve())

if len(sys.argv) < 4:
  print("Usage: %s <input_json_file> <output_src_file> <output_h_file>" % sys.argv[0])
  exit(1)

with open(sys.argv[1], 'r') as json_file:
  with open(sys.argv[2], 'w') as src_file:
    with open(sys.argv[3], 'w') as h_file:
      with open(mypath/'boilerplate-cpp.txt', 'r') as src_boilerplate:
        with open(mypath/'boilerplate-h.txt', 'r') as h_boilerplate:
          loggingDSL = json.load(json_file)

          src_file.write(src_boilerplate.read())
          h_file.write(h_boilerplate.read())

          for logStatement in loggingDSL['log_statements']:
            str='void %s (string context, ' % (logStatement['readable_id'])
            src_file.write(str)
            h_file.write(str)

            # write function arguments
            for idx, arg in enumerate(logStatement['arguments']):
              if idx != 0:
                src_file.write(', ')
                h_file.write(', ')
              str='%s %s' % (arg['type'], arg['name'])
              src_file.write(str)
              h_file.write(str)

            src_file.write(') {\n')
            h_file.write(');\n')

            # write function body
            src_file.write('\tcout\n\t\t<< msTimeStamp() << endl\n')
            src_file.write('\t\t<< "context: " << context << endl\n')
            src_file.write('\t\t<< "%s" << endl\n' % (logStatement['description']))
            for idx, arg in enumerate(logStatement['arguments']):
              if idx != 0:
                src_file.write('\n')
              src_file.write('\t\t<< "\t%s: " << %s << endl' % (arg['name'], arg['name']))

            src_file.write(';\n}\n\n')
          h_file.write('\n#endif\n')
