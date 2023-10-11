import json
import pickle
import numpy as np

__locations= None
__data_columns= None
__model = None


def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1


    X = np.zeros(len(__data_columns))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
    if loc_index >= 0:
         X[loc_index] = 1

    return round(__model.predict([X])[0],2)
def get_location_name():
    return __locations


def load_saved_artifacts():
    print(" loading saved artiacts")

    global __locations
    global  __data_columns

    with open("./artifacts/colums.json",'r') as f:
        __data_columns=json.load(f)['data_colums']
        __locations=__data_columns[3:]
    global __model
    with open("./artifacts/real_estate_price_prediction_model.pickle",'rb') as f:
        __model=pickle.load(f)
        print("Loading is done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_name())
    print(get_estimated_price('5th Block Hbr Layout',1000,2,2))

