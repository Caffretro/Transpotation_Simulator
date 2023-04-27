# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:20:13 2018

@author: kejintao

input information:
1. demand patterns (on minutes)
2. demand databases
3. drivers' working schedule (online/offline time)

** All the inputs are obtained from env, thus we do not need to alter parameters here
"""

import numpy as np
import pandas as pd
from copy import deepcopy
import random
from config import *
from path import *
import pickle
import sys

class SimulatorPattern(object):
    def __init__(self, **kwargs):
        # read parameters
        self.simulator_mode = kwargs.pop('simulator_mode', 'simulator_mode')
        self.request_file_name = kwargs['request_file_name']
        self.driver_file_name = kwargs['driver_file_name']
        self.experiment_mode = kwargs['experiment_mode']

        if self.simulator_mode == 'toy_mode':
            self.request_all = pickle.load(open(data_path + self.request_file_name + '.pickle', 'rb'))
            # print(self.request_all)
            self.driver_info = pickle.load(open(load_path + self.driver_file_name + '.pickle', 'rb'))
            # drivers are grouped by driver_id, sample drivers to keep all their corresponding rows
            all_drivers = pd.unique(self.driver_info['driver_id'])
            random.seed(42)
            drivers_to_keep = random.sample(list(all_drivers), env_params['driver_num'])
            if self.experiment_mode == 'train':
                self.driver_info = self.driver_info[self.driver_info['driver_id'].isin(drivers_to_keep)]
            else:
                train_set = self.driver_info[self.driver_info['driver_id'].isin(drivers_to_keep)]
                self.driver_info = self.driver_info.loc[~self.driver_info.index.isin(train_set.index)]
            # self.driver_info = self.driver_info.sample(n=env_params['driver_num'])
            # print(self.driver_info)