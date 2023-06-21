# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Wed May 31 12:18:04 2023)---
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
df.reset_index()
df.index = df.reset_index()
df.index = ['a', 'b', 'c']
df.index.reset_index()
df.reset_index()
df.reset_index(drop = True)
df.index = df.reset_index(drop = True)
df.reset_index(drop = True, inplace= True)
import pandas as pd
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = 5
df = pd.DataFrame({'col_one' : [1, 2, 3], 'col_two': [4, 5, 6]})
df.index = ['a', 'b', 'c']
df = df.reset_index()
df = df.reset_index(drop = True)
df = df['index'].reset_index(drop = True)
df = df.index.reset_index(drop = True)
df = df['index'].index.reset_index()
df = df['index'].reset_index()
df = pd.DataFrame({'col_one' : [1, 2, 3], 'col_two': [4, 5, 6]})
df.index = ['a', 'b', 'c']
df = df.reset_index()
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
import pandas as pd
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = 5
df = pd.DataFrame({'col_one' : [1, 2, 3], 'col_two': [4, 5, 6]})
df.index = ['a', 'b', 'c']
df = df.reset_index(drop = True)

## ---(Wed May 31 12:52:12 2023)---
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
df_two = pd.DataFrame({'col_one' : df.col_two, 'col_two': df.col_three, 'col_three': df.col_one})
df_two['col_4'] = df_two.col_one + 10

## ---(Mon Jun 12 14:56:19 2023)---
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
runcell(0, 'C:/Users/ywaterhouse/.spyder-py3/temp.py')
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')


df = pd.read_csv(f'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv')

df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv')
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
vix.df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\VIX_Futures_Minutely.csv',nrows= 1000000)
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')

## ---(Mon Jun 12 15:30:41 2023)---
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df.quote_datatime.astype(int)
spx_df.quote_datatime = spx_df.quote_datatime.astype(int)
runcell(0, 'C:/Users/ywaterhouse/.spyder-py3/temp.py')
spx_df.quote_datatime.to_numpy()
pd.quote_datatime.to_datetime(spx_df.quote_datatime)
pd.quote_datatime.to_datetime(spx_df)
pd.to_datatime.to_datetime(spx_df)
pd.to_datatime(spx_df)
for quote_datatime in spx_df: 
    pd.to_datatime(quote_datatime, format = '%Y-%m-%d %H:%M:%S.%f' )

## ---(Mon Jun 12 16:03:21 2023)---
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')

spx_df["quote_datatime"] = spx_df["quote_datatime"].apply(to_datatime)
spx_df["quote_datatime"] = spx_df["quote_datatime"].apply(to_datatime)
spx_df["quote_datatime"] = spx_df["quote_datatime"].apply(pd.to_datatime)
spx_df["quote_datatime"] = pd.to_datatime spx_df["quote_datatime"]
spx_df["quote_datatime"] = pd.to_datatime(spx_df["quote_datatime"])
spx_df["quote_datatime"] = pd.to_datetime(spx_df["quote_datatime"])
spx_df["quote_datatime"] = pd.to_datetime(spx_df["quote_datatime"],infer_datetime_format=True))
spx_df["quote_datatime"] = pd.to_datetime(spx_df["quote_datatime"],infer_datetime_format=True)
spx_df[quote_datatime] = pd.to_datetime(spx_df[quote_datatime],infer_datetime_format=True)
spx_df['quote_datetime''] = pd.to_datetime(spx_df['quote_datetime'],infer_datetime_format=True)
spx_df['quote_datetime'] = pd.to_datetime(spx_df['quote_datetime'],infer_datetime_format=True)

datatypes = df.dtypes

# Print the data types
# of each column
datatypes
datatypes = spx_df.dtypes

# Print the data types
# of each column
datatypes
spx_df['quote_datetime'] = pd.to_datetime(spx_df['quote_datetime'],infer_datetime_format=True)
spx_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv',parse_dates = ['quote_datetime'])
vix_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\VIX_Futures_Minutely.csv',nrows= 1000000)
spx_df['quote_datetime'] = pd.to_datetime(spx_df.'quote_datetime',format=True)
spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime,format=True)
datatypes = spx_df.dtypes

# Print the data types
# of each column
datatypes
timez = pd.Timestamp('quote_datime', tz= (US/Central))
timez = pd.Timestamp('quote_datime', tz= 'US/Central')
spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime,format=True)

timez = pd.Timestamp('quote_datime', tz= 'US/Central')
spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime,format=mixed)

timez = pd.Timestamp('quote_datime', tz= 'US/Central')
spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime,format='mixed')

timez = pd.Timestamp('quote_datime', tz= 'US/Central')
spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime,format='%Y%m%d')

timez = pd.Timestamp('quote_datime', tz= 'US/Central')
spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime,format='%Y%m%d')
spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime,format=True)

timez = pd.Timestamp('quote_datetime', tz= 'US/Central')
spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime,format=True)

spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime,format=True)

datatypes = spx_df.dtypes

# Print the data types
# of each column
datatypes
timez = pd.Timestamp('quote_datetime', tz= 'US/Central')
timez = pd.Timestamp(spx_df['quote_datetime'], tz= 'US/Central')
spx_df()
spx_df
timez = pd.Timestamp(spx_df['quote_datetime'], tz= 'US/Central')

spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime,format='mixed')


