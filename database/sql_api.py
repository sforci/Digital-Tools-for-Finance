#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import sqlalchemy
import pymysql

# Define API for SQL database

def create_sql_connection(SQL_USERNAME, SQL_PASSWORD, SQL_DB_NAME, verbose):

    # Connection settings
    SQL_DIALECT = "mysql"  # we are using MySQL
    SQL_DRIVER = "pymysql"  # pymsql provides an interface between MySQL and Python

    # The 
    SQL_URL = "{}+{}://{}:{}@localhost:3306/{}".format(SQL_DIALECT,
                                                       SQL_DRIVER,
                                                       SQL_USERNAME,
                                                       SQL_PASSWORD,
                                                       SQL_DB_NAME)
    engine = sqlalchemy.create_engine(SQL_URL, echo = verbose)
    return engine
    
def run_query(engine, query):
    # runs arbitrary SQL query     
    return engine.execute(query)

def read_sql_query(engine, query):
    # reads data and returns in a pandas dataframe
    return pd.read_sql(sql=query, con=engine)
    
def write_sql_query(engine, df, name):
    # write a pandas dataframe into a SQL server
    df.to_sql(con=engine, name = name, **{"if_exists": "replace", "index": False})

