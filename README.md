# task-origin-medical

Dataset link: https://drive.google.com/drive/folders/1qaupQoJIj8xUx0_dQrIlDV5wD0xQsdkC
The dataset contains images and labels. The labels are 8 coordinates of two straight lines stored in a CSV file. The two straight lines are the ac and bd of the images given below.


## Problem:
To develop an algorithm that is capable of identifying the biparietal diameter and occipitofrontal landmark points in fetal axial images. 


![Screenshot from 2024-01-31 15-45-29](https://github.com/sanjoymollarpur/task-origin-medical/assets/89268947/6b13355d-e321-4275-84a3-5871e83def58)   


## Approach:
Finding the bounding box on the ellipse using YOLOV5. The width and height are the biparietal diameter and occipitofrontal diameter respectively which can be obtained from the bounding box. 


## Step 1

To get the diagonal coordinates from the CSV file run

python data-preparation-from-csv-file.py

## Step 2

To get YOLO format data in .txt file run

python convert-label-yolov5-format.py

## Step 3 

After getting the data ready run Jupyter notebook

## Folder structure

task origin medical:
----> Data:
      ---> train:
            ----> images:
                        1.jpg
                        2.jpg
                        .
                        .
            -----> labels:
                        1.txt
                        2.txt
                        .
                        .
        ---> test:
            ----> images:
                        1.jpg
                        2.jpg
                        .
                        .
            -----> labels:
                        1.txt
                        2.txt
                        .
                        .
---->yolov5
   

