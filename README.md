<h1 style="color: green;">Home Shopping project</h1>

</p>
I have a tendency of collecting my shopping receipts. In May 2020, I decided to build a database of
these shopping receipts. This database is called Home Shopping. It has provided me with a useful way
not only of keeping an eye on my expenditure but also gaining insight into my consumption habbits:
<ul>
<li>where do I spend most of my money</li>
<li>How much have I spent in each venue overall</li>
<li>when do I spend most of my money</li>
<li>what do I spend most of my money on</li>
<li>what products do I buy most</li>
<li>How much do I spend per week, per month, per year</li>
<li>How many items do I buy per week, per month, per year</li>
<li>etc ...</li>
</ul>
</p>

<p>
Having gathered several years worth of data, I wanted to apply machine learning to this data.<br>
The project involves several tables from the database
<ul>
<li>Receipt table - This contains summary receipt data, total price, total number of items receipt date, receipt time and shopping venue</li>
<li>Payment table - This contains payment information e.g. payment type; cash, card, plan Card_Source; Contactless, Pin, 0,DB. DD, Transfer</li>
<li>Item table - This contains items/product information e.g. item name and item price</li>
</ul>
</p>

<h3 style="color: green;">Problem statement</h3>
<p>
I need a set of tools that guide my expenditure such that I feel more in control of
my expenditure while saving time spent shopping.<br>

I have a small fridge so I don't tend to bulk buy and consume over a longer period.
I buy small quantities, as a result I do many shopping trips in a week, which consumes
a very important resource, time.<br>

In additions, I go through phases where I buy lots of things in a short period of time
whether online or in store. This reflects negatively on my budget.<br>

With respect to the actually expenditure, I don't have a consistent expenditure pattern
i.e. there are significant variations/variance between expenditure on similar shopping trips.<br>

I want to smooth the shopping experience: I want to reduce the time spent shopping, the number of
trips I do per week; I want to reduce the variability in expenditure using a planning tool that
provides a good estimate of expenditure given shopping list.<br>

These tools will be used in combination to optimise the shopping experience: reduce time spent shopping
and stabilize expenditure.

</p>

<h3 style="color: green;">A problem on the nature of time series: Data</h3>
<p>
<strong>
Michael Burry did not have a time series/forcasting model that predicted an imenent
stock market crash in 2008. Instead, Michael stumbled onto data which indicated
a serious problem in the subprime lending, the rest is common sense.</strong><br><br>
<strong>
Back in 2006-2007 no financial forcasting models successfully predicted the crash in 2008:<br> 
they didn't have the data that indicated a serious problem in the underlying assets, subprime lending.</strong><br><br>
<strong>
Forecasting models do well when there is data supporting the trend:<br>
you can see a wave building by the sea side and follow it until it collapses but you can't
predict where and when it will collapse with certainty; nore where and when the next one will arise
with certainty, unless you have multiple detectors beneath the waters.</strong><br><br>
<strong>
But you know in advance that one will arise, eventually.</strong><br><br>

<h3 style="color: green;">A problem on the nature of time series: Algorithms</h3>
<strong>
Tree based algorithms such as random forest and XGBoost employ bootstrapping and are also used in combination with cross validation.
Bootstrapping process involves randomly sampling from the data the model is trained on. Thus, within the training set, relatively future
data is used to predict relatively past data i.e. data leakage.<br><br>

Cross validation is a powerful technique used in model validation; in splitting the data into k-folds each fold is used once as testing set
which means that the earlier folds, relative past data, will be used to validate later folds, relative future data i.e. data that wouldn't
otherwise be available at the time, will be used for model training. Once again, this is a form of data leakage.<br>

Developing time series models with these techniques is inconsistent with the intuition behind train test split for time series.
Given the much spoken success of these models, time series considerations when splitting the data into train and test should be ignored in general
as such consideration is already violated in training the models.<br></strong><br>
<strong>
So the question, is time series real data science?
</strong><br>

</p>

<h3 style="color: green;">What's inside</h3>
<h5 style="color: green;">1. Data extraction</h5>
<p>
Inside the Data Extraction folder the following tasks are accomplished:
<ul>
<li>Data extraction from database</li>
<li>New features creation (preliminary feature engineering)</li>
<li>Classifier target/Label definition</li>
<li>Exporting of the raw data to csv format</li>
</ul>
</p>

<h5 style="color: green;">2. Data</h5>
<p>
Inside the data folder you will find all of the datasets used in the project.<br>
Individual notebooks will read in or create these datasets
</p>

<h5 style="color: green;">3. Exploratory data analysis</h5>
<p>
Exploring the distributions of the features.
</p>

<h5 style="color: green;">4. Feature engineering</h5>
<p>
In here the following tasks are accomplished:
<ul><b>Classifier feature engineering</b>
<li>Creating dummy variables with pd.get_dummies</li>
<li>Split the data into training and testing</li>
<li>Scale the values using StandardScaler</li>
<li>Feature selection removing low variance features</li>
<li>Feature selection removing correlated features</li>
<li>Illustrate the features capacity to distinguish between the target classes </li>
<li>Export data for modelling</li>
</ul>

