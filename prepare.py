import numpy as np
import pandas as pd
import seaborn as sns
import env

def prep_iris(df):
    to_drop = ['species_id', 'measurement_id']
    
    df.drop(columns=to_drop, inplace=True)
    df.rename(columns={'species_name': 'species'}, inplace=True)
    dummy_iris = pd.get_dummies(df.species, drop_first=True)
    df = pd.concat([df, dummy_iris], axis=1)
    return df

def prep_titanic(df):
    df.drop(columns=['Unnamed: 0','passenger_id','class','deck','embarked'], inplace=True)
    dummy_titanic = pd.get_dummies(df[['sex','embark_town']], drop_first=True)
    df = pd.concat([df, dummy_titanic], axis=1)
    return df

def prep_telco(df):
    df = df.drop(columns=['internet_service_type_id', 'contract_type_id', 'payment_type_id'])
    dummy_df = pd.get_dummies(df[['multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']], drop_first=True)
    df = pd.concat( [df, dummy_df], axis=1 )
    return df

def split_dataset(df):
    import pandas as pd
    import numpy as np

    from sklearn.model_selection import train_test_split
    from sklearn.impute import SimpleImputer
    '''
    returns train, validate, test
    
    # 20% test, 80% train_validate
    # then of the 80% train_validate: 30% validate, 70% train.
    '''

    train, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train, test_size=.3, random_state=123)

    return train,validate,test