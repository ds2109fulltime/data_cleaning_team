
import pandas as pd
import numpy as np
import seaborn as sns
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score


def  max_min (data,columna):
    minimos =  data.loc[data[columna].idxmin()]
    maximos =  data.loc[data[columna].idxmax()]
    return print('el valor minimo es:',minimos,'el valor maximo es:',maximos)


def nulos_0 (data):
    df = data.fillna(0)
    return df

def nulos_media (data,columna):
    mean_df = data[columna].mean()
    df = data.fillna(mean_df)
    return df


def automl(X_train,y_train,X_test,y_test):
    my_automl = AutoML(eval_metric='accuracy')
    my_automl.fit(X_train,y_train)
    preds = my_automl.predict(X_test)
    accuracy_score(preds, y_test)
    return accuracy_score
