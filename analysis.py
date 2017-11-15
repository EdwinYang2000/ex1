#!/usr/local/anaconda3/bin/python3
import json
import pandas as pd

def analysis(file,user_id):
    times = 0
    minutes = 0
    df = pd.read_json(file, sep=',')
    if df[df['user_id']==int(user_id)]: 
        times = df[df['user_id']==int(user_id)].shape[0]
        minutes = df[df['user_id']==int(user_id)]['minutes'].sum()
    

    return times,minutes
