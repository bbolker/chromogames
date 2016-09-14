import EvoPro2_4
import importlib
reload(EvoPro2_4)
import matplotlib.pyplot as plt 
clr=['blue','red','black','green','yellow','cyan','orange','magenta'] 
for a_val in range(-6,1):
    x=EvoPro2_4.runsim(roundnum=10000000,colour_init=(0,10),a_range_init=(a_val,a_val),b_range_init=(0,0),result_type='timeseries',rpt_freq=1000,seed=2)
    x1=str(a_val) 
    plt.plot(x[:,0],label='mean A ='+x1, color=clr[a_val])
x=EvoPro2_4.runsim(roundnum=10000000,colour_init=(0,10),a_range_init=(-0.5,-0.5),b_range_init=(0,0),result_type='timeseries',rpt_freq=1000,seed=2)
plt.plot(x[:,0],label='mean A =-0.5', color=clr[1])
x=EvoPro2_4.runsim(roundnum=10000000,colour_init=(0,10),a_range_init=(-0.1,-0.1),b_range_init=(0,0),result_type='timeseries',rpt_freq=1000,seed=2)
plt.plot(x[:,0],label='mean A =-0.1', color=clr[0])
plt.title('b=0 colour=0,10 seed=2 mutations=0.01 nsize=1 chicken')  
plt.legend(bbox_to_anchor=(-0.03,0.5),prop={'size':11})
plt.show() 
    