timez = pd.Timestamp(spx_df['quote_datetime'], tz= 'US/Central')
timez = pd.Timestamp(spx_df['quote_datetime'], tz= 'US/Central') 
timez
timez = pd.Timestamp('quote_datetime, tz= 'US/Central') 
timez
timez = pd.Timestamp('quote_datetime', tz= 'US/Central') 
timez
timez = pd.Timestamp(quote_datetime, tz= 'US/Central') 
timez
timez = pd.Timestamp('quote_datetime', tz= 'US/Central') 
timez
timez = pd.Timestamp(spx_df['quote_datetime'], tz= 'US/Central') 
timez
timez = pd.Timestamp.tz_localize(spx_df['quote_datetime'], tz= 'US/Central') 
timez
timez = pd.Timestamp(spx_df['quote_datetime']) 
timez
timez = pd.Timestamp(spx_df.quote_datetime) 
timez
timez = pd.Timestamp(spx_df['quote_datetime'],tz = "US/Central") 
timez

Timestamp.tz_localize(tz,ambiguous ='raise' , nonexistent = 'shift_forward' )
pd.Timestamp.tz_localize(tz,ambiguous ='raise' , nonexistent = 'shift_forward' )
pd.Timestamp.tz_localize(ambiguous ='raise' , nonexistent = 'shift_forward' )
pd.Timestamp.tz_localize( tz = 'UTC',ambiguous ='raise' , nonexistent = 'shift_forward' )
pd.Timestamp.tz_localize( tz = 'UTC', ambiguous ='raise' , nonexistent = 'shift_forward' )
pd.Timestamp.tz_localize(tz = 'UTC', ambiguous ='raise', nonexistent = 'shift_forward')
pd.Timestamp.tz_localize('UTC','raise', 'shift_forward')
timez = pd.Series.Timestamp.(spx_df['quote_datetime'],tz = "US/Central")
timez
timez = pd.Series.Timestamp(spx_df['quote_datetime'],tz = "US/Central")
timez
timez = pd.Timestamp.Series(spx_df['quote_datetime'],tz = "US/Central")
timez
timez = pd.Series.dt.tz_convert(spx_df['quote_datetime'],tz = "US/Central")
timez
spx_df.select_dtypes('quote_datetime')
spx_df.select_dtypes(spx_df['quote_datetime'])
spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime,format='mixed')
spx_df['quote_datetime'].tz_localize('UTC')
Timestamp.tz_convert(tz)
pd.Timestamp.tz_convert(tz)
pd.Timestamp.tz_convert(tz = 'US/Central')
pd.Timestamp.tz_convert('quote_datetime',tz = 'US/Central')
pd.Timestamp.tz_convert(spx_df['quote_datetime'],tz = 'US/Central')
pd.Series.dt.tz_convert(spx_df['quote_datetime'])
spx_df.tz_covert('UTC')
spx_df.tz_convert('UTC')
spx_df['quote_dateframe'].tz_convert('UTC')
spx_df['quote_datetime'].tz_convert('UTC')
for i in spx_df['quote_datetime']:
    i.tz_convert('UTC')
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
pd.Series.tz_localize(spx_df['quote_datetime'],ambiguous = 'raise', nonexistent = 'raise')
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
pd.Series.tz_localize(tz, spx_df['quote_datetime'],ambiguous = 'raise', nonexistent = 'raise')
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
pd.Series.tz_localize(tz = spx_df['quote_datetime'],ambiguous = 'raise', nonexistent = 'raise')
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
pd.Series.tz_localize(self,tz = spx_df['quote_datetime'],ambiguous = 'raise', nonexistent = 'raise')
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
pd.Series.tz_localize(self = spx_df['quote_datetime'],ambiguous = 'raise', nonexistent = 'raise')
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
pd.Series.tz_localize(self = spx_df['quote_datetime'],ambiguous = 'raise', nonexistent = 'raise', tz)
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
pd.Series.tz_localize(self = spx_df['quote_datetime'],tz,ambiguous = 'raise', nonexistent = 'raise')
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
pd.Series.tz_localize(spx_df['quote_datetime'],tz,ambiguous = 'raise', nonexistent = 'raise')
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
pd.Series.tz_localize(None)
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
pd.Series.tz_localize(tz = None)
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
pd.Series.tz_localize(self,tz = None)
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')

pd.Series.tz_localize(self = spx_df['quote_datetime'],tz = None)
for timex in spx_df['quote_datetime']:
    timex.tz_convert('UTC')
for timex in spx_df['quote_datetime']:
    tmx.tz_localize()
    timex.tz_convert('UTC')
for timex in spx_df['quote_datetime']:
    ttimex.tz_localize()
    timex.tz_convert('UTC')
for timex in spx_df['quote_datetime']:
    timex.tz_localize()
    timex.tz_convert('UTC')
for timex in spx_df['quote_datetime']:
    timex.tz_localize(timex,tz = None)
    timex.tz_convert('UTC')
for timex in spx_df['quote_datetime']:
    timex.tz_localize(timex,tz)
    timex.tz_convert('UTC')
for timex in spx_df['quote_datetime']:
    timex.tz_localize(tz = timex)
    timex.tz_convert('UTC')
pd.Timestamp(spx_df['quote_datetime'])
for timex in spx_df['quote_datetime']:
    timex.tz_localize(tz = timex)
    timex.tz_convert('UTC')
pd.Timestamp(spx_df['quote_datetime'])
for timex in spx_df['quote_datetime']:
    pd.Timestamp(spx_df['quote_datetime'])
    timex.tz_localize(tz = timex)
    timex.tz_convert('UTC')
for timex in spx_df['quote_datetime']:
    pd.Timestamp(timex)
    timex.tz_localize(tz = timex)
    timex.tz_convert('UTC')
pd.Timestamp.series(spx_df['quote_datetime'])
pd.Timestamp.Series(spx_df['quote_datetime'])
central = pytz.timezone('US/Central')
spx_df.index = spx_df.index.tz_localize.pytz('UTC').tz_convert(central)
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
datatypes = df.dtypes

# Print the data types
# of each column
datatypes
datatypes = spx_df.dtypes

# Print the data types
# of each column
datatypes
pd.to_datetime(spx_df["quote_datatime"],infer_datetime_format=True)
datatypes = spx_df.dtypes

# Print the data types
# of each column
datatypes
pd.to_datetime(spx_df["quote_datetime"],infer_datetime_format=True)
datatypes = spx_df.dtypes

# Print the data types
# of each column
datatypes
spx_df["quote_datetime"] = pd.to_datetime(spx_df["quote_datetime"])
pd.to_datetime(spx_df["quote_datetime"],infer_datetime_format=True)
datatypes = spx_df.dtypes

# Print the data types
# of each column
datatypes
spx_df["quote_datetime"] = pd.to_datetime(spx_df["quote_datetime"])

datatypes = spx_df.dtypes

# Print the data types
# of each column
datatypes

Series.dt.tz_convert(tz)
Series.dt.tz_localize(tz=spx_df['quote_datetime'])

pd.Series.dt.tz_localize(tz=spx_df['quote_datetime'])

spx_df["quote_datetime"] = pd.to_datetime(spx_df["quote_datetime"])

pd.Series.dt.tz_localize(self,tz=spx_df['quote_datetime'])
pd.Series.dt.tz_localize(self=spx_df['quote_datetime'],tz = none)
pd.Series.dt.tz_localize(self=spx_df['quote_datetime'],tz = None)
pd.Series()

pd.Series(spx_df["quote_datetime"])
pd.Timestamp.astimezone(tz= spx_df["quote_datetime"] )
pd.Timestamp.astimezone(self= spx_df["quote_datetime"], tz= 'US/Central')
pd.Series(pd.Timestamp.astimezone(self= spx_df["quote_datetime"], tz= 'US/Central'))
pd.dti.tz_convert(spx_df['quote_datetime'] ,tz = 'US/Central')

Series.dt.tz_convert(spx_df['quote_datetime'] ,tz = 'US/Central')
pd.Series.dt.tz_convert(spx_df['quote_datetime'] ,tz = 'US/Central')
spx_df['quote_datetime'].dt.tz_localize()
spx_df['quote_datetime'].dt.tz_localize('UTC')
spx_df['quote_datetime'].dt.tz_localize('US/Central')
timex = spx_df['quote_datetime'].dt.tz_localize('UTC')
timex.dt.tz_convert('US/Central')
timex = spx_df['quote_datetime'].dt.tz_localize('US/Eastern')
timex.dt.tz_convert('US/Central')

timex = spx_df['quote_datetime'].dt.tz_localize('US/Eastern')
timex = spx_df['quote_datetime'].dt.tz_localize('US/Eastern')
timex
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
timex = spx_df['quote_datetime'].dt.tz_localize('US/Eastern')
timex.dt.tz_convert('US/Central')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_convert('US/Central')
spx_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv')
vix_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\VIX_Futures_Minutely.csv',nrows= 1000000)

