execfile('Qscan.230520.py')
this_file_path = sys._getframe().f_code.co_filename

'''File path'''
# Data in path\cooldown_name\data, logs and summaries in path\cooldown_name\
datapath=r'C:\Users\example\Desktop\data'
filename='dat_test'

channels_to_read = [# (instrument,parameter,label or list of labels)
                    # ('smu1','val','I_leak (A)'), 
                    # ('smu2','val','R (ohm)'), 
                    ('lockin1','val_XY',['I_x (A)', 'I_y (A)']),
                    ('lockin2','val_XY',['Vxx_x (V)','Vxx_y (V)']),
                    # ('lockin3','XY',['Vxy_x (V)','Vxy_y (V)']),
                    # ('ppms','temperature','T (K)'),
                    ]

channels_to_set = {# name: [unit,instrument,parameter] or [unit, function]
                    'vg':['V','smu1','source_level'],
                    'T':['K','ppms','temperature'],
                    'B':['T','ppms','field'],
                  }

g = get_set()
'''If you need to insert customized columns'''
def get_prcss_new(val):
    p_val = [time()-g.t0, time()]
    return p_val
g.prcss_labels = ['t (s)', 'timestamp (s)']
g.get_prcss = get_prcss_new

e = easy_scan()

'''Other settings'''
# Lockin:(0,10*tau,1.5tau-10tau) DC:(0,1,0.1)
delay0,delay1,delay2 = (0,1,0)

'''measure'''

# qt.get_instruments()['smu1'].set_switch_source_readback(0)
# qt.get_instruments()['smu1'].set_switch_source_autodelay(0)
# qt.get_instruments()['smu1'].set_switch_autozero(0)
# qt.get_instruments()['ppms'].get_temp()

# e.scan: channels, start, end, number of steps ( = point number -1), ...
# e.set: channel, value

###############

# e.set('vg',0)

# delay0,delay1,delay2 = (0,1,1)
e.scan([''],[0],[1],100000)# nothing is scanned, repeat reading

# e.scan(['vg'],[-6.8],[-7],300,bwd = True)
# qt.msleep(60)


# higher-dimensional scan
# e.scan([''],[0],[1],180,['vg'],[-8.7],[-8.3],100)

# scan multiple channels together
# e.scan(['Vg1(mV)_g2','Vg2(mV)'],[0,0],[100,-100],200)

# scan without stopping at setpoints
# remember to add magnet.field to channels_to_read
# qt.get_instruments()['magnet'].set_field(35, wait=False)
# e.scan([''],[0],[1],36000*1)


'''more scans'''
# Excute file "poscan_more.py" if exist, then delete it.
e.more_scan('poscan_more.py')