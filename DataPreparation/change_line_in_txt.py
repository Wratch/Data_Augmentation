import os
import glob


# This script to change the class number of labeled data

input_path = "output/"

txt_path = os.path.join(input_path, '*.txt')
txt_list = glob.glob(txt_path)
i = 0

for txt in txt_list:
    with open(txt, 'r+') as file:
        new_file = []
        lines = file.readlines()
        for line in lines:
            ln_sp = line.split(' ')
            new_line = "{} {} {} {} {}".format(ln_sp[0].replace(ln_sp[0], '1'), ln_sp[1], ln_sp[2], ln_sp[3], ln_sp[4])
            new_file.append(new_line)
        print(new_file)
    with open(txt, 'w+') as file:
        for i in new_file:
            file.write(i)
