import pandas as pd

def quarter_volume():   

    sumdata = []
    data1 = []
    data = pd.read_csv('apple.csv',header=0)
    date1 = pd.to_datetime(data['Date'])


    volume = data['Volume']
    for i in volume:
        data1.append(i)
    data2 = pd.Series(data1,index=date1)


    alldate = pd.date_range('2009-1-1','2016-12-31',freq=3*offsets.DateOffset(months=1))

    for i in alldate:
        if i=='2016-10-01':
            s1 = data2.truncate(before='2016-10-01',after='2016-12-31').sum()
            sumdata.append(s)
        else:
            s = data2.truncate(before=i,after=i+1).sum()
            sumdata.append(s)

    finaldata = pd.Series(sumdata,index=alldate)

    second_volume= finaldata.sort_values()
    second_volume = second_volume[-1]
    return second_volume


print(quarter_volume())