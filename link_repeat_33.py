
import pandas as pd
tday=32
data=pd.DataFrame()

for j in range(18,tday):  
    dat=pd.read_csv("bmlink_"+str(j)+".csv", names=['UsID','NbID','Hst','Hend','NbSt','Nbend'])
    data=data.append(dat)
    dat=pd.read_csv("badlink_"+str(j)+".csv", names=['UsID','NbID','Hst','Hend','NbSt','Nbend']) 
    data=data.append(dat)
    data.to_csv("bclink_"+str(j)+".csv",header=False, index=False) 
    print(len(data))
    data=pd.DataFrame()