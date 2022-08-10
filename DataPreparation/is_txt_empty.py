import os
import glob
import argparse


def parser():
    parser = argparse.ArgumentParser(description="Check .txt data is empty")
    parser.add_argument("--input", type=str, help="Please enter input folder path")
    return parser.parse_args()


def check_txt(input_path):
    input_txt = os.path.join(input_path, '*.txt')
    list_of_txt = glob.glob(input_txt)
    i = 0
    for txt in list_of_txt:
        a = os.path.getsize(txt) == 0
        file_basename = os.path.basename(txt)
        file_name = os.path.splitext(file_basename)
        file_name = file_name[0]
        if a is True:
            i += 1
            os.remove(txt)
            os.remove(input_path + file_name + ".jpg")
    print(i)


if __name__ == '__main__':
    args = parser()
    input_path = args.input

    check_txt(input_path)
