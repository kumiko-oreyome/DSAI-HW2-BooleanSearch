import pandas as pd
import numpy as np

def load_querys(path='query.txt'):
    querys = []
    with open(path, mode='r',encoding='utf-8') as f :
       querys = f.readlines()
    return querys


def load_titles(path='source.csv'):
    raw = pd.read_csv(path)
    df = transform2df(raw)
    titles = df.iloc[:,:].values.ravel().tolist()
    return titles


#處理第一行不是header的問題
def transform2df(origin):
    title1 = origin.columns.values[1]
    _b = origin.iloc[:,:].values
    b = np.concatenate((np.array([title1]),_b[:,1]))
    df = pd.DataFrame(b,columns=['title'])
    return df

from functools import wraps
import time

def elapsed_time(message):
    def _elapsed_time(func):
        @wraps(func)
        def body(*args, **kwargs):
            print(message)
            start_time = time.time()
            ret = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            print(message)
            print('elapsed time %.3f'%(elapsed_time))
            return ret
        return body
    return _elapsed_time

