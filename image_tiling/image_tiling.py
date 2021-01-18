import os
import glob
import math
from PIL import Image
import argparse


def parser():
    parser = argparse.ArgumentParser(description="Image tiling with YOLO (txt) labels")
    parser.add_argument("--input", type=str, help="Please enter input folder path")
    parser.add_argument("--destination", type=str, help="Please enter destination folder path")
    parser.add_argument("--divide_x", type=int, help="Please enter how much you want to divide x by")
    parser.add_argument("--divide_y", type=int, help="Please enter how much you want to divide y by")
    parser.add_argument("--extra_frame", type=int, default=0, help="Please enter extra frame size")
    parser.add_argument("--extension", type=str, default='jpg', help="Please enter the extension of images (jpg,png)")
    return parser.parse_args()


def image_tiling():
    ext = '*.' + extension
    input_images = os.path.join(input_path, ext)
    list_of_images = glob.glob(input_images)

    for image_path in list_of_images:
        print(image_path)
        image = Image.open(image_path)
        x_main, y_main = image.size
        x_ = x_main / divide_x
        y_ = y_main / divide_y

        # filename.jpg
        file_basename = os.path.basename(image_path)

        # filename
        file_name = os.path.splitext(file_basename)
        file_name = file_name[0]

        for i in range(0, divide_y):
            y1 = int(i * y_)
            y2 = int((i + 1) * y_ + extra_frame)
            y_name = i + 1
            for k in range(0, divide_x):
                x1 = int(k * x_)
                x2 = int((k + 1) * x_ + extra_frame)
                x_name = k + 1
                # Regional image cropping
                image.crop((x1, y1, x2, y2)).save(dest_path + file_name + "_" + str(x_name)
                                                  + str(y_name) + ".jpg")
                # Create a regional txt file
                with open(dest_path + file_name + "_" + str(x_name) +
                          str(y_name) + ".txt", "w"):
                    pass

        # Read coordinates from txt file
        with open(input_path + file_name + ".txt", 'r') as file:
            data = file.readlines()
            # Delete "\n" in list
            data = [x.strip() for x in data]

        i = 0
        while i < len(data):
            array = list(data[i].split(' '))
            cls = int(array[0])
            x = float(array[1])
            y = float(array[2])
            w = float(array[3]) * divide_x
            h = float(array[4]) * divide_y
            i += 1

            # Round the number upper and find region
            x_region = int(math.ceil(x / (1 / divide_x)))
            y_region = int(math.ceil(y / (1 / divide_y)))
            # Find the coordinates of object from the original images
            x_region_coord = x_main * x
            y_region_coord = y_main * y

            x = (x_region_coord - ((x_region - 1) * x_)) / (x_ + extra_frame)
            y = (y_region_coord - ((y_region - 1) * y_)) / (y_ + extra_frame)

            with open(dest_path + file_name + "_" + str(x_region) + str(y_region) + ".txt", "a") as file:
                print(str(cls), str(x), str(y), str(w), str(h), file=file)


if __name__ == '__main__':
    args = parser()
    input_path = args.input
    dest_path = args.destination
    divide_x = args.divide_x
    divide_y = args.divide_y
    extra_frame = args.extra_frame
    extension = args.extension

    image_tiling()
