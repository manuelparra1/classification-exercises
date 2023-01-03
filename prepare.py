import numpy as np
import pandas as pd
import seaborn as sns
import env

def prep_iris(df):
    '''
    
    
    
    '''
    
    to_drop = ['species_id', 'measurement_id']
    
    df.drop(columns=to_drop, inplace=True)
    df.rename(columns={'species_name': 'species'}, inplace=True)
    dummy_iris = pd.get_dummies(df.species, drop_first=True)
    df = pd.concat([df, dummy_iris], axis=1)
    return df

def prep_titanic(df):
    '''
    
    accepts titanic dataframe
    
    removes unused columns, creates dummy columns for categorical values, and
    concatenates temporary variable holding dummies to main dataframe
    
    returns updated dataframe
    
    '''
    # Class, Deck, Embarked, are redundant
    df.drop(columns=['Unnamed: 0','passenger_id','class','deck','embarked'], inplace=True)
    dummy_titanic = pd.get_dummies(df[['sex','embark_town']], drop_first=True)
    df = pd.concat([df, dummy_titanic], axis=1)
    return df

def prep_telco(df):
    '''
    
    accepts Telco Churn Dataframe
    
    Fixes numerical column 'total_charges' in wrong data type, drops unused columns,
    creates dummy columns of categorical values (sorts bivariate & multivariate), and
    concatenates temporary variables holding 2 types of dummies to main dataframe
    
    
    '''
    
    # Fix incoming dataframe column with numerical values set as string type
    df['total_charges'] = (df.total_charges + '0').astype('float')
    
    # Remove useless columns from incoming dataframe
    df = df.drop(columns = ['internet_service_type_id', 'contract_type_id', 'payment_type_id'])
    
    # Temporary list with only names of categorical columns from incoming dataframe
    categorical_columns = df.drop(columns = 'customer_id').select_dtypes(include=object).columns.to_list()

    # Filtering list into 1 of 2 types of categorical columns:
    # e.g. BIVARIATE
    
    # Empty list to hold categorical columns with BIVARIATE values
    categorical_columns_binary = []

    # Loop to search binary values in categorical column
    for i in range(len(categorical_columns)):
        if len(df[categorical_columns[i]].value_counts()) == 2:
            categorical_columns_binary.append(categorical_columns[i])

    # Use new filled list with column names, from
    # filtered incoming dataframe, to create dummies
    categorical_columns_binary_dummies = pd.get_dummies(df[categorical_columns_binary],drop_first=True)

    # Filtering list into 2 of 2 types of categorical columns:
    # e.g. MULTIVARIATE
    
    # Empty list to hold categorical columns with MULTIVARIATE values
    categorical_columns_not_binary = []
    
    # Loop to search MULTIVARIATE values in categorical column
    for i in range(len(categorical_columns)):
        if len(df[categorical_columns[i]].value_counts()) > 2:
            categorical_columns_not_binary.append(categorical_columns[i])

    # Use new filled list with column names, from
    # filtered incoming dataframe, to create dummy column dataframes
    categorical_columns_not_binary_dummies = pd.get_dummies(df[categorical_columns_not_binary],drop_first=True)

    # Use both sets of dummy column dataframes to concatenate them
    # to main dataframe:

    df = pd.concat([df, categorical_columns_binary_dummies], axis=1)
    df = pd.concat([df, categorical_columns_not_binary_dummies], axis=1)
    return df

def split_dataset(df):
    import pandas as pd
    import numpy as np

    from sklearn.model_selection import train_test_split
    from sklearn.impute import SimpleImputer
    '''
    returns train, validate, test (in that order)
    
    uses train_test_split() from SciKit Learn - Model Selection
    
    20% test, 80% train_validate
    then of the 80% train_validate: 30% validate, 70% train.
    '''

    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

    return train,validate,test