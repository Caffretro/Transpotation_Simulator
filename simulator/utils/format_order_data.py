import pickle
import numpy as np
import pandas as pd

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
    data = pd.read_pickle("../input/hongkong_date_based_order.pickle")
    # for key in data['day4'].keys():
    #     print(key, ':', data['day4'][key])
    print(data['day2'][85163+86400])
        
if __name__ == '__main__':
    # format_hongkong_order_time()
    check_formatted_data()