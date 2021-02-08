# Data Augmentation Tools..

# Image Tiling 

## How to use on the command line : 

**python image_tiling.py --input input/ --destination result/ --divide_x 2 --divide_y 2 --extra_frame 30 --extension jpg** 

**--input** : Enter the location of the images and labels(txt files)

**--destination** : Enter the folder where the processed images and tags will be extracted

**--divide_x** : Enter how many equal parts you want to divide the x coordinate into

**--divide_y** : Enter how many equal parts you want to divide the y coordinate into

**--extra_frame** : Enter extra frame for overlap image 

**--extension** : Enter image extension (jpg,png)

## Txt files must be in yolo format:

```
1 0.716797 0.395833 0.216406 0.147222
0 0.687109 0.379167 0.255469 0.158333
1 0.420312 0.395833 0.140625 0.166667
```

## Original photo:

<img src="Assets/original.png" width="811" height="608" />


## After image tilling:
### <img src="Assets/processed1.png" width="405" height="304" /> <img src="Assets/processed2.png" width="405" height="304" />
<img src="Assets/processed3.png" width="405" height="304" /> <img src="Assets/processed4.png" width="405" height="304" />