spx_df["quote_datetime"] = pd.to_datetime(spx_df["quote_datetime"])
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_convert('US/Central')
p.log(spx_df['open'])
np.log(spx_df['open'])
pd.np.log(spx_df['open'])
spx_open = pd.np.log(spx_df['open'])
spx_close = pd.np.log(spx_df['close'])
spx_open = pd.np.log2(spx_df['open'])
spx_close = pd.np.log2(spx_df['close'])
spx_open = pd.np.log5(spx_df['open'])
spx_close = pd.np.log5(spx_df['close'])
spx_open = pd.np.loge(spx_df['open'])
spx_close = pd.np.loge(spx_df['close'])

spx_open = pd.np.log(spx_df['open'])
spx_close = pd.np.log(spx_df['close'])
spx_open = pd.np.log(spx_df['open'])
spx_close = pd.np.log(spx_df['close'])

spx_returns = spx_open/spx_close
spx_open = pd.np.log(spx_df['open'])
spx_close = pd.np.log(spx_df['close'])

spx_returns = spx_open/spx_close

spx_df[spx_returns] = spx_returns
spx_returns = spx_open/spx_close

## ---(Tue Jun 13 12:53:07 2023)---
a = 5
test_series = pd.Series([6, 7, 8])
a = 5
test_series = pd.Series([6, 7, 8])
df = pd.DataFrame({'col_one' : [1, 2, 3], 'col_two': [4, 5, 6], 'col_three': test_series})
a = 5
test_series = pd.Series([6, 7, 8])
df = pd.DataFrame({'col_one' : [1, 2, 3], 'col_two': [4, 5, 6], 'col_three': test_series})
df.index = ['a', 'b', 'c']
a = 5
test_series = pd.Series([6, 7, 8])
df = pd.DataFrame({'col_one' : [1, 2, 3], 'col_two': [4, 5, 6], 'col_three': test_series})
df.index = ['a', 'b', 'c']
df = df.reset_index(drop = True)
df_two = pd.DataFrame({'col_one' : df.col_two, 'col_two': df.col_three, 'col_three': df.col_one})
df_two['col_4'] = df_two.col_one + 10
spx_returns = spx_close/spx_open
spx_open = pd.np.log(spx_df['open'])
spx_close = pd.np.log(spx_df['close'])

spx_returns = spx_close/spx_open
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv',n=10)
vix_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\VIX_Futures_Minutely.csv',nrows= 1000000)
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_returns = spx_open/spx_close
spx_df['spx_returns']= spx_returns

spx_df['close'].shift(1)
shift1 = spx_df['close'].shift(1)
spx_df['close' = spx_df['close'].shift(1)
spx_df['close'] = spx_df['close'].shift(1)
spx_close = pd.np.log(spx_df['close'])
spx_nextclose = pd.np.log(spx_df['close'])

spx_returns = spx_nextclose/spx_close

spx_df['spx_returns']= spx_returns

spx_df['close'] = spx_df['close'].shift(1)
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_return = pd.np.log(spx_df['close']/spx_df['close'].shift(1))
spx_return = np.log(spx_df['close']/spx_df['close'].shift(1))
if 8:30:00 in spx_df['quote_datetime'] :
    spx_return= 'nan'
spx_return = np.log(spx_df['close']/spx_df['close'].shift(1))
if '8:30:00' in spx_df['quote_datetime'] :
    spx_return= 'nan'
spx_return = np.log(spx_df['close']/spx_df['close'].shift(1))
if '08:30:00' in spx_df['quote_datetime'] :
    spx_return= 'nan'
spx_return = np.log(spx_df['close']/spx_df['close'].shift(1))
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
if '08:30:00' in spx_df['quote_datetime'] :
    spx_return= 'nan'
else:
    spx_return = np.log(spx_df['close']/spx_df['close'].shift(1))
spx_df.groupby('quote_datetime').apply('spx_return'="nan")
spx_df.groupby('quote_datetime').apply('spx_return'=="nan")
spx_df.groupby('quote_datetime', group_keys = True).apply('spx_return'=="nan")
spx_df.groupby('quote_datetime', group_keys = True).apply("nan")
spx_df.groupby('quote_datetime', group_keys = True).apply(spx_return= 'nan')
spx_df.groupby('quote_datetime', group_keys = True).apply(zero_return)

spx_df.groupby('quote_datetime', group_keys = True).apply(zero_return())
spx_df.groupby('quote_datetime', group_keys = True).apply('zero_return')
spx_df.groupby('quote_datetime', group_keys = True).apply(zero_ret())
def zero_ret():
    spx_return = 'nan'
    return spx_return

spx_df.groupby('quote_datetime', group_keys = True).apply(zero_ret())
spx_df.groupby('quote_datetime', group_keys = True)
spx_df.groupby('quote_datetime', group_keys = True).apply(np.log(spx_df['close']/spx_df['close'].shift(1)))
spx_df.Series.groupby('quote_datetime', group_keys = True).apply(np.log(spx_df['close']/spx_df['close'].shift(1)))
spx_df.groupby('quote_datetime', group_keys = True).apply(np.log(spx_df['close']/spx_df['close'].shift(1)))
spx_return = spx_df.groupby('quote_datetime', group_keys = True).apply(np.log(spx_df['close']/spx_df['close'].shift(1)))
spx_return = spx_df['quote_datetime'].groupby('quote_datetime',group_keys = True).apply(np.log(spx_df['close']/spx_df['close'].shift(1)))
spx_return = spx_df.groupby(spx_df['quote_datetime'],group_keys = True).apply(np.log(spx_df['close']/spx_df['close'].shift(1)))
spx_df.groupby('quote_datetime').apply(np.log(spx_df['close']/spx_df['close'].shift(1)))
spx_df.groupby(spx_df['quote_datetime']).apply(np.log(spx_df['close']/spx_df['close'].shift(1)))
spx_df.groupby(spx_df['quote_datetime']).apply(lambda x: np.log(spx_df['close']/spx_df['close'].shift(1)))
spx_df.groupby(spx_df['quote_datetime']).apply(spx_returns = lambda x: np.log(spx_df['close']/spx_df['close'].shift(1)), 'nan')
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')

## ---(Wed Jun 14 09:20:35 2023)---
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_convert('US/Central')
spx_df["quote_datetime"] = pd.to_datetime(spx_df.quote_datetime)
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_convert('US/Central')
spx_df["quote_datetime"] = pd.to_datetime(spx_df.quote_datetime)
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_convert('US/Central')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('nan')dt.tz_convert('US/Central')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('UTC')dt.tz_convert('US/Central')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('UTC').dt.tz_convert('US/Central')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('nan').dt.tz_convert('US/Central')
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')

spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_convert('US/Central')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('UTC')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_convert('US/Central')
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df['quote_datetime'].dt.tz_localize('None')
spx_df['quote_datetime'].dt.tz_convert('None')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_convert('US/Central').dt.tz_localize(None)
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern').dt.tz_convert('US/Central').dt.tz_localize(None)
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_convert('US/Central')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize(None)
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern').dt.tz_convert('US/Central').dt.tz_localize(None)
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df.groupby(spx_df['quote_datetime']).apply(spx_return = lambda x: np.log(x['close']/x['close'].shift(1)))
spx_df.groupby(spx_df['quote_datetime'],dropna = False ).apply(spx_return = lambda x: np.log(x['close']/x['close'].shift(1)))
spx_df.groupby(spx_df['quote_datetime']).apply(spx_return = lambda x: np.log(x['close']/x['close'].shift(1)))
spx_df.groupby(spx_df['quote_datetime']).apply(spx_return = lambda x: np.log(spx_df['close']/spx_df['close'].shift(1)))
spx_df.groupby(spx_df['quote_datetime']).apply(spx_return = lambda x: np.log(x['close']/x['close'].shift(1)))
spx_df.groupby(spx_df['quote_datetime']).apply(lambda x: np.log(x['close']/x['close'].shift(1)))
spx_df.groupby(spx_df['quote_datetime']).apply(lambda x: np.log((x['close']-(x['close'].shift(1))/x['close']))
spx_df.groupby(spx_df['quote_datetime']).apply(lambda x: np.log((x['close']-(x['close'].shift(1))/x['close'])))
spx_df.groupby(spx_df['quote_datetime']).apply(lambda x: np.log((x.close-(x.close.shift(1))/x.close)))
spx_df['date'] = spx_df['quote_datetime'].dt.date
spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log((x.close-(x.close.shift(1))))
spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log((x.close-(x.close.shift(1)))))
spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(spx_returns = lambda x: np.log((x.close-(x.close.shift(1)))))
runcell(0, 'C:/Users/ywaterhouse/.spyder-py3/temp.py')
spx_returns = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log((x.close-(x.close.shift(1)))))
spx_df['spx_returns']= spx_returns
spx_returns = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log((x.close-(x.close.shift(1)))))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log((x.close-(x.close.shift(1)))))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log((x.close-x.close.shift(1))))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log(x.close-x.close.shift(1)))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log(x.close) - np.log(x.close.shift()))

spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log(x.close) - np.log(x.close).shift()))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log(x.close) - np.log(x.close).shift())
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x:spx_df['quote_datetime'].np.log(x.close) - np.log(x.close.shift()))
runcell(0, 'C:/Users/ywaterhouse/.spyder-py3/temp.py')
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x:spx_df['quote_datetime'] np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'].dt.date).apply(lambda x: np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime.dt.date.apply(lambda x: np.log(x.close) - np.log(x.close.shift())))
spx_df['spx_returns'] = spx_df.groupby((spx_df['quote_datetime'].dt.date).apply(lambda x: np.log(x.close) - np.log(x.close.shift())))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime']['date'].apply(lambda x: np.log(x.close) - np.log(x.close.shift())))
#spx_df['spx_returns']= spx_returns
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime.date.apply(lambda x: np.log(x.close) - np.log(x.close.shift())))
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime).dt.date.apply(lambda x: np.log(x.close) - np.log(x.close.shift())))
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime).dt.date.apply(lambda x: np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby((spx_df.quote_datetime).dt.date).apply(lambda x: np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby((spx_df.quote_datetime).dt.date)    .apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime.date).apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime.date.apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift())))

## ---(Wed Jun 14 10:51:12 2023)---
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
runcell(0, 'C:/Users/ywaterhouse/.spyder-py3/temp.py')
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime.dt.date.apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift())))
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime.dt.date).apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby(quote_datetime.dt.date).apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby(['quote_datetime'].dt.date.apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby(['quote_datetime'].dt.date.apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift())))
spx_df['spx_returns'] = spx_df.groupby(['quote_datetime'].date.apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift())))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'])date.apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift())))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'])date.apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime']).date.apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift()))
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'.date]).apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift))

## ---(Wed Jun 14 10:58:35 2023)---
spx_df['spx_returns'] = spx_df.groupby(spx_df['quote_datetime'].date).apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift))
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df['spx_returns'] = spx_df.groupby('quote_datetime'.date).apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift))
spx_df['spx_returns'] = spx_df.groupby(dt.date).apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift))
spx_df['spx_returns'] = spx_df.groupby(spx_df.dt.date).apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift))

## ---(Wed Jun 14 11:01:09 2023)---

spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime).apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift))
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime.dt.date).apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift))
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime).dt.date.apply(lambda x = spx_df: np.log(x.close) - np.log(x.close.shift))
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime).dt.date.apply(lambda x : np.log(x.close) - np.log(x.close.shift))

spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime).date.apply(lambda x : np.log(x.close) - np.log(x.close.shift))

spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime.dt.date).apply(lambda x : np.log(x.close) - np.log(x.close.shift))
spx_df = spx_df.close.dropna()
spx_temp = spx_df

spx_df["quote_datetime"] = pd.to_datetime(spx_df.quote_datetime)

#change SPX timezone to VIX timezone
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern').dt.tz_convert('US/Central').dt.tz_localize(None)
spx_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv', nrows = 1000000)
spx_df["quote_datetime"] = pd.to_datetime(spx_df.quote_datetime)

#change SPX timezone to VIX timezone
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern').dt.tz_convert('US/Central').dt.tz_localize(None)
spx_temp = spx_df
spx_temp = spx_temp.close.replace(0, 'nan')
spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.quote_datetime.dt.date).apply(lambda x : np.log(x.close) - np.log(x.close.shift))
spx_temp = spx_df
spx_temp['close'] = spx_temp.close.replace(0, 'nan')

spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.quote_datetime.dt.date).apply(lambda x : np.log(x.close) - np.log(x.close.shift))
spx_temp['close'] = spx_temp.close.replace(0, np.nan)

spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.quote_datetime.dt.date).apply(lambda x : np.log(x.close) - np.log(x.close.shift))
spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.quote_datetime.dt.date)['close'].apply(lambda x : np.log(x.close) - np.log(x.close.shift))
spx_temp['close'] = spx_temp.close.replace(0, np.nan)
spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.quote_datetime.dt.date)['close'].apply(lambda x : np.log(x.close) - np.log(x.close.shift))
spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.quote_datetime.dt.date)[['close']].apply(lambda x : np.log(x.close) - np.log(x.close.shift))
spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.quote_datetime.dt.date)['close'].apply(lambda x : np.log(x) - np.log(x.shift))
spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.quote_datetime.dt.date)['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
blah = spx_temp.groupby(spx_temp.quote_datetime.dt.date)

spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.quote_datetime.dt.date)['close']

