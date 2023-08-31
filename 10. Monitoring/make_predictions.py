import joblib
import pandas as pd
from sklearn.preprocessing import binarize

# Function to score the classifier
def predict_classifier(data):

    # load the X_scaler
    Classifier_X_scaler = joblib.load("../8. Models/StandardScaler_models/Classifier_X_scaler_19082023")
    
    # transform the data
    classifier_trans  = Classifier_X_scaler.transform(data)
    
    # load the classifier model
    catb_final = joblib.load('../8. Models/Classifier_models/catboost_classifier14082023')
    
    # make predictions
    predictions_prob = catb_final.predict_proba(classifier_trans)[:,1]
    
    predictions_label_binarized = binarize([predictions_prob],threshold=0.1423)[0]

    return predictions_prob, predictions_label_binarized


def predict_regressor(data):

    # load the regressor X_scaler
    regressor_X_scaler = joblib.load("../8. Models/StandardScaler_models/Regressor_X_Scaler_19082023")

    # transform the data
    regressor_trans = regressor_X_scaler.transform(data)

    # load the regressor model
    GBR_final = joblib.load("../8. Models/Regressor_models/GBRegressor_19082023")

    # make predictions
    predictions = GBR_final.predict(regressor_trans)
    predictions

    # load the y scaler
    y_scaler = joblib.load("../8. Models/StandardScaler_models/y_scaler26072023")

    # inverse transform the predictions
    predictions_inv = y_scaler.inverse_transform(predictions.reshape(-1,1))

    return predictions_inv