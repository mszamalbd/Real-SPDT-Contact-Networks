""""
This is reconstucting DDT networks from the SDT networks
This program generates statistics which users are present at which days in SDT network
Second part is generatnig which is still missing after reapting the host users

This is the input for 31
"""

import pandas as pd
import numpy as np
tday=32
pid=pd.Series()
uspd=pd.DataFrame(columns=['day','uid'])         ### traking the days user presence and corrsponding ids


for j in range(0,tday):    
    data=pd.read_csv("bnlink_3"+str(j)+".csv", names=['UsID','NbID','Hst','Hend','NbSt','Nbend'])  
    usid=pd.Series(data.NbID.unique())  
     
    nitem=pd.DataFrame(columns=['day','uid'])
    days=[j]*len(usid)                                      ## user present days
    nitem['uid']=usid                                       ## user list
    nitem['day']=pd.Series(days)
    uspd=uspd.append(nitem)                                  ## appneding every day statisics
    
    if(j>0):
        nid=usid[usid.isin(pid)==False]  
        pid=pid.append(nid, ignore_index=True)                  ## listing all users
    else:
        pid=usid
        
uspd=uspd.sort_values(['uid','day'], ascending=True)             ## This is sorting the userpresence statisics
uspd.to_csv("cruser_2.csv",header=False, index=False) 


uspd=pd.DataFrame(columns=['day','uid'])
for j in range(0,1):    
    data=pd.read_csv("bmlink_"+str(j)+".csv", names=['UsID','NbID','Hst','Hend','NbSt','Nbend'])     
    usid=pd.Series(data.NbID.unique()) 
    nid=pid[pid.isin(usid)==False]           ## which neighbor is not present , collected from the previous program
    
            
    nitem=pd.DataFrame(columns=['day','uid'])
    nitem['day']=j
    nitem['uid']=nid
    uspd=uspd.append(nitem)
    print(len(uspd),len(nitem),len(nid))
uspd=uspd.sort_values(['uid','day'], ascending=True)
uspd.to_csv("nruser_2.csv", header=False, index=False) 

print("Finish")