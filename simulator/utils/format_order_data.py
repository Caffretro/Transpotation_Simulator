import pickle
import numpy as np
import pandas as pd
import random

def format_hongkong_order_time():
    DATE_LIST = ['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'day8']
    new_dict = {}
    data = pd.read_pickle("../input/hongkong_date_based_order_test.pickle")
    for idx, day in enumerate(data.keys()):
        for second in data[day].keys():
            if day not in new_dict.keys():
                new_dict[day] = {second % 86400: data[day][second]}
                new_dict[day][second % 86400][0][8] %= 86400
            else:
                new_dict[day].update({second % 86400: data[day][second]})
                new_dict[day][second % 86400][0][8] %= 86400

    test_save_data = pickle.dump(new_dict, open("../input/hongkong_date_based_order.pickle", 'wb'))

def check_formatted_data():
    data = pd.read_pickle("../input/April 25/hongkong_processed_order_April25.pickle")
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    # for key in data['day4'].keys():
    #     print(key, ':', data['day4'][key])
        for key in sorted(data.keys()):
            print(data[key])
        
def check_driver_data():
    data = pd.read_pickle('../input/April 25/hongkong_driver_info_April25.pickle')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    # minimum = 100000000
    # for driver in data['end_time']:
    #     if driver < minimum:
    #         minimum = driver
    # print(minimum)
        print(data)

def shift_driver_working_time():
    data = pickle.load('../input/hongkong_driver_info.pickle', 'rb')
    data['start_time'] -= 28800
    data['end_time'] -= 28800
    test_save_data = pickle.dump(data, open("../input/hongkong_driver_info_time_forwarded.pickle", 'wb'))

def sample_drivers(sample_num):
    data = pd.read_pickle('../input/April 25/hongkong_driver_info_April25_122348.pickle')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        driver_num = pd.unique(data['driver_id'])
        drivers_to_keep = random.sample(list(driver_num), sample_num)
    
        print(drivers_to_keep)

if __name__ == '__main__':
    # format_hongkong_order_time()
    # check_formatted_data()
    # check_driver_data()
    # shift_driver_working_time()
    sample_drivers(3000)