"""
This is a project that takes data from vix futures trades (date) and spx trades (dates), cleans, transforms, and filters
to calculate returns for each security, and calculates and plots beta. 
"""

import pandas as pd 
import datetime as dt
import numpy as np
import matplotlib.pyplot as plot
import statsmodels.api as sm

#read in spx and vix files 
spx_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv') 
vix_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\VIX_Futures_Minutely.csv')

def clean_df(df,index,index1,index2): 
    df[index1] = df[index].dt.date 
    df[index2] = df[index2].replace(0, np.nan) 
    
def df_resample(df,index): 
    df = df.set_index(df[index]) 
    df = df.resample('15T').first()
    return df 
    
def remove_outliers(df,index):
    ret_df = df[index].loc[(df[index]>df[index].mean()-df[index].std()*3)&(df[index]<df[index].mean()+df[index].std()*3)] 
    return ret_df

def beta_linear(index,index1):
    X=merge_df[index] 
    Y=merge_df[index1] 
    plot.scatter(X,Y)
    X = sm.add_constant(X) 
    mod = sm.OLS(Y,X).fit() 
    return mod 

def beta_covariance(index,index1):
    D=merge_df[index] 
    E=merge_df[index1] 
    betas = np.cov(E,D)[0][1]/np.var(D)
    return betas
    
"""SPX_DF""" 
#change type to then make time zone the same as vix  
spx_df['quote_datetime'] = pd.to_datetime(spx_df.quote_datetime) 
spx_df['quote_datetime'] = spx_df.quote_datetime.dt.tz_localize('US/Eastern').dt.tz_convert('US/Central').dt.tz_localize(None) 
spx15_df = spx_df.copy()   
#add date and remove nan values to successfully calculate returns, calc returns, and remove outliers 
clean_df(spx_df,'quote_datetime','date','close')
spx_df['spx_returns'] = spx_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1))) 
spx1_ret = remove_outliers(spx_df,'spx_returns')  

"""SPX2_DF""" 
#set index to datetime to resample to 15 minute intervals 
spx15_df = df_resample(spx15_df,'quote_datetime') 
#add date and remove nan values to successfully calculate returns, calc returns, and remove outliers 
clean_df(spx15_df,'quote_datetime','date','close')
spx15_df['spx_returns'] = spx15_df.groupby('date')['close'].apply(lambda x : np.log(x) - np.log(x.shift(1)))
spx15_ret = remove_outliers(spx15_df,'spx_returns')

"""VIX_DF""" 
#making into 15 min interval
vix_df["quote_datetime"] = pd.to_datetime(vix_df.quote_datetime) 
#set index to datetime to resample to 15 minute intervals for fair return comparison
vix_df = df_resample(vix_df,'quote_datetime') 
#drop any nans to successfully sort vix_df 
vix_df = vix_df.dropna(how = 'all') 
vix_df = vix_df.sort_values(by=['trade_date', 'expiration'], ascending = True) 
#make unique expiration series sorted in order to sort trade_dates by
vix_exps = vix_df.expiration.unique()
vix_exps = np.sort(vix_exps) 
#sort each rows expiration into the unique expirations to see the actual exiprations of each row
#sort trade_dates into unique expiration to get each rows correct front month
#find difference to see what expiration month each trade is trading and add 1 to correctly show the month
vix_df['exp_month'] = np.searchsorted(vix_exps,vix_df.expiration) - np.searchsorted(vix_exps,vix_df.trade_date) +1 
#locate on front months, calculate returns, and remove outliers to later correctly calcuate beta
vix_df = vix_df.loc[vix_df.exp_month == 1] 
vix_df['vix_returns'] = np.log(vix_df.close) - np.log(vix_df.close.shift(1)) 
vix_ret = remove_outliers(vix_df,'vix_returns')

"""Calc Beta Linear Regression"""
#get rid of duplicate quote_dateime to merge then merge
spx15_df = spx15_df.drop('quote_datetime',axis=1) 
vix_df = vix_df.drop('quote_datetime',axis=1) 
merge_df = spx15_df.merge(vix_df, right_on= 'quote_datetime',left_on = 'quote_datetime') 
#remove nan values to successfully make scatter plot then plot 
merge_df = merge_df.dropna(subset = ['vix_returns']) 
merge_df = merge_df.dropna(subset = ['spx_returns']) 
model  = beta_linear('spx_returns','vix_returns')

"""Calc beta using Covariance"""
cov_calc = beta_covariance('spx_returns','vix_returns')




