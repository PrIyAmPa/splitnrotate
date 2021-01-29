import numpy as np
from PIL import Image
import os
Image_Directory="C:/Users/patel/OneDrive/Desktop/divide and rotate/images"
os.chdir(Image_Directory)
for images in os.listdir(Image_Directory):
    image = Image.open(images) 
    image_width, image_height=image.size
    image_width=int(image_width)
    image_height=int(image_height)
    
    image_arr = np.array(image) 
    imageleft=image_arr[0:image_height,0:int(image_width/2)]
    imageleftname="Left_"+ images +".jpg"
    rotatedleft = np.rot90(imageleft)
    rotatedleftimage=Image.fromarray(rotatedleft)
    rotatedleftimage=rotatedleftimage.save(imageleftname)
    #cv2.imwrite(imageleftname, rotatedleft)

    imageright=image_arr[0:image_height,int(image_width/2):image_width]
    imagerightname="Right_"+ images +".jpg"
    rotatedright = np.rot90(imageright)
    rotatedrightimage=Image.fromarray(rotatedright)
    rotatedrightimage=rotatedrightimage.save(imagerightname)
    

