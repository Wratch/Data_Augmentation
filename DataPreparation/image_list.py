import glob

"""
    -path
        -train
            .jpg
            .txt
            ..
        -test
            .jpg
            .txt
            ..
        -val
            .jpg
            .txt
            ..
    
    train.txt
        -path/train/name.jpg
    test.txt
        -path/test/name.jpg
    val.txt
        -path/val/name.jpg   

PLEASE CHECK THE PATH BEFORE RUN
"""

path = 'data/2_class/'
images_list = glob.glob(path+ "train/*.jpg")
print(images_list)

#Create training.txt file
file = open(path + "train.txt", "w")
file.write("\n".join(images_list))
file.close()


## Create test list txt ##


images_list_test = glob.glob(path + "test/*.jpg")
print(images_list_test)


#Create test.txt file
file = open(path + "test.txt", "w")
file.write("\n".join(images_list_test))
file.close()


#val
images_list_val = glob.glob(path + "val/*.jpg")
print(images_list_val)


#Create test.txt file
file = open(path + "val.txt", "w")
file.write("\n".join(images_list_val))
file.close()