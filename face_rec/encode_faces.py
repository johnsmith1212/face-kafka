# import the necessary packages
import face_recognition

import pickle

import numpy
import cv2
import os

from utils import fr_utils


def embed_known_faces(path_to_dir,pkl_file_path,upsample=1,model='hog'):

    # takes in a path to dir of all the known face images 
    # returns the list of embeddings and their class labels (extracted from the dir name)
    # in a dict format
     

    known_embeddings = []
    known_names = []

    impaths = fr_utils.images_paths(path_to_dir)

    num_of_imgs = len(impaths)


    for i,impath in enumerate(impaths):

        # loading the image as rgb
        rgb = fr_utils.load_image(impath)
        

        name,fname = fr_utils.extract_name(impath)


        print('[INFO] processing image '+str(fname)+' : '+str(i)+ '/'+str(num_of_imgs-1))
        embeddings = fr_utils.embed(rgb,upsample,model)

        
        

        known_embeddings.append(embeddings)

        known_names.append(name)

        

    data = {'known_embeddings':known_embeddings,'known_names':known_names}
    

    #serialize embeddings in a pickle object

    print('[INFO] serializing embeddings...')

    fr_utils.serialize_embeddings(data,pkl_file_path)

    print('[INFO] serialization done!!')





if __name__ == "__main__":

    path_to_dir = 'imgs/known_faces'
    pkl_file_path = 'face_rec/embeddings.pickle'


    embed_known_faces(path_to_dir,pkl_file_path)
