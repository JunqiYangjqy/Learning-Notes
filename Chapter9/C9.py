# -*- coding: utf-8 -*-
"""
@author: Jarry
"""
#Chapter 9 - Visualisation

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data=np.arange(10)

plt.plot(data)
plt.show()

#Create a fig with subplots. The last parametre in add_subplot identicate the subplot order
fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)
plt.plot(np.random.randn(50).cumsum(),'k--')

_ = ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30)+ 3*np.random.randn(30))
ax3.bar(np.arange(8),np.random.uniform(0.5,1.0,8),alpha=0.9, width = 0.35, facecolor = 'lightskyblue', edgecolor = 'white', label='one', lw=1)

fig

# subplots_adjust() is used to adjust the margin between subplots
# subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=None,hspace=None)

plt.plot(np.random.randn(30).cumsum(),color='g',marker='o')

pltdata=np.random.randn(30).cumsum()
plt.plot(pltdata,'g--',label='Default')
plt.plot(pltdata,'k-',drawstyle='steps-post',label='steps-post')
plt.legend(loc='best')


fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())
#Set the labels
#set_xticks is used to set the scale position within the data range
xticks=ax.set_xticks([0,250,500,750,1000])
xlabels=ax.set_xticklabels(['one','two','three','four','five'],rotation=25,fontsize='small')
ax.set_title('Matplotlib Learning')
ax.set_xlabel('Stages')
fig

#Add Legend of a picture
fig = plt.figure();
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum(),'k',label='One')
ax.plot(np.random.randn(1000).cumsum(),'k--',label='Two')
ax.plot(np.random.randn(1000).cumsum(),'k.',label='Three')
#use ax.legend()or plt.legend() to generate legend
ax.legend(loc='best') #loc is the location parametre, 'best' is a good option

#Annotation and subplot 'modification'
#ax.annotate() can draw labels at specified x and y coordinates
from datetime import datetime
fig=plt.figure()
ax = fig.add_subplot(1,1,1)

data = pd.read_csv('D:\GitHub\Repos\Learning-Notes\Datasets\examples\spx.csv',index_col=0,parse_dates=True)
spx= data['SPX']

spx.plot(ax=ax,style='g-')

crisis_data = [
        (datetime(2007,10,11),'Peak of bull Marker'),
        (datetime(2008,3,12),'Bear Stearns Fails'),
        (datetime(2008,9,15),'Lehman Bankruptcy')
        ]

for date,label in crisis_data:
    ax.annotate(label,xy=(date,spx.asof(date)+75),
                xytext=(date,spx.asof(date)+225),
                arrowprops=dict(facecolor='black',headwidth=4,headlength=4,width=2),
                horizontalalignment='left',verticalalignment='top')
    
#enlarge 2007 - 2010
ax.set_xlim(['1/1/2007',''1/1/2011])
ax.set_ylim([600,1800])
ax.set_title('Important dates in 2008-2009')

