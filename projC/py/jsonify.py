import os
import json
import inspect

input_file_prefix = 'output_'
output_file_prefix = 'output_json'
extension = 'json'
dirname = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

for i in range(1,4):
    with open(os.path.join(dirname,input_file_prefix + str(i) +"." + extension),"r",encoding="utf-8") as inp :
        with open(os.path.join(dirname,output_file_prefix + str(i) + "." + extension),"w+",encoding="utf-8") as out :
            out.write("[\n")
            for line in inp:
                if (line[len(line)-2]) == ',':
                    out.write(line)
                if (line[len(line)-2]) == '}':
                    line = line.replace("\n",",\n")
                    #print(line[len(line)-2])
                    out.write(line)
            out.write("]");
