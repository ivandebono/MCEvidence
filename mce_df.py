import pandas as pd
import os

"""
Converts MCE output to a dataframe containing all models and all data sets.

"""

def listofcsv(folder):

    csvlist=[]
    for root, dirs, files in os.walk(folder+'/Allchains/csv'):
        for file in files:
            if file.endswith('.csv'):
                csvlist.append(folder+'/Allchains/csv/'+file)
            
    print('Folder contains ', len(csvlist),' data sets')
    
    return csvlist


 
def csv2df(csvlist):
    bigdf=pd.DataFrame({'Data':[],'Model':[], 'AllChains':[], 'delta_lnE_k1':[], 'PriorVol':[], 'ndim':[], 'N_read':[],
   'N_used':[]})
    newcolumns=['Data','Model', 'AllChains', 'delta_lnE_k1', 'PriorVol', 'ndim', 'N_read',
              'N_used']
    for file in csvlist:
        df=pd.read_csv(file,names=['Model', 'AllChains', 'delta_lnE_k1', 'PriorVol', 'ndim', 'N_read',
                            'N_used'],skiprows=1)
        df['Data']=((file.split('/')[-1]).replace('mce_','')).replace('.csv','')
    

        bigdf=bigdf.append(df,ignore_index=True,sort=False)
    
    bigdf=bigdf[newcolumns]

    return bigdf

    
def mce_df(folder,pickle=False):

    csvlist=listofcsv(folder)

    bigdf=csv2df(csvlist)
    
    if pickle is True: bigdf.to_pickle(folder+'/mce_fullgrid.pkl')
    
    return bigdf

def bayes2df(file):

        #Make a dataframe with just ln(B) for the models

    bayesdf=pd.read_pickle(file)

    return bayesdf