#!/usr/bin/python
from sys import argv
import re
import os
import stat

"""Simple script that performs C-like includes (preprocessing). This is,
   substitutes lines matching '. [a-zA-Z_-]* #INCLUDE' with
   file content.

   Example use. Suppose, that file program.in contains line:
   . my_other_cool_library #INCLUDE

   After running ./compile.py program.in program this line
   will be substituted with my_other_cool_library content
   """

if len(argv) != 3:
    print "Usage:", argv[0], " [input_file] [output_file]"
    exit(1)

input_name = argv[1]
output_name = argv[2]

try:
    input = open(input_name, 'r')
    output = open(output_name, 'w+')
except IOError as err:
    print err.strerror+':', err.filename
    exit(2)

line_count = 0
for line in input.xreadlines():
    line_count += 1
    if re.match('.[ ]*[a-zA-Z_-]*[ ]+#INCLUDE[ ]*\n', line):
        file_name = re.findall('[a-zA-Z_-]+', line)[0]
        try:
            file = open(file_name, 'r')
            output.write(file.read())
            file.close()
        except IOError as err:
            print 'At', input_name+':'+str(line_count), ':', \
                  err.strerror+':', err.filename
            exit(2)
        output.write('\n')
    else:
        output.write(line)

input.close()
output.close()
os.chmod(output_name, stat.S_IRGRP | stat.S_IXGRP | stat.S_IRUSR |
        stat.S_IWUSR | stat.S_IXUSR | stat.S_IROTH | stat.S_IXOTH)