blah = spx_temp.groupby(spx_temp.quote_datetime.dt.date)['close']
spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.quote_datetime)['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))

spx_temp['spx_returns'] = spx_temp.groupby(by =[quote_datetime.dt.date])['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx_temp['spx_returns'] = spx_temp.groupby(by =['quote_datetime'.dt.date])['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx_temp['spx_returns'] = spx_temp.groupby(by =['quote_datetime.dt.date'])['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))

spx_temp['spx_returns'] = spx_temp.groupby(by =['quote_datetime'])['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx_df['date'] = spx_df.quote_datetime.dt.date
spx_temp = spx_df
spx_temp['close'] = spx_temp.close.replace(0, np.nan)
spx_temp['spx_returns'] = spx_temp.groupby(by='date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx_temp['spx_returns'] = spx_temp.groupby(by='date', dropna = True)['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))

spx_temp['spx_returns'] = spx_temp.groupby(by='date').apply(lambda x : np.log(x.close) - np.log(x.close.shift

spx_temp['spx_returns'] = spx_temp.groupby(by='date').apply(lambda x : np.log(x.close) - np.log(x.close.shift(1)))


spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.date).apply(lambda x : np.log(x.close) - np.log(x.close.shift(1)))
spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.date)['close'].apply(lambda x : np.log(x.close) - np.log(x.close.shift(1)))

spx_temp['spx_returns'] = spx_temp.groupby(spx_temp.date)['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))


spx_temp['spx_returns'] = spx_temp.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx_temp['close'] = spx_temp.dropna()
spx_temp = spx_temp.dropna()
spx_temp = spx_temp.dropnan()
spx_temp['close'] = spx_temp.close.dropna()
spx_temp.dropna(inplace = True)
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_temp['spx_returns'] = spx_temp.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx_temp = spx_df
spx_temp['close'] = spx_temp.close.replace(0, np.nan)
spx_temp.dropna(inplace = True)

spx_temp['spx_returns'] = spx_temp.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df['close'] = spx_df.close.replace(0, np.nan)
spx_df.dropna(inplace = True)

spx_df['spx_returns'] = spx_df.groupby('date', group_keys=True)['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv', nrows = 1000000)
vix_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\VIX_Futures_Minutely.csv', nrows = 1000000)

"""SPX cleaning and calculations"""

#change date time string into integer 
spx_df["quote_datetime"] = pd.to_datetime(spx_df.quote_datetime)

#change SPX timezone to VIX timezone
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern').dt.tz_convert('US/Central').dt.tz_localize(None)
spx_df['date'] = spx_df.quote_datetime.dt.date
#calc spx minute returns 


spx_df['close'] = spx_df.close.replace(0, np.nan)
spx_df.dropna(inplace = True)

spx_df['spx_returns'] = spx_df.groupby('date', group_keys=True)['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv', nrows = 1000000)
vix_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\VIX_Futures_Minutely.csv', nrows = 1000000)

"""SPX cleaning and calculations"""

#change date time string into integer 
spx_df["quote_datetime"] = pd.to_datetime(spx_df.quote_datetime)

#change SPX timezone to VIX timezone
spx_df['quote_datetime'] = spx_df['quote_datetime'].dt.tz_localize('US/Eastern').dt.tz_convert('US/Central').dt.tz_localize(None)
spx_df['date'] = spx_df.quote_datetime.dt.date
#calc spx minute returns 


spx_df['close'] = spx_df.close.replace(0, np.nan)
spx_df.dropna(inplace = True)

spx_df['spx_returns'] = spx_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime.dt.date)['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx_df['spx_returns'] = spx_df.groupby(spx_df.quote_datetime.dt.date)[spx_df.close].apply(lambda x : np.log(x) - np.log(x.shift(1)))
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df['spx_returns'] = spx_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx_df['date'] = spx_df.quote_datetime.dt.date

spx_df['close'] = spx_df.close.replace(0, np.nan)

spx_df['spx_returns'] = spx_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
'spx_returns'.plot()
spx_df['spx_returns'].plot()
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df['spx_returns'].plot()
spx_df['spx_returns'].hist()
spx_df.plt.density()
spx_df['spx_returns'].plt.density()
spx_df['spx_returns'].plot.density()
spx_df['spx_returns'].hist.density()

spx_df['spx_returns'].plot.kde()
spx_df['spx_returns'].plot.kde(y = 'SPX returns')
spx_df['spx_returns'].plot.kde(ylabel = 'SPX returns')

spx_df['spx_returns'].plot.hist(xlabel='distrib',ylabel= 'returns', xlim = .75 )
np.normal(spx_df.spx_returns)
plot.normal(spx_df.spx_returns)
spx_df.spx_returns.plot.normal()
spx_df.spx_returns.plot.hist(xlabel='distrib', ylabel= 'returns', xlim = .75)
#spx_df['spx_returns'].hist()
spx_df.spx_returns.plot.hist(xlabel='distrib', ylabel= 'returns', xlim = .75, ylim = 40)
spx_df.spx_returns.plot.(xlabel='distrib', ylabel= 'returns', xlim = .75, ylim = 40)

spx_df.spx_returns.plot(xlabel='distrib', ylabel= 'returns', xlim = .75, ylim = 40)

spx_df.spx_returns.plot()
ax = spx_df.spx_returns.plot()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax = spx_df.spx_returns.plot.hist()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax = spx_df.spx_returns.plot.hist()
ax.set_xlabel('returns')
ax.set_ylabel('frequency')
ax = spx_df.spx_returns.plotting()
ax.set_xlabel('returns')
ax.set_ylabel('frequency')
spx_df.spx_returns.plot(x,stats.norm.pdf())
runcell(0, 'C:/Users/ywaterhouse/.spyder-py3/temp.py')
spx_df.spx_returns.plot(stats.norm.pdf())
spx_df.spx_returns.plot.stats.norm.pdf()

ax = spx_df.spx_returns.plt.hist(normed=True)
ax.set_xlabel('returns')
ax.set_ylabel('frequency')
ax = spx_df.spx_returns.plot()
ax.set_xlabel('returns')
ax.set_ylabel('frequency')
ax = spx_df.spx_returns.plot.hist()
ax.set_xlabel('returns')
ax.set_ylabel('frequency')
ax = spx_df.spx_returns.plot.hist.kde()
ax.set_xlabel('returns')
ax.set_ylabel('frequency')
ax = spx_df.spx_returns.plot.hist(xlim = [spx_returns -3, spx_returns +3])
ax.set_xlabel('returns')
ax.set_ylabel('frequency')
ax = spx_df.spx_returns.plot.hist(xlim = [spx_df.spx_returns -3, spx_df.spx_returns +3])
ax.set_xlabel('returns')
ax.set_ylabel('frequency')
#spx_df['spx_returns'].hist()
ax = spx_df.spx_returns.plot.dkde(xlim = [spx_df.spx_returns -3, spx_df.spx_returns +3])
ax = spx_df.spx_returns.plot.kde(xlim = [spx_df.spx_returns -3, spx_df.spx_returns +3])

ax = spx_df.spx_returns.plot.hist(xlim = [spx_df.spx_returns -3, spx_df.spx_returns +3])
ax.set_xlabel('returns')
ax.set_ylabel('frequency')
ax = spx_df.spx_returns.plot.kde(xlim = [spx_df.spx_returns -3, spx_df.spx_returns +3])
ax.set_xlabel('returns') 
ax.set_ylabel('frequency')

## ---(Wed Jun 14 13:33:38 2023)---
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
ax = spx_df.spx_returns.plot.kde(xlim = [spx_df.spx_returns -1, spx_df.spx_returns +1])

spx_df.spx_returns.plot()
ax = spx_df.spx_returns.plot.kde(xlim = [spx_df.spx_returns -.2, spx_df.spx_returns +1])
ax = spx_df.spx_returns.plot.kde('x' : -.5,0,.5,1)
ax = spx_df.spx_returns.plot.kde('x' : [-.5,0,.5,1])
ax = spx_df.spx_returns.plot()
ax.set_xlabel('returns') 
ax.set_ylabel('frequency')
ax = spx_df.spx_returns.plot.hist()
ax.set_xlabel('returns') 
ax.set_ylabel('frequency')
ax.set_xlim(-3,3)
ax = spx_df.spx_returns.plot.hist()
ax.set_xlabel('returns') 
ax.set_ylabel('frequency')
ax.set_xlim(-.5,.5)
ax = spx_df.spx_returns.plot.kde()
ax.set_xlabel('returns') 
ax.set_ylabel('frequency')
ax.set_xlim(-.5,.5)
ax = spx_df.spx_returns.plot.hist()
ax.set_xlabel('returns') 
ax.set_ylabel('frequency')
ax.set_xlim(-.5,.5)
ax = spx_df.spx_returns.plot.hist()
ax.set_xlabel('returns') 
ax.set_ylabel('frequency')
ax.set_xlim(-.2,.2)
ax = spx_df.spx_returns.plot.hist(bins=1000)
ax.set_xlabel('returns') 
ax.set_ylabel('frequency')
ax.set_xlim(-.2,.2)
spx_df['spx_returns'].hist(bins=10000)
spx_df['spx_returns'].describe()
def remove_outliers():
    Q1 = spx_df.spx_returns.quantile(.25)
    Q3 = spx_df.spx_returns.quantile(.25)
    IQR = Q3 - Q1
    trueList = ~((spx_df.spx_returns < (Q1 - 1.5 * IQR)) |(spx_df.spx_returns > (Q3 + 1.5 * IQR)))
    return trueList
#plot minutely 

spx_df['clean_returns'] = spx_df['spx_returns'].remove_outliers()
Q1 = spx_df.spx_returns.quantile(.25)
Q3 = spx_df.spx_returns.quantile(.75)
print(f'{Q1},{Q3}')
stdev(spx_df['spx_returns'])
std.(spx_df['spx_returns'])
(spx_df['spx_returns']).std()
(spx_df['spx_returns']).std()
(spx_df['spx_returns']).std(2)
spx_df.loc[spx_df['spx_returns']<0.03]
spx_df.loc[spx_df['spx_returns']<11]
spx_df.loc[spx_df['spx_returns']<11]
spx_df.loc[spx_df['spx_returns']>-5]
spx_df['clean_returns'] = spx_df['spx_returns'].remove(stand_plus)

spx_df['clean_returns'] = spx_df['spx_returns'].drop(stand_plus)

spx_df['clean_returns'] = spx_df['spx_returns'].drop('stand_plus')

spx_df['clean_returns'] = spx_df['spx_returns'].drop(spx_df.loc[spx_df['spx_returns']<11])
stand_plus = spx_df.loc[spx_df['spx_returns']<11]
stand_minus = spx_df.loc[spx_df['spx_returns']>-5]
spx_df['clean_returns'] = spx_df['spx_returns'].drop(spx_df.loc[-5<spx_df['spx_returns']<11])
stand_plus = spx_df.loc[-5<spx_df['spx_returns']<11]
stand_plus = spx_df.loc[spx_df['spx_returns']<11]
stand_minus = spx_df.loc[spx_df['spx_returns']>-5]
stand_plus = spx_df['spx_returns'].loc[spx_df['spx_returns']<11]
stand_minus = spx_df['spx_returns'].loc[spx_df['spx_returns']>-5]
spx_df['clean_returns'] = spx_df['spx_returns'].drop(spx_df['spx_returns'].loc[spx_df['spx_returns']<11])

## ---(Wed Jun 14 14:44:03 2023)---
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx_df['spx_returns'].drop(spx_df['spx_returns'].loc[spx_df['spx_returns']<11])
spx_df['spx_returns'] = spx_df['spx_returns'].drop(spx_df.loc[spx_df['spx_returns']<11])
spx_df['spx_returns'].drop(spx_df.loc[spx_df['spx_returns']<11])
spx_df.loc[spx_df['spx_returns']<11]
spx_df['spx_returns'] = spx_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx_df['date'] = spx_df.quote_datetime.dt.date

spx_df['close'] = spx_df.close.replace(0, np.nan)
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
stand_minus = spx_df.loc[-5<spx_df['spx_returns']<11]
stand_minus = spx_df['spx_returns'].loc[spx_df['spx_returns']>-5]
stand_plus = spx_df['spx_returns'].loc[spx_df['spx_returns']<11]
spx_df['spx_returns'] - stand_minus
spx_df['spx_returns'].drop(stand_minus)
spx_df['spx_returns'] = spx_df['spx_returns'].drop(stand_minus)

## ---(Wed Jun 14 15:02:40 2023)---
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
stand_minus = spx_df.loc[(spx_df['spx_returns']>-5)&(spx_df['spx_returns']<11)]
spx_df['spx_returns'].describe()
spx_df['spx_returns'].std()
three_std = spx_std*3
spx_std = spx_df['spx_returns'].std() 
three_std = 'spx_std'*3
spx_std = spx_df['spx_returns'].std() 
three_std = spx_std*3
spx_df['spx_returns'].mean()
spx_mean = spx_df['spx_returns'].mean()
lower_m = spx_mean-three_std
higher_m = spx_mean+three_std

stand_minus = spx_df.loc[(spx_df['spx_returns']>lower_m)&(spx_df['spx_returns']<higher_m)]

stand_minus = spx_df['spx_returns'].loc[(spx_df['spx_returns']>lower_m)&(spx_df['spx_returns']<higher_m)]
stand_minus.plot()
stand_minus.plot.hist()
stand_minus.plot.hist(bins = 1000)
stand_minus = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]
stand_minus.plot.hist(bins = 1000)
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx2_df = spx_df
spx2_df['spx_returns'].loc[::15, :]
runcell(0, 'C:/Users/ywaterhouse/.spyder-py3/temp.py')
spx2_df['spx_returns'].loc[::15]
spec_thr = spx2_df['spx_returns'].loc[::15]
spec_thr.plot()
spx2_df = spx_df.copy()
spec_thr = spx2_df['spx_returns'].loc[::15]
spec_thr.plot()
spec_thr = spx2_df['spx_returns'].resample('15T')
spec_thr = spx2_df['spx_quote_datetime'].resample('15T')
spec_thr = spx2_df['quote_datetime'].resample('15T')
spec_thr = spx2_df.resample('15T')
spec_thr = spx2_df['unique_id'].resample('15T')
spx2_df['unique_id'].resample('15T')
spx2_df['quoate_datetime'].resample('15T')
spx2_df['quote_datetime'].resample('15T')
spx2_df['quote_datetime'].set_index.resample('15T')

spx2_df.set_index.resample('15T')
spx2_df['quote_datetime'].set_index
spx2_df['quote_datetime'].set_index()
spx2_df.set_index('quote_datetime')
spx2_df = spx_df.copy()
spx2_df.set_index('quote_datetime')
spx2_df.quote_datetime.resample('15T')
spx2_df['quote_datetime'] = spx2_df.set_index('quote_datetime')
spx2_df.quote_datetime.resample('15T')
spx2_df['quote_datetime'] = spx2_df.set_index('quote_datetime')
spx2_df['quote_datetime'] = spx2_df['quote_datetime'].set_index('quote_datetime')
spx2_df['quote_datetime'] = spx2_df.set_index('quote_datetime')
spx2_df.quote_datetime.resample('15T')
spx2_df.set_index('quote_datetime')
a = spx2_df.set_index('quote_datetime')
a = spx2_df.set_index('quote_datetime').resampe('15T')
a = spx2_df.set_index('quote_datetime').resampLe('15T')
a = spx2_df.set_index('quote_datetime')
a.resample()
a.resample('15min')
a.resample('15T')
spx2_df['time'] = spx_df.quote_datetime.dt.time
a = spx2_df.set_index('time')
a.resample('15T')
a = spx2_df.to_datetime('time')
a.resample('15T')
a = spx2_df.to_datetime('time'.index)
a = spx2_df.set_index('time')
a.resample('15T')
a = spx2_df.set_index('time')
spx2_df.resample('15T')
spx2_df.set_index('time').resample('15T')
spx2_df = spx_df.copy()
spx2_df['time'] = spx_df.quote_datetime.dt.time
a = spx2_df.datetime_index('Datetime')
a = spx2_df.set_index('Datetime')
spx2_df['Datetime'] = spx_df.quote_datetime.dt.time
a = spx2_df.set_index('Datetime')
b = a.resample('15T')
runfile('C:/Users/ywaterhouse/.spyder-py3/temp.py', wdir='C:/Users/ywaterhouse/.spyder-py3')
spx2_df.set_index('quote_datetime').resample('15T')
spx2_df.set_index(spx2_df['quote_datetime']).resample('15T')
#spx2_df['Datetime'] = spx_df.quote_datetime.dt.time
b = spx2_df.set_index(spx2_df['quote_datetime'])
c = a.resample('15T')
b = spx2_df.set_index(spx2_df['quote_datetime'])
c = a.resample('15min')
a = spx2_df.set_index(spx2_df['quote_datetime'])
c = a.resample('15min')
a = spx2_df.set_index(spx2_df['quote_datetime'])
c = a.resample(freq = '15min')
c = a.resample(freq = '15T')
a = spx2_df.set_index(spx2_df['quote_datetime'])
c = a.resample('15T')
a = spx2_df.set_index(spx2_df['quote_datetime'])
c = a.resample('15T').asfreq()

spx2_df['spx_returns'].plot.hist()
spx2_df['spx_returns'].plot.hist()
new15_ret = spx2_df['spx_returns'].loc[(spx2_df['spx_returns']>spx2_df['spx_returns'].mean()-spx2_df['spx_returns'].std()*3 )&(spx2_df['spx_returns']<spx2_df['spx_returns'].mean()+spx2_df['spx_returns'].std()*3 )]
new15_ret.plot.hist(bins = 1000)
a = spx2_df.set_index(spx2_df['quote_datetime'])
spx2_df['spx_returns'] = a.resample('15T').asfreq()
spx2_df.drop('spx_returns')
spx2_df.drop['spx_returns']
a = spx2_df.set_index(spx2_df['quote_datetime'])
spx2_df['spx2_returns'] = a.resample('15T').asfreq()
a = spx2_df.set_index(spx2_df['quote_datetime'])
spx2_df = a.resample('15T').asfreq()
runfile('//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn/temp.py', wdir='//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn')
spx2_df = spx_df.copy()
#a = spx2_df.set_index(spx2_df['quote_datetime'])
spx2_df = spx2_df.set_index(spx2_df['quote_datetime']).resample('15T').asfreq()
new15_ret.describe()
one_ret.describe()
d = np.log(spx2_df['open'])/np.log(spx2_df['close'])
d.plot.hist(bins=1000)
d = np.log(spx2_df['close'])/np.log(spx2_df['open'])
d.plot.hist(bins=1000)
spx2_df = spx_df.copy()
spx2_df = spx2_df.set_index(spx2_df['quote_datetime']).resample('15T')

#d = np.log(spx2_df['close'])/np.log(spx2_df['open'])
#d.plot.hist(bins=1000)
new15_ret = spx2_df['spx_returns'].loc[(spx2_df['spx_returns']>spx2_df['spx_returns'].mean()-spx2_df['spx_returns'].std()*3 )&(spx2_df['spx_returns']<spx2_df['spx_returns'].mean()+spx2_df['spx_returns'].std()*3 )]
new15_ret.describe()
new15_ret.plot.hist(bins = 1000)
spx2_df = spx_df.copy()
spx2_df = spx2_df.set_index(spx2_df['quote_datetime']).resample('15T')
spx2_df = spx_df.copy()
spx2_df = spx2_df.set_index(spx2_df['quote_datetime']).resample('15T').asfreq()
spx2_df.resample('15T').asfreq()
spx2_df.resample('15T')
spx2_df = spx_df.copy()
spx2_df = spx2_df.set_index(spx2_df['quote_datetime'])
spx2_df.resample('15T').last()
runfile('//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn/temp.py', wdir='//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn')
spx2_df = spx2_df.resample('15T').last()
new15_ret = spx2_df['spx_returns'].loc[(spx2_df['spx_returns']>spx2_df['spx_returns'].mean()-spx2_df['spx_returns'].std()*3 )&(spx2_df['spx_returns']<spx2_df['spx_returns'].mean()+spx2_df['spx_returns'].std()*3 )]
#new15_ret.describe()
new15_ret.plot.hist(bins = 1000)
runfile('//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn/temp.py', wdir='//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn')

## ---(Tue Jun 20 08:13:22 2023)---
runfile('//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn/temp.py', wdir='//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn')
one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]
one_ret.plot.hist(bins = 1000)
spx2_df = spx2_df.set_index(spx2_df['quote_datetime'])
spx2_df = spx2_df.resample('15T').last()
runfile('//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn/temp.py', wdir='//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn')
spx2_df['date'] = spx2_df.quote_datetime.dt.date

spx2_df['close'] = spx2_df.close.replace(0, np.nan)

spx2_df['spx_returns'] = spx2_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
two_ret = spx2_df['spx_returns'].loc[(spx2_df['spx_returns']>spx2_df['spx_returns'].mean()-spx2_df['spx_returns'].std()*3 )&(spx2_df['spx_returns']<spx2_df['spx_returns'].mean()+spx2_df['spx_returns'].std()*3 )]
two_ret.plot.hist(bins = 1000)
one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]
one_ret.plot.hist(bins = np.log2(one_ret.count())+1)
one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]
one_ret.plot.hist(bins = np.log2(one_ret.value_counts())+1)
#one_ret.describe()
opt_bins = np.log2(N973773)+1)
opt_bins = np.log2(973773)+1)
opt_bins = np.log2(973773)+1
one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]
one_ret.plot.hist(bins = opt_bins)
runfile('//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn/temp.py', wdir='//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn')
opt_bins = np.log2(one_ret.count())+1
one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]
one_ret.plot.hist(bins = opt_bins)
one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]
one_ret.plot.hist(opt_bins)
one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]
one_ret.plot.hist(bins = opt_bins)
opt_bins = int(np.log2(one_ret.count())+1)