<ul><b>Regressor feature engineering</b>
<li>Creating dummy variables with pd.get_dummies</li>
<li>Split the data into training and testing</li>
<li>Scale the values using StandardScaler</li>
<li>Feature selection removing low variance features</li>
<li>Feature selection removing correlated features</li>
<li>Export data for modelling</li>
</ul>
</p>

<h5 style="color: green;">5. Modelling</h5>
<p>
In here is the classification and regression model training process. This includes:<br>
<ul><b>Classifier model training</b><br>
<li>Balancing the data with imblearn</li>
<li>Hyperparameter tuning with GridSearchCV</li>
<li>Model comparison: imbalanced vs balanced </li>
<li>Final feature selection using selectfrom</li>
<li>Final model evaluation with confusion matrix</li>
</ul>

<ul><b>Regressor model training</b><br>
<li>Hyperparameter tuning with GridSearchCV</li>
<li>Retrieving the best parameters for the top 4 models from GridSearchCV</li>
<li>Comparing VotingRegressor with the best model using cross validation</li>
<li>Working with the best model</li>
<li>Feature importance of the best model</li>
<li>Exporting the best model for evaluation</li>
</ul>
</p>

<h5 style="color: green;">6. Model evaluation</h5>
<p>
In here is the classifier and regressor model evaluations. This includes:<br>

<ul><b>Classifier model evaluation</b><br>
<li>Evaluating the CatBoost model</li>
<li>Comparing the CatBoost with the Random forest model</li>
<li>Visualizing Predicted probabilities by class attribute</li>
<li>Visualizing the distribution of predicted probability of class 1</li>
<li>Sensitivity threshold tuning</li>
<li>Receiver operating Characteristic Curve (ROC Curves) and Area Under the Curve (AUC)</li>
<li>Selecting Sensitivity and Specificity from ROC using a function</li>
<li>Visualizing sensitivity vs specificity threshold ranges</li>
</ul>

<ul><b>Regressor model evaluation</b><br>
<li>Final feature selection using selectfrom on the best model</li>
<li>Final model training</li>
<li>Validate the final model</li>
<li>Feature importance top features model</li>
<li>Exporting the evaluated best model</li>
</ul>
</p>

<h5 style="color: green;">7. Explain the models with SHAP</h5>
<p>
In here the models are explained from a global and local perspective. This includes:<br>
<ul><b>Classifier model explaination</b>
<li><b>Global fidelity:</b> An explaination of the positive and negative relationship between the features and the target from a wholistic model point of view</li>

<li><b>Local fidelity:</b> An explaination of how the model behaves for a single prediction i.e. the feature by feature contribution to the prediction</li>
</ul>

<ul><b>Regressor model explaination</b>
<li><b>Global fidelity:</b> An explaination of the positive and negative relationship between the features and the target from a wholistic model point of view</li>

<li><b>Local fidelity:</b> An explaination of how the model behaves for a single prediction i.e. the feature by feature contribution to the prediction</li>
</ul>
</p>

<h5 style="color: green;">8. Models</h5>
<p>
In here all the classifier, regressor and StandardScaler models are stored ready for use.
</p>

<h5 style="color: green;">9. Deployment pipeline</h5>
<p>
Inside is all the modules required to generate a new classifier and regressor prediction and to explain the predictions.<br>

This includes:<br>

<ul>
<li>Import the pipeline module <b>output_pipeline</b> to preprocess the data and generate the predictions and shap values.</li>
<li>Import the fidelity module <b>local_fidelity</b> to  generate the local explaination plots for the classifier and regressor models.</li>
<li>Display the retrieved data using print()</li>

</ul>

</p>

<h5 style="color: green;">10. Monitoring</h5>
<p>
This is where mock monitoring scenarios are developed to mimick real situations<br>
where after deployment two monitoring concerns are considered: no data drift and data drift.<br>
This includes:<br>
<ul><b>Generating classifier datasets</b><br>
<li>Create classifier reference dataset and append classifier predictions to it.</li>
<li>Create classifier current dataset no drift and append classifier predictions to it.</li>
<li>Create classifier current dataset with drift and append classifier predictions to it.</li>
<li>Run various evidently preset reports and export them to Reports folder</li>
</ul>

<ul><b>Generating regressor datasets</b><br>
<li>Create regressor reference dataset and append regressor predictions to it.</li>
<li>Create regressor current dataset no drift and append regressor predictions to it.</li>
<li>Create regressor current dataset with drift and append regressor predictions to it.</li>
<li>Run various evidently preset reports and export them to Reports folder</li>
</ul>

</p>

<h5 style="color: green;">11. Reports</h5>
<p>
In hear Evidently AI monitoring reports are stored.This includes:<br>
<ul>
<li>Data quality reports</li>
<li>Data drift reports</li>
<li>Model performance reports</li>
</ul>
</p>

<h5 style="color: green;">Next step</h5>
Looking forward, the objective is to:<br>
<ul>
<li>Rebuild the models to include important features that were left out of the SelectFrom algorithm</li>
<li>Consider regularization parameters for the models, non has been specified thus far, thus default was applied.</li>
<li>Add a data dictionary</li>
<li>Develop time series models for comparison</li>
<li>Build deep learning versions of the models for comparison.</li>
<li>To fully deploy the models with AWS</li>
</ul>
</p>
