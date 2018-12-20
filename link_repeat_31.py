""""
Updated file on 21/06/2018
This algorithm fill up the missing days
It is providing input to the next algorithm

"""

import pandas as pd
import numpy as np


file=open("crepday.csv",'w')                      ## records of filling up the missing day

user=pd.read_csv("nruser_2.csv",names=['day','uid'])             ## which day is not filled up yet
dat=user.sort_values(['uid','day'], ascending=True)

user=pd.read_csv("cruser_2.csv",names=['day','uid'])
data=user.sort_values(['uid','day'], ascending=True)       ## which day is available day

nid=dat.uid.unique()
print(len(nid),len(dat))

track=1000
for i in range(0,len(nid)):         ## work through every nodes
    sid=nid[i]
    updts=data[data['uid']==sid]  
    avlst=list(updts['day'])
    
    updto=dat[dat['uid']==sid]  
    mlst=list(updto['day'])
    
    for j in range(0,len(mlst)):
        k=int(mlst[j])
        temp=np.random.randint(0,len(avlst))
        d=int(avlst[temp])
        file.write("{0} {1} {2} {3} {4} {5}".format(sid,",",d,",",k,"\n"))
    if(i>track):
        print(track)
        track=track+1000
file.close()
print("Finish")