""""
This is reconstructing the links according to the file of 31
This is developed on 21/06/18

"""

import pandas as pd
tday=32
day=86400

dayrp=pd.read_csv("crepday.csv",names=['uid','rday','mday'])
print(len(dayrp))
usid=dayrp.uid.unique()
print(len(usid))

for j in range(0,tday):   
    updts=dayrp[dayrp['mday']==j]                        # reconstructing the jth day, missing day
    file=open("badlink_"+str(j)+".csv",'w')              # creating reconstructed links, fillup the missing days

    for k in range(0,32):                                # from where it is comming, which days kth
        if(j==k):
            continue
        adtm=(j-k)*day
        updt=updts[updts['rday']==k]                     ## day k taking the updates
        dat=pd.read_csv("bnlink_3"+str(k)+".csv", names=['UsID','NbID','Hst','Hend','NbSt','Nbend']) 
        
        for i in range(0,len(updt)):                    ## for each users
            temp=updt.iloc[i]
            sid=int(temp.uid)             
            rpup=dat[dat['NbID']==sid]             ## taking from j day
            for n in range(0,len(rpup)):
                temp=rpup.iloc[n]
                hst=float(temp.Hst)+adtm
                hend=float(temp.Hend)+adtm
                nbst=float(temp.NbSt)+adtm
                nbend=float(temp.Nbend)+adtm
                file.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11}".format(temp.UsID,",",temp.NbID,",",hst,",",hend,",",nbst,",",nbend,"\n"))
                
        print("Finish day",j,k)
    file.close()
    print("Finish day",j)
    
print("Finish")