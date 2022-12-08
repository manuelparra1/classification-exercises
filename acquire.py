import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import env as env
import os

def get_titanic_data():
    
    path = 'titanic.csv'
    file_exists = os.path.exists(path)
    
    if file_exists:
        df = pd.read_csv(path)
        
        return df
    
    else:
        url = env.get_db_url('titanic_db')

        sql_query = '''
                        SELECT *
                        FROM passengers;
                    '''
        df = pd.read_sql(sql_query, url)
        df.to_csv('titanic.csv')

        return df

def get_iris_data():
    
    path = 'iris.csv'
    file_exists = os.path.exists(path)
    
    if file_exists:
        df = pd.read_csv(path)
        
        return df
    
    else:
        url = env.get_db_url('iris_db')
        sql_query = '''
                        SELECT 
                        *
                        FROM measurements
                        JOIN species USING(species_id)
                    '''
        df = pd.read_sql(sql_query, url)
        df.to_csv('iris_db.csv')
        return df

def get_telco_data():
    
    path = 'telco.csv'
    file_exists = os.path.exists(path)
    if file_exists:
        
        df = pd.read_csv(path)
        
        return df 
    
    else:
        url = env.get_db_url('telco_churn')
        sql_query = '''
                        SELECT
                            *
                        FROM 
                            customers AS c
                        JOIN 
                            contract_types AS ct USING(contract_type_id)
                        JOIN 
                            internet_service_types as ist USING(internet_service_type_id)
                        JOIN
                            payment_types as pt USING(payment_type_id)
                    '''
        df = pd.read_sql(sql_query, url)
        df.to_csv('telco_churn.csv')
        return df