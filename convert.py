import glob
import ntpath
import os

output_dir = "output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for f in glob.glob("*.rdp"):
    with open(f, 'r') as inputfile:
        with open('%s/%s' % (output_dir, ntpath.basename(f)), 'w') as outputfile:
            for line in inputfile:
                outputfile.write(line.replace('mohamed', 'gshaikh'))