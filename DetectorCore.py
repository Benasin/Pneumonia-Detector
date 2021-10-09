from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense
from keras.models import Model
import pandas as pd
import ntpath
from datetime import date
import keras.backend.tensorflow_backend as tb


class Pneumonia_Detector:
    def __init__(self, batch_size, img_dir):
        self.batch_size = batch_size
        self.img_dir = img_dir
        self.img_height, self.img_width = 224, 224
        self.df = pd.read_csv('patients_info.data')


    def write_csv(self, patient_id, percent, path):
        fdate = date.today().strftime('%d/%m/%Y')
        self.df = pd.read_csv('patients_info.data')
        a = {'ID': patient_id, 'Prediction': percent, 'Directory': path, 'Name': "empty", 'Birth': "empty", 'Date': fdate, 'Gender': "empty", 'Description':"empty"}
        self.df = self.df.append(a, ignore_index = True)
        self.df.to_csv('patients_info.data', index = False)
        

    def runs(self):
        tb._SYMBOLIC_SCOPE.value = True
        test_datagen = ImageDataGenerator(rescale=1. /255)
        test_gen = test_datagen.flow_from_directory(self.img_dir, (self.img_height, self.img_width), class_mode=None, batch_size=self.batch_size, shuffle = False)
        model = load_model("./fourth_try_model.h5")
        prediction = model.predict_generator(test_gen, verbose = 0)
        for predx in range(0,len(prediction)):
            percent = round(prediction[predx][0] * 100, 2)
            path = str(self.img_dir) + "/" + str(test_gen.filenames[predx])
            patient_id = ntpath.basename(path)[:-5]
            self.write_csv(patient_id, percent, path)
        self.df.sort_values(by=['Prediction'], inplace=True, ascending=False)
        self.df.to_csv('patients_info.data', index = False)
    
if __name__ == "__main__":
    predictor = Pneumonia_Detector(8, '/home/benasin/PneumoniaDetector/testing')
    predictor.runs()