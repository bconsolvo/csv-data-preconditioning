#!/bin/env python3

###---usage: cuts.py <name.csv>

import os, sys
import datetime as dt
import pandas as pd
import numpy as np

#INPUTS
age=30 # minimum age of person
distance=400 # distance from work to home in km
pt_prefix = 'name' #prefix that will be used to name the output


#Calculations and output
conf_df = pd.read_csv(sys.argv[1])
id_no = conf_df['CertID'].iloc[0] # Fetches the CertID number from the CertID column, only if all CertID rows are the same
age_dist_cut = conf_df.loc[(conf_df['AGE'] > age) & (conf_df['DIST'] > distance)]
age_dist_cut.to_csv(pt_prefix + '_agedistcut' + str(id_no) +'.csv', index = False)


