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