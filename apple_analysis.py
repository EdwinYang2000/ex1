# -*- coding:utf-8-

import pandas as pd
from pandas import DataFrame


def quarter_volume():
    data = pd.read_csv('/usr/local/anaconda3/apple.csv', header=0)
    i = pd.to_datetime(data['Date'])
    data_ts = DataFrame(data=data.values, columns=data.columns, index=i)
    data_ts = data_ts.drop(['Date', 'Open', 'High', 'Low', 'Close'], axis=1)
    data_ts_3M = data_ts.resample('3M').sum()
    second_volume_a = data_ts_3M.sort_values(by='Volume', ascending=False)
    second_volume = second_volume_a.iloc[1]['Volume']

    return second_volume