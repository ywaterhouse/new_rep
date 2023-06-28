import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plot

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
a = 5
test_series = pd.Series([6, 7, 8])
df = pd.DataFrame({'col_one' : [1, 2, 3], 'col_two': [4, 5, 6], 'col_three': test_series})
df.index = ['a', 'b', 'c']
df = df.reset_index(drop = True)
df_two = pd.DataFrame({'col_one' : df.col_two, 'col_two': df.col_three, 'col_three': df.col_one})
df_two['col_4'] = df_two.col_one + 10
"""
#
#read in spx and vix files
spx_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv', nrows = 1000000)
vix_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\VIX_Futures_Minutely.csv', nrows = 1000000)
"""ALL SPX"""

#change date time string into integer 
spx_df["quote_datetime"] = pd.to_datetime(spx_df.quote_datetime)


#change SPX timezone to VIX timezone
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern').dt.tz_convert('US/Central').dt.tz_localize(None)


spx2_df = spx_df.copy()

#calc spx minute returns 
spx_df['date'] = spx_df.quote_datetime.dt.date

spx_df['close'] = spx_df.close.replace(0, np.nan)
 
spx_df['spx_returns'] = spx_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))

#spx_df['spx_returns'].describe()

# ? optimal bins? log2(N) +1 

#plot of one minute returns
def opt_bins(returns):
    bin_num = int(np.log2(returns.count())+1)
    return bin_num 
#opt_bins = int(np.log2(one_ret.count())+1)

one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]

one_ret.plot.hist(bins = opt_bins(one_ret))
#one_ret.describe()

#calc spx 15 minute returns 
spx2_df = spx2_df.set_index(spx2_df['quote_datetime'])
spx2_df = spx2_df.resample('15T').last()

spx2_df['date'] = spx2_df.quote_datetime.dt.date

spx2_df['close'] = spx2_df.close.replace(0, np.nan)
 
spx2_df['spx_returns'] = spx2_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
two_ret = spx2_df['spx_returns'].loc[(spx2_df['spx_returns']>spx2_df['spx_returns'].mean()-spx2_df['spx_returns'].std()*3 )&(spx2_df['spx_returns']<spx2_df['spx_returns'].mean()+spx2_df['spx_returns'].std()*3 )]
two_ret.plot.hist(bins = opt_bins(two_ret))


#d = np.log(spx2_df['close'])/np.log(spx2_df['open'])
#d.plot.hist(bins=1000)
#new15_ret = spx2_df['spx_returns'].loc[(spx2_df['spx_returns']>spx2_df['spx_returns'].mean()-spx2_df['spx_returns'].std()*3 )&(spx2_df['spx_returns']<spx2_df['spx_returns'].mean()+spx2_df['spx_returns'].std()*3 )]
#new15_ret.describe()
#new15_ret.plot.hist(bins = 1000)

"""
!git add "file.py"
!git commit -m "My commit"
!git push origin master
!git push -u origin master
"""

"""ALL VIX"""
#making into 15 min interval 
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime) 
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').first()
vix_df = vix_df.dropna(how = 'all')
vix_df['trade_date'] = pd.to_datetime(vix_df['trade_date'])
vix_df['expiration'] = pd.to_datetime(vix_df['expiration'])
vix_df['front_month'] = False


#if trade date is less than expiration even after trade date is moved up a month, 

#for each index, if the trade_date is within a month before the trade date, that is a front_month 
for index in vix_df.index:
    vix_df.at[index,'month_diffs'] = vix_df.at[index,'expiration'] - vix_df.at[index,'trade_date']
    if vix_df.at[index,'month_diffs'] <= pd.Timedelta(days=31):
        vix_df.at[index,'front_month'] = True
    else:
        vix_df.at[index,'front_month'] = False

vix_get_front = vix_df.loc[vix_df['front_month'] == True]
vix_get_front['vix_returns'] = np.log(vix_get_front.close) - np.log(vix_get_front.close.shift(1))


"""  
    if vix_df.at[index,'date'] < vix_df.at[index,'expiration'] and :
        vix_df.at[index,'front_mon'] = True
    else: 
        vix_df.at[index,'front_mon'] = False
    print(date)
    if vix_df.at[index,'expiration'] == vix_df.at[index,'trade_date']:
        vix_df.at[index,'front_month'] = True
    # if the expiration index is " " then test to see if trade_date is a month before that 
    if vix_df.at[index,'expiration'] == 2004-0o5-19 and 2004-0o4-18 < vix_df.at[index,'trade_date'] < 2004-0o5-19:
        vix_df.at[index,'front_month'] = True
"""
# calcuate 

"""
vix_df.groupby(vix_df['expiration'])
#calculating difference between expiration and trade date 
vix_df['trade_date'] = pd.to_datetime(vix_df['trade_date'])
vix_df['expiration'] = pd.to_datetime(vix_df['expiration'])
"""

"""
vix_df['expiration'].unique()
vix_expirations = pd.to_datetime(vix_expirations)
vix_df['trade_date'] = pd.to_datetime(vix_df['trade_date'])
vix_df['expiration'] = pd.to_datetime(vix_df['expiration'])
vix_df.groupby('expiration')
vix_df['front_month'] = False
vix_front = False
"""
#vix_df['trade_month'] = vix_df.trade_date.dt.month  
#vix_df['expiration_month'] = vix_df.expiration.dt.month
#vix_df['month_diff'] = vix_df.expiration_month - vix_df.trade_month #calc month diffs in a different way, using for loop 
 
# get month and days diff 
#vix_df['trade_month'] = pd.to_datetime(vix_df['trade_date']).dt.month_name()
#vix_df['expiration_month'] = pd.to_datetime(vix_df['expiration']).dt.month_name()
#vix_df['trade_date'] = pd.to_datetime(vix_df['trade_date']).dt.date_name()
#vix_df['expiration_date'] = pd.to_datetime(vix_df['expiration']).dt.date_name()
#vix_df['trade_dayte'] = pd.to_datetime(vix_df['trade_date']).dt.day
#vix_df['expiration_date'] = pd.to_datetime(vix_df['expiration']).dt.day


#while trade_month has not hit that element in series and it is not less than 1 month 
#it will calc returns with that exp date 


#front month: if quote_datetime is less than a month away

""" New DF where calc occurs"""
#vix_get_front = vix_df.loc[vix_df['month_diff'] == 1]
#vix_get_front['vix_returns'] = np.log(vix_get_front.close) - np.log(vix_get_front.close.shift(1))

    #vix_df.at[index,'time_diff'] = ((vix_df.at[index,'trade_date'] - vix_df.at[index,'expiration'])/np.timedelta64(1, 'M'))
    # if more than a month after trade date, 


"""vix_df.groupby(vix_df['expiration'])
vix_df['expiration'] = pd.to_datetime(vix_df.expiration)
vix_df['front_month'] = False"""

#for index in vix_df.index:
#    if vix_df.month_diff < 1: 
    # if expiration date is more than a month after or before the trade date, then vix_df is false, else true 
#        vix_df.at[index, 'front_month'] = True
idk = vix_df.front_month.unique()
#vix_df.groupby(vix_df['expiration'])

#vix_ret = vix_df['vix_returns'].loc[(vix_df['vix_returns']>vix_df['vix_returns'].mean()-vix_df['vix_returns'].std()*3 )&(vix_df['vix_returns']<vix_df['vix_returns'].mean()+vix_df['vix_returns'].std()*3 )]
#vix_ret.plot.hist(bins = opt_bins(vix_ret))

"""
!git add "file.py"
!git commit -m "My commit"
!git push origin master
!git push -u origin master
"""

