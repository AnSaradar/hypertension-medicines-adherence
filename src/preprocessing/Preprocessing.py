import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
import logging
def preprocess_input(data: dict):

    data_df = pd.DataFrame([data])

    numerical_cols = data_df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = data_df.select_dtypes(include=['object']).columns.tolist()
    logger = logging.getLogger('uvivorn.error')

    logger.error(f"numerical_cols : {numerical_cols}")
    logger.error(f"categorical_cols : {categorical_cols}")
    # numerical_cols = [
    #     'disease_duration', 'n_of_comorbidities', 'age', 
    #     'n_of_hypertension_medication', 'knowledge', 'difficulty_medication', 
    #     'distance_to_medication', 'medication_price_affect', 'phq2', 'bmq1'
    # ]
    
    # categorical_cols = [
    #     'sex', 'residency',
    # ]

    numerical_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder()
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ],
        remainder='passthrough'  
    )

    
    transformed_data = preprocessor.fit_transform(data_df)

    return transformed_data