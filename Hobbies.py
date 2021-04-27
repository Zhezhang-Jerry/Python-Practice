"""
program: Hobbies.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 26 2021
"""

def get_hobbies(file):
    with open(file, 'r') as f_hobbies:
        content = f_hobbies.readlines()




def main():
    file_name = 'Hobbies.txt'
    hobbies_list = get_hobbies(file_name)
    # hobbies_count = get_count(hobbies_list)



main()