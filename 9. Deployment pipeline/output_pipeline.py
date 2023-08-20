def retrieve_output(venue_g, Total_Nbr_of_Items_g, Total_Price_g, 
                    Receipt_Date_g, Item_name_g, Item_Price_g):
    """
    This function calls on all the different components of the deployment pipeline 
    and returns the classifier and the regressor predictions and the shap values
    ready for visualizing the prediction contribution of features
    """

    import pandas as pd
    import pull_last_7_days_receipts as pull_data
    import derive_item_name_features as derive_features
    import data_transformers


    # pull data from database
    last_7_days = pull_data.read_last_7_days()
    
    # Attach guest data to database data
    last_7_days = pull_data.attach_new_receipt_data(last_7_days, venue_g, Total_Nbr_of_Items_g, Total_Price_g, 
                                                    Receipt_Date_g, Item_name_g, Item_Price_g)
    
    # Feature engineering using item_name, text feature
    last_7_days_classifier, last_7_days_regressor = derive_features.item_name_features(last_7_days)
    
    return data_transformers.transform_and_predict(last_7_days_classifier, last_7_days_regressor)