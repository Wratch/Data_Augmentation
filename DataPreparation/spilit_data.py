import glob
import os
import random
import shutil
import argparse

"""
-datas
    -1.jpg
    -1.txt
    -2.jpg
    -2.txt
    -3.jpg
    -3.txt
    ...

"""


def parser():
    parser = argparse.ArgumentParser(description="Split data - input -> train test val")
    parser.add_argument("--input", type=str, help="Please enter input folder path")
    parser.add_argument("--rate", tpye=list, default=[.8, .1, .1], help="Please enter distribution of rate(.8 .1 .1)")
    parser.add_argument("--extension", type=str, default='jpg', help="Please enter the extension of images (jpg,png)")
    return parser.parse_args()


def spilit_data(folder_name, ext=".jpg", train_r=.8, test_r=.1, val_r=.1):
    curr_path = os.path.dirname(os.path.abspath(__file__))

    os.chdir(curr_path + "/" + folder_name)
    files = glob.glob("*" + ext)
    print(curr_path + "/" + folder_name)
    random.shuffle(files)

    len_file = len(files)

    train_r = int(train_r * len_file)
    test_r = int(test_r * len_file)
    val_r = int(val_r * len_file)

    train_data = files[:train_r]
    test_data = files[train_r:train_r + test_r]
    val_data = files[train_r + test_r:]
    src = curr_path + "/" + folder_name
    dst = curr_path + "/" + 'output/'
    dst_train = dst + 'train/'
    dst_test = dst + 'test/'
    dst_val = dst + 'val/'

    dst_list = [dst, dst_train, dst_test, dst_val]
    for x in dst_list:
        if not os.path.exists(x):
            os.makedirs(x)

    it = 1
    for x in [train_data, test_data, val_data]:
        dst_name = dst_list[it]
        for file in x:
            txt_file = file.split('.')[0] + '.txt'

            shutil.copyfile(src + file, dst_name + file)
            shutil.copyfile(src + txt_file, dst_name + txt_file)
        it += 1


if __name__ == '__main__':
    args = parser()
    input_path = args.input
    rate_list = args.rate
    ext = args.extension

    train_r, test_r, val_r = rate_list
    spilit_data(input_path, ext, train_r=train_r, test_r=test_r, val_r=val_r)
