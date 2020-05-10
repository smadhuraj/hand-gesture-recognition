
import cv2
import numpy as np
import os

def resizeImage():

    for i in range(1, 400):
        try:
            if not os.path.exists('p'):
                os.makedirs('p')
            
            imageUrl = "Image"+ str(i)
            print(imageUrl)
            img = cv2.imread("pos/"+imageUrl+".jpg",cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("p/"+str(i)+".jpg",resized_image)
            print("sucsess ! image "+ str(i))
        except Exception as e:
            print(str(e))

resizeImage()


# def store_raw_images():
#     neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
#     pic_num = 1
    
#     if not os.path.exists('neg'):
#         os.makedirs('neg')
        
#     for i in neg_image_urls.split('\n'):
#         try:
#             print(i)
#             urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
#             img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
#             # should be larger than samples / pos pic (so we can place our image on it)
#             resized_image = cv2.resize(img, (100, 100))
#             cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
#             pic_num += 1
            
#         except Exception as e:
#             print(str(e))

# store_raw_images()