import cv2
import numpy as np
import pandas as pd

df=pd.read_csv("role_challenge_dataset_ground_truth.csv")

# text = 'Hello, OpenCV!'
# font = cv2.FONT_HERSHEY_SIMPLEX
# font_scale = 1
# font_color = (255, 255, 255)  # White color in BGR
# font_thickness = 2

# # Specify the position to place the text (bottom-left corner)
# text_position = (50, 50)

# # Add text to the image
# cv2.putText(image, text, text_position, font, font_scale, font_color, font_thickness)


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[2])/2.0
    y = (box[1] + box[3])/2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


# ofd_1_x,ofd_1_y,ofd_2_x,ofd_2_y,bpd_1_x,bpd_1_y,bpd_2_x,bpd_2_y
for i in range(0, 622):
    print(df.iloc[i])
    print(df['ofd_1_x'][i])
    ofd_1_x=df['ofd_1_x'][i]
    ofd_1_y=df['ofd_1_y'][i]

    ofd_2_x=df['ofd_2_x'][i]
    ofd_2_y=df['ofd_2_y'][i]

    bpd_1_x=df['bpd_1_x'][i]
    bpd_1_y=df['bpd_1_y'][i]

    bpd_2_x= df['bpd_2_x'][i]
    bpd_2_y= df['bpd_2_y'][i]

    print(ofd_1_x,ofd_1_y,ofd_2_x,ofd_2_y,bpd_1_x,bpd_1_y,bpd_2_x,bpd_2_y)

    img=df['image_name'][i]
    print(img)




    image_path = f'images/{img}'  # Replace with the actual image file path
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    print(height,width)
    size=(height, width)
    # Specify two points as (x1, y1) and (x2, y2)
    point1 = (ofd_1_x, ofd_1_y)
    point2 = (ofd_2_x, ofd_2_y)

    point3 = (bpd_1_x, bpd_1_y)
    point4 = (bpd_2_x, bpd_2_y)
    minx=min(ofd_1_x, ofd_2_x, bpd_1_x, bpd_2_x)
    miny=min(ofd_1_y, ofd_2_y, bpd_1_y, bpd_2_y)

    maxx=max(ofd_1_x, ofd_2_x, bpd_1_x, bpd_2_x)
    maxy=max(ofd_1_y, ofd_2_y, bpd_1_y, bpd_2_y)

    point5 = (minx, miny)
    point6 = (maxx, maxy)

    # Draw a red line between the two points
    color = (0, 0, 255)  # BGR color for red
    thickness = 2
    cv2.line(image, point1, point2, color, thickness)
    color = (255, 0, 0)
    cv2.line(image, point4, point3, color, thickness)

    color = (0, 255, 0)
    cv2.line(image, point5, point6, color, thickness)

    #rectangle

    plu=(minx,miny)
    prl=(minx,maxy)
    pll=(maxx,miny)
    pru=(maxx,maxy)
    thickness = 2
    color = (255, 255, 0)
    cv2.line(image, plu, prl, color, thickness)
    cv2.line(image, pll, pru, color, thickness)
    cv2.line(image, plu, pll , color, thickness)
    cv2.line(image, prl, pru, color, thickness)
    # color = (0, 255, 0)
    # cv2.line(image, point5, point8, color, thickness)

    # point7=(minx,maxy)
    # point8=(maxx,miny)
    # color = (0, 255, 0)
    # cv2.line(image, point7, point6, color, thickness)

    cv2.imwrite(f'label/{img}', image)



    # Display the image with the drawn line
    # cv2.imshow('Image with Drawn Line', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()