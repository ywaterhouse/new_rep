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

#read in spx and vix files
spx_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv', nrows = 1000000)
vix_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\VIX_Futures_Minutely.csv', nrows = 1000000)

"""ALL SPX"""

#change date time string into integer 
spx_df["quote_datetime"] = pd.to_datetime(spx_df.quote_datetime)

#change SPX timezone to VIX timezone
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern').dt.tz_convert('US/Central').dt.tz_localize(None)

#calc spx minute returns 
spx_df['date'] = spx_df.quote_datetime.dt.date

spx_df['close'] = spx_df.close.replace(0, np.nan)
 
spx_df['spx_returns'] = spx_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))

#spx_df['spx_returns'].describe()

#plot of one minute returns
stand_minus = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]
stand_minus.plot.hist(bins = 1000)


#calc spx 15 minute returns 
# ideas - shif
spx2_df = spx_df.copy()
a = spx2_df.set_index(spx2_df['quote_datetime'])
c = a.resample('15T').asfreq()
#spx2_df['Datetime'] = spx_df.quote_datetime.dt.time
#a = spx2_df.set_index('Datetime')
#b = a.resample('15T')


