"""
program: Hobbies.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 26 2021
"""

import sys

def get_data(file):
    """ open file and get data """
    with open(file, 'r') as f_hobbies:
        content = f_hobbies.readlines()
        total_list = [i.strip().split(' ') for i in content]

    return total_list


def get_hobbies(data):
    """ get the hobbies from data and delete the duplex hobbies """
    person_hobbies = [person_info[1] for person_info in data]
    hobbies_list = []
    for i in person_hobbies:
        if ',' in i:
            for hobby in i.split(','):
                hobbies_list.append(hobby)
        else:
            hobbies_list.append(hobby)

    return set(hobbies_list)


def get_count(data, hobbies_list):
    """ count each person's hobbies and make it as a dictionary """
    count_hobby = 0
    dict_hobbies = {}
    for hobby in hobbies_list:
        for i in data:
            if hobby in i[1]:
                count_hobby += 1
        dict_hobbies[hobby] = count_hobby
        count_hobby = 0
    
    return dict_hobbies


def main():
    """ main function """
    file_name = 'Hobbies.txt'
    data = get_data(file_name)
    hobbies_list = list(get_hobbies(data))
    dict_hobbies = get_count(data, hobbies_list)
    for hobby, count in dict_hobbies.items():
        print(f'{hobby:15} {count}')


main()