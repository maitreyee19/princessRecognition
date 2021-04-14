import PIL.Image
import PIL.ImageDraw
import face_recognition
import os
import numpy as np
import pandas as pd
from pathlib import Path

path = '/home/bhabani/Work/disney_character/princess1'
path_new = '/home/bhabani/Work/disney_character/princess_cropped'
if not os.path.exists(path_new):
    os.mkdir(path_new)


def face_location_find(file, directory):

    to_dir = directory.replace(path, path_new)
    print("destination_dir",to_dir)
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    # print(directory)
    image = face_recognition.load_image_file(directory + "/" + file)
    # print(type(image))
    face_locations = face_recognition.face_locations(image)
    #print(face_locations)

    if len(face_locations) > 0:
        top, right, bottom, left = face_locations[0]

        image_original = PIL.Image.open(directory + "/" + file)
        # img2 = image_original.crop((left, top, right, bottom))
        img_name = file.split(".")[0] + "_" + ".jpeg"
        img2 = image_original.crop((left, top, right, bottom))

        img2.save(to_dir+"/"+img_name,"JPEG")
        # pil_image2 = PIL.Image.fromarray(img2)
        # pil_image2.show()


def set_filetolabel(path):
    for root, directories, files in os.walk(path):
        for directory in directories:
            print(directory)
            # set_filetolabel(path + "/" + directory)
        for file in files:
            face_location_find(file, root)
            # image = face_recognition.load_image_file(file)
            # print("image",image)
            # face_locations = face_recognition.face_locations(image)
            # print(face_locations)
            # pil_image = PIL.Image.fromarray(image)
            # print("pil_image",pil_image)
            # for face_location in face_locations:
            #
            #     top, right, bottom, left = face_location
            #     draw = PIL.ImageDraw.Draw(pil_image)
            #     draw.rectangle([left, top, right, bottom], outline="red")

            # pil_image.show()


set_filetolabel(path)
