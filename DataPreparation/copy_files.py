import os
import glob
import shutil

"""
-----
    -Input
        -f1
            -a1.jpg
            -a1.txt
            -a2.jpg
            -a2.txt
        -f2
            -b1.jpg
            -b1.txt
            ..
        -f3
            ..
    
    -output
        -a1.jpg
        -a1.txt
        -a2.jpg
        -a2.txt
        -b1.jpg
        -b1.txt
        ...
        
"""

folder_list = os.listdir('Input')

print(folder_list)
for folder in folder_list:
    files = glob.glob('Input/' + folder + '/*.jpg')
    for file in files:

        txt_file = file.split(".")[0] + '.txt'

        jpg_name = file.split('\\')[-1]
        txt_name = txt_file.split('\\')[-1]

        dst_jpg = 'output/' + jpg_name
        dst_txt = 'output/' + txt_name

        if not os.path.exists('output'):
            os.mkdir('output')

        print(file)
        print(txt_file)
        if os.path.exists(txt_file):
            shutil.copy(file, dst_jpg)
            shutil.copy(txt_file, dst_txt)