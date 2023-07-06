import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plot
import statsmodels.api as sm

#read in spx and vix files
spx_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv')
vix_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\VIX_Futures_Minutely.csv')
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

#plot of one minute returns
def opt_bins(returns):
    bin_num = int(np.log2(returns.count())+1)
    return bin_num 
#opt_bins = int(np.log2(one_ret.count())+1)

one_ret = spx_df['spx_returns'].loc[(spx_df['spx_returns']>spx_df['spx_returns'].mean()-spx_df['spx_returns'].std()*3 )&(spx_df['spx_returns']<spx_df['spx_returns'].mean()+spx_df['spx_returns'].std()*3 )]

one_ret.plot.hist(bins = opt_bins(one_ret))


#calc spx 15 minute returns 
spx2_df = spx2_df.set_index(spx2_df['quote_datetime'])
spx2_df = spx2_df.resample('15T').first()

spx2_df['date'] = spx2_df.quote_datetime.dt.date

spx2_df['close'] = spx2_df.close.replace(0, np.nan)

spx2_df['spx_returns'] = spx2_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
two_ret = spx2_df['spx_returns'].loc[(spx2_df['spx_returns']>spx2_df['spx_returns'].mean()-spx2_df['spx_returns'].std()*3 )&(spx2_df['spx_returns']<spx2_df['spx_returns'].mean()+spx2_df['spx_returns'].std()*3 )]
two_ret.plot.hist(bins = opt_bins(two_ret))

"""ALL VIX"""
#making into 15 min interval 
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime) 
vix_df = vix_df.set_index(vix_df['quote_datetime'])
vix_df = vix_df.resample('15T').first()
vix_df = vix_df.dropna(how = 'all')
vix_df = vix_df.sort_values(by=['trade_date', 'expiration'], ascending = True)

vix_exps = vix_df.expiration.unique()
vix_exps = np.sort(vix_exps)     
vix_df['exp_month'] = np.searchsorted(vix_exps,vix_df.expiration) - np.searchsorted(vix_exps,vix_df.trade_date) +1

vix_df = vix_df.loc[vix_df.exp_month == 1] 
vix_df['vix_returns'] = np.log(vix_df.close) - np.log(vix_df.close.shift(1))  


vix_ret = vix_df['vix_returns'].loc[(vix_df['vix_returns']>vix_df['vix_returns'].mean()-vix_df['vix_returns'].std()*3 )&(vix_df['vix_returns']<vix_df['vix_returns'].mean()+vix_df['vix_returns'].std()*3 )]
vix_ret.plot.hist(bins = opt_bins(vix_ret))


spx2_df = spx2_df.drop('quote_datetime',axis =1)
vix_df = vix_df.drop('quote_datetime',axis =1)

merge_df = spx2_df.merge(vix_df, right_on= 'quote_datetime',left_on = 'quote_datetime')

merge_df = merge_df.dropna(subset = ['vix_returns'])
merge_df = merge_df.dropna(subset = ['spx_returns'])

X=merge_df['spx_returns']
Y=merge_df['vix_returns']

plot.scatter(X,Y)  

X = sm.add_constant(X)

mod = sm.OLS(Y,X).fit()

D=merge_df['spx_returns']
E=merge_df['vix_returns']

betas = np.cov(E,D)[0][1]/np.var(D) 





