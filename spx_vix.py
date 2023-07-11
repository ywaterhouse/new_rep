import pandas as pd 
import datetime as dt
import numpy as np
import matplotlib.pyplot as plot
import statsmodels.api as sm

def df_resample(df,quote_datetime): 
    df = (df.set_index(quote_datetime,drop = True) 
          .resample('15T').first())
    return df 
    
def beta_linear(spx_returns,vix_returns):
    independent_variable = spx_returns
    dependent_variable = vix_returns 
    independent_variable = sm.add_constant(independent_variable) 
    mod = sm.OLS(dependent_variable,independent_variable).fit() 
    return mod 

def beta_covariance(spx_returns,vix_returns):
    independent_variable = spx_returns
    dependent_variable = vix_returns
    betas = np.cov(dependent_variable,independent_variable)[0][1]/np.var(independent_variable)
    return betas

def remove_outliers(returns):
    mean = returns.mean()
    three_standard_dev = returns.std()*3
    clean_spx_returns = (returns
                         .loc[returns
                              .between(mean - three_standard_dev, mean + three_standard_dev)])
    return clean_spx_returns

def main():
    spx_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\spx_index.csv',parse_dates = ['quote_datetime']) 
    vix_df = pd.read_csv(r'\\lfp-chi.local\shared\Lakeview_Shared\Lakeview Investment Group\Yoselyn\VIX_Futures_Minutely.csv',parse_dates = ['quote_datetime'],encoding_errors = "replace")

    """SPX_DF""" 
    spx_df['quote_datetime'] = (spx_df.quote_datetime
                                .dt.tz_localize('US/Eastern')
                                .dt.tz_convert('US/Central')
                                .dt.tz_localize(None))
     
    spx_df['date'] = spx_df.quote_datetime.dt.date
    spx_df['close'] = spx_df.close.replace(0, np.nan) 
    
    spx_df['spx_returns'] = (spx_df.groupby('date').close
                             .apply(lambda x : np.log(x) - np.log(x.shift(1)))) 
    
    spx_returns = remove_outliers(spx_df.spx_returns) 
    spx_returns.plot.hist(bins = int(np.log2(spx_returns.count())+1))
    
    """SPX_15min_DF""" 
    
    spx_15min_df = df_resample(spx_df,'quote_datetime') 
    spx_15min_df['close'] = spx_15min_df.close.replace(0, np.nan) 
    
    spx_15min_df['spx_returns'] = (spx_15min_df.groupby('date').close
                                   .apply(lambda x : np.log(x) - np.log(x.shift(1)))) 
    
    spx_15min_returns = remove_outliers(spx_15min_df.spx_returns)
    spx_15min_returns.plot.hist(bins = int(np.log2(spx_15min_returns.count())+1))
    
    """VIX_DF""" 
    vix_df = (df_resample(vix_df,'quote_datetime')
              .dropna(how = 'all') 
              .sort_values(by=['trade_date', 'expiration'], ascending = True))
    
    unique_vix_expirations = (pd.Series(vix_df.expiration.unique())
                              .sort_values(ascending = True))
    
    vix_df['expiration_month'] = np.searchsorted(unique_vix_expirations,vix_df.expiration,side= 'right') - np.searchsorted(unique_vix_expirations,vix_df.trade_date, side = 'right')  
    
    vix_front_month = vix_df.loc[vix_df.expiration_month == 1] 
    vix_front_month['vix_returns'] = np.log(vix_front_month.close) - np.log(vix_front_month.close.shift(1)) 
    
    vix_returns = remove_outliers(vix_front_month.vix_returns)
    vix_returns.plot.hist(bins = int(np.log2(vix_returns.count())+1))
    
    """Calc Beta Linear Regression"""
    merge_df = (spx_15min_df.merge(vix_front_month, on= 'quote_datetime')
                .dropna(subset = ['vix_returns'])
                .dropna(subset = ['spx_returns']))
    
    model = beta_linear(merge_df['spx_returns'],merge_df['vix_returns'])
     
    """Calc beta using Covariance"""
    cov_calc = beta_covariance(merge_df['spx_returns'],merge_df['vix_returns']) 

if __name__ == "__main__": 
    main()