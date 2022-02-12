"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.17.6
"""
from kedro.pipeline import node
import pandas as pd

def extract_data_firstN(data, nrows = 1000):
    df = catalog.load(data, nrows)
    return df

def downsize_numeric(df, dtypes,numbercols):
    dtype = {}
    
    for c in numbercols:
        if(dtypes[c] == 'int64' and df[c].max() <= 128 and df[c].min()>= -128):
            dtype[c] = 'int8'
        elif (dtypes[c] == 'int64' and df[c].max() <= 32767 and df[c].min() >= -32767):
            dtype[c] = 'int32'

        if (dtypes[c] == 'float64' and df[c].max() <= 32767 and df[c].min() >= -32767):
            dtype[c] = 'float32'
        
    return dtype

def generate_dtypes(data):
    df = extract_data_first200(data)
    
    dtypes = df.dtypes # Get the dtypes
    numbercols = list(df.select_dtypes(exclude=['object']).columns)
    cols = df.columns # Get the columns

    dtype = downsize_numeric(df, dtypes, numbercols)
    objcols = list(df.select_dtypes(include=['object']).columns)

    for c in objcols:
        dtype[c] = 'category'

    return dtype


def read_data():
    return 0