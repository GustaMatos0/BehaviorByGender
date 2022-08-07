import pandas as pd
import numpy as np
from os import path

def LoadData():
    # Estude os bancos de dados
    
    DatabaseOne = pd.read_csv(path.join(path.dirname(path.realpath(__file__)), "tweet_data.csv"), encoding = 'iso-8859-1')
    DatabaseTwoTrain = pd.read_csv(path.join(path.dirname(path.realpath(__file__)), "twitgen_train_201906011956.csv"), encoding = 'iso-8859-1')
    DatabaseTwoVal = pd.read_csv(path.join(path.dirname(path.realpath(__file__)), "twitgen_valid_201906011956.csv"), encoding = 'iso-8859-1')
    DatabaseTwoTest = pd.read_csv(path.join(path.dirname(path.realpath(__file__)), "twitgen_test_201906011956.csv"), encoding = 'iso-8859-1')
    
    
    # Agora só checar se tá tudo nos conforme
    try:
        DatabaseOne.head()
        DatabaseTwoTrain.head()
        DatabaseTwoVal.head()
        DatabaseTwoTest.head()
        
        return print("Done!")

    except: 
        return print("Deu merda")


# Importe essa função no seu arquivo. O notebook principal será criado apenas para análise.

## Teste da função

if __name__ == "__main__":
    
    LoadData()