one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]
one_ret.plot.hist(bins = opt_bins)
#one_ret.describe()
def opt_bins(returns):
    int(np.log2(returns.count())+1))

opt_bins = int(np.log2(one_ret.count())+1)

one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]

one_ret.plot.hist(bins = opt_bins(one_ret))
def opt_bins(returns):
    int(np.log2(returns.count())+1)

#opt_bins = int(np.log2(one_ret.count())+1)

one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]

one_ret.plot.hist(bins = opt_bins(one_ret))
def opt_bins(returns):
    bin_num = int(np.log2(returns.count())+1)
    return bin_num 
#opt_bins = int(np.log2(one_ret.count())+1)

one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]

one_ret.plot.hist(bins = opt_bins(one_ret))
#one_ret.describe()
spx2_df = spx2_df.set_index(spx2_df['quote_datetime'])
spx2_df = spx2_df.resample('15T').last()

spx2_df['date'] = spx2_df.quote_datetime.dt.date

spx2_df['close'] = spx2_df.close.replace(0, np.nan)

spx2_df['spx_returns'] = spx2_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
two_ret = spx2_df['spx_returns'].loc[(spx2_df['spx_returns']>spx2_df['spx_returns'].mean()-spx2_df['spx_returns'].std()*3 )&(spx2_df['spx_returns']<spx2_df['spx_returns'].mean()+spx2_df['spx_returns'].std()*3 )]
two_ret.plot.hist(bins = opt_bins(two_ret)))
spx2_df = spx2_df.set_index(spx2_df['quote_datetime'])
spx2_df = spx2_df.resample('15T').last()

spx2_df['date'] = spx2_df.quote_datetime.dt.date

spx2_df['close'] = spx2_df.close.replace(0, np.nan)

spx2_df['spx_returns'] = spx2_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
two_ret = spx2_df['spx_returns'].loc[(spx2_df['spx_returns']>spx2_df['spx_returns'].mean()-spx2_df['spx_returns'].std()*3 )&(spx2_df['spx_returns']<spx2_df['spx_returns'].mean()+spx2_df['spx_returns'].std()*3 )]
two_ret.plot.hist(bins = opt_bins(two_ret))
vix_df.set_index(vix_df['quote_datetime'])
vix_df.resample('15T').last()
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').last()
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime)
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').last()
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
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime)
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').last()
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
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime)
vix_df = vix_df.resample('15T').last()
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').last()
vix_df = vix_df.resample('15T').first()
vix_df.groupby(vix_df['expiration'])
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
#group by expiration first 
vix_df.groupby(vix_df['expiration'])
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime)
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').first()
vix_df = vix_df.resample('15T').last()
vix_df = vix_df.resample('15T')

vix_df.groupby(vix_df['expiration'])
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime)
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').first()
vix_df.groupby(vix_df['expiration'])
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime)
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').first()
runfile('//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn/temp.py', wdir='//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn')
vix_df['date'] = vix_df.quote_datetime.dt.date
vix_df['vix_returns'] = vix_df.groupby('date').apply(lamda x: np.log(x) - np.log(x.shift(1)))
vix_df['date'] = vix_df.quote_datetime.dt.date
vix_df['vix_returns'] = vix_df.groupby('date').apply(lambda x: np.log(x) - np.log(x.shift(1)))

vix_df.groupby(vix_df['expiration'])
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime)
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').first()
#calc returns in 15 min intervals - using front month so for trading in april, you are trading may exp
vix_df['date'] = vix_df.quote_datetime.dt.date
vix_df['vix_returns'] = vix_df.groupby('date').apply(lambda x: np.log(x) - np.log(x.shift(1)))
vix_df.groupby(vix_df['expiration'])
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime)
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').first()
#calc returns in 15 min intervals - using front month so for trading in april, you are trading may exp
vix_df['date'] = vix_df.quote_datetime.dt.date
vix_df['vix_returns'] = vix_df.groupby('date').apply(lambda x: np.log(x) - np.log(x.shift(1)))
vix_df['vix_returns'] = vix_df.groupby('date')['close'].apply(lambda x: np.log(x) - np.log(x.shift(1)))
vix_ret = vix_df['vix_returns'].loc[(vix_df['vix_returns']>vix_df['vix_returns'].mean()-vix_df['vix_returns'].std()*3 )&(vix_df['vix_returns']<vix_df['vix_returns'].mean()+vix_df['vix_returns'].std()*3 )]
vix_ret.plot.hist(bins = opt_bins(vix_ret))
!git add "file.py"
!git commit -m "My commit"
!git push origin master
!git push -u origin master
!git add "file.py"
runfile('//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn/temp.py', wdir='//lfp-chi.local/shared/Lakeview_Shared/Lakeview Investment Group/Yoselyn')
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
#group by expiration first 
vix_df.groupby(vix_df['expiration'])
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime)
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').first()



vix_df['date'] = vix_df.quote_datetime.dt.date
vix_df['vix_returns'] = vix_df.groupby('date')['close'].apply(lambda x: np.log(x) - np.log(x.shift(1)))


vix_ret = vix_df['vix_returns'].loc[(vix_df['vix_returns']>vix_df['vix_returns'].mean()-vix_df['vix_returns'].std()*3 )&(vix_df['vix_returns']<vix_df['vix_returns'].mean()+vix_df['vix_returns'].std()*3 )]
vix_ret.plot.hist(bins = opt_bins(vix_ret))
one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]

one_ret.plot.hist(bins = opt_bins(one_ret))
#one_ret.describe()
spx2_df['close'] = spx2_df.close.replace(0, np.nan)

spx2_df['spx_returns'] = spx2_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
two_ret = spx2_df['spx_returns'].loc[(spx2_df['spx_returns']>spx2_df['spx_returns'].mean()-spx2_df['spx_returns'].std()*3 )&(spx2_df['spx_returns']<spx2_df['spx_returns'].mean()+spx2_df['spx_returns'].std()*3 )]
two_ret.plot.hist(bins = opt_bins(two_ret))


#d = np.log(spx2_df['close'])/np.log(spx2_df['open'])

vix_df['date'] = vix_df.quote_datetime.dt.date
vix_df['vix_returns'] = vix_df.groupby('date')['close'].apply(lambda x: np.log(x) - np.log(x.shift(1)))


vix_ret = vix_df['vix_returns'].loc[(vix_df['vix_returns']>vix_df['vix_returns'].mean()-vix_df['vix_returns'].std()*3 )&(vix_df['vix_returns']<vix_df['vix_returns'].mean()+vix_df['vix_returns'].std()*3 )]
vix_ret.plot.hist(bins = opt_bins(vix_ret))
!git init
!git add "file.py"
!git commit -m "My commit"
!git push origin master