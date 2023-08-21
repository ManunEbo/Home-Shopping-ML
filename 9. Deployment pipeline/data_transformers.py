def transform_and_predict(input_data_1, input_data_2):
    import pandas as pd
    
    import joblib

    # Scaling the values
    from sklearn.preprocessing import binarize

    # For explaining the model output
    import shap

    # ***************************************************************************************************************
    # ***************************************** Classifier prediction ***********************************************
    # ***************************************************************************************************************

    # renaming input data
    last_7_days_classifier = input_data_1

    # ***************************************************************************************************************
    # load X_scaler
    
    Classif_X_scaler = joblib.load("../8. Models/StandardScaler_models/Classifier_X_scaler_19082023")

    last_7_days_classifier = Classif_X_scaler.transform(last_7_days_classifier)

    # ***************************************************************************************************************
    # load the classifier model
    catb_final = joblib.load('../8. Models/Classifier_models/catboost_classifier14082023')

    # Making predictions with stored model
    loaded_prob = catb_final.predict_proba(last_7_days_classifier)[:,1]

    # binarize with the threshold
    loaded_pred_class_binarize = binarize([loaded_prob],threshold=0.1423)[0]
    loaded_pred_class_binarize


    # ***************************************************************************************************************
    # *********************************** local fidelity for classifier *********************************************
    # ***************************************************************************************************************

    # Building the explainer
    explainer_clfier =  shap.TreeExplainer(catb_final)

    # Calculating shap_values
    shap_values_Clfier = explainer_clfier.shap_values(last_7_days_classifier)

    # Map feature names to the index of the shap values
    shap_Series_clfier = pd.Series(shap_values_Clfier[0,:], index=last_7_days_classifier.iloc[0,:].index)

    # The additive shap prediction for the instance
    shap_prediction_clfier = shap_Series_clfier.sum() + explainer_clfier.expected_value



    # ***************************************************************************************************************
    # ***************************************** Regressor prediction ************************************************
    # ***************************************************************************************************************

    # renaming input data
    last_7_days_regressor = input_data_2

   
    # load the StandardScaler
    X_scaler = joblib.load("../8. Models/StandardScaler_models/Regressor_X_Scaler_19082023")
    last_7_days_regressor = X_scaler.transform(last_7_days_regressor)


    # load the regressor model
    GBR = joblib.load("../8. Models/Regressor_models/GBRegressor_19082023")
    Scaled_expenditure_pred = GBR.predict(last_7_days_regressor)

    # load y_scaler for inverse transform
    y_scaler =  joblib.load("../8. Models/StandardScaler_models/y_scaler26072023")

    # inverse transform Expenditure_pred
    Inverse_transf_expenditure_pred = y_scaler.inverse_transform(Scaled_expenditure_pred.reshape(-1,1))

    # ***************************************************************************************************************
    # ************************************ local fidelity for regressor *********************************************
    # ***************************************************************************************************************

    # Building the explainer
    explainer_regress =  shap.TreeExplainer(GBR)

    # Calculating shap_values
    shap_values_regress = explainer_regress.shap_values(last_7_days_regressor)

    # Map feature names to the index of the shap values
    shap_Series_regress = pd.Series(shap_values_regress[0,:], index=last_7_days_regressor.iloc[0,:].index)

    # The additive shap prediction for the instance
    shap_prediction_regress = shap_Series_regress.sum() + explainer_regress.expected_value


    return loaded_pred_class_binarize, loaded_prob, shap_Series_clfier, shap_prediction_clfier, Inverse_transf_expenditure_pred, shap_Series_regress, shap_prediction_regress