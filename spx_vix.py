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
 #vix front month returns
 
vix_df.groupby(vix_df['expiration'])
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime) 
vix_df['expiration'] = pd.to_datetime(vix_df.expiration)
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').first()

vix_df['front_month'] = False

#for index in vix_df.index:
vix_df['month_diff'] = (vix_df.at[index,'expiration'] - vix_df.at[index,'quote_datetime'])
    if vix_df.month_diff < 1: 
    # if expiration date is more than a month after or before the trade date, then vix_df is false, else true 
        vix_df.at[index, 'front_month'] = True

    vix_df['front_month'] = 'Yes'
idk = vix_df.month_diff.unique()
vix_df.groupby(vix_df['expiration'])

#vix_ret = vix_df['vix_returns'].loc[(vix_df['vix_returns']>vix_df['vix_returns'].mean()-vix_df['vix_returns'].std()*3 )&(vix_df['vix_returns']<vix_df['vix_returns'].mean()+vix_df['vix_returns'].std()*3 )]
#vix_ret.plot.hist(bins = opt_bins(vix_ret))
    
"""
!git add "file.py"
!git commit -m "My commit"
!git push origin master
!git push -u origin master
"""

