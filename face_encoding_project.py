import PIL.Image
import PIL.ImageDraw
import face_recognition
import os

import numpy as np
import pandas as pd
from pathlib import Path
import cv2


class PrincessFaceRecognition():
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def checkOpDirExists(self):
        if not os.path.exists(self.output_path):
            os.mkdir(self.output_path)

    def face_localization_crop(self, file, directory):
        '''

        :param file: the name of image File
        :param directory: the directory where the image exists
        The function calls  face_recognition.face_locations() to find four coordinates on image face
        then image will be cropped and will be saved in a new directory named <directory>_cropped having same subdir name as input
        '''

        to_dir = directory.replace(path, path_new)
        print("destination_dir", to_dir)
        if not os.path.exists(to_dir):
            os.mkdir(to_dir)
        # print(directory)
        image = face_recognition.load_image_file(directory + "/" + file)
        # print(type(image))
        face_locations = face_recognition.face_locations(image)

        if len(face_locations) > 0:
            top, right, bottom, left = face_locations[0]

            image_original = PIL.Image.open(directory + "/" + file)

            img_name = file.split(".")[0] + "_" + ".jpeg"
            img2 = image_original.crop((left, top, right, bottom))
            rgb_im = img2.convert('RGB')
            rgb_im.save(to_dir + "/" + img_name, "JPEG")
            # pil_image2 = PIL.Image.fromarray(img2)
            # pil_image2.show()

    def execute_faceRecognition(self):
        '''

        :param path: takes input directory path and call face_localization_crop function with input of each image along with the directory where it exists
        :return:
        '''
        self.checkOpDirExists()
        for root, directories, files in os.walk(path):
            for directory in directories:
                print(directory)

                # set_filetolabel(path + "/" + directory)
            for file in files:
                self.face_localization_crop(file, root)


# read_imageFile(path)

if __name__ == "__main__":
    path = '/home/bhabani/Work/disney_character/princess'
    path_new = '/home/bhabani/Work/disney_character/princess_cropped'
    princessCharacters = PrincessFaceRecognition(path, path_new)
    princessCharacters.execute_faceRecognition()
