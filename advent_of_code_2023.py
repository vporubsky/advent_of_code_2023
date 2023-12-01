"""
Developer Name: Veronica Porubsky
Developer ORCID: 0000-0001-7216-3368
Developer GitHub Username: vporubsky
Developer Email: veronica.porubsky@gmail.com

File Creation Date: 12/1/2023

Description: library containing the functions to solve each Advent of Code challenge
"""
# Imports
import re

#%% Functions
def get_data(filename):
    """
    Parse the input file, splitting each line into a distinct string.

    :param filename:
    :return:
    """
    with open(filename, 'r') as file:
        text = file.read()
    file.close()
    return text.split('\n')


def day_1(filename, parse_words=True):
    """
    Determine the calibration value for each line of the input dataset (filename), where each
    calibration value is found by combining the first digit and last digit in the line to form
    a single two-digit number. Return the sum of all calibration values.

    If parse_words is set to True, then all numbers which are spelled out with letters
    ('one', 'two', etc. through 'nine) should first be converted to valid digits in the line to be used
    when determining the  calibration values and overal sum.

    :param filename:
    :param parse_words:
    :return: int
    """
    data = get_data(filename=filename)

    nums_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    # To parse strings with numbers written as words:
    if parse_words:
        store_strings = []
        for string in data:
            nums = []
            num_locs = []
            for key in list(nums_dict.keys()):
                if key in string:
                    res = [i.start() for i in re.finditer(key, string)]
                    for idx in res:
                        nums.append(nums_dict[key])
                        num_locs.append(idx)
            if num_locs:
                locs, nums = zip(*sorted(zip(num_locs, nums)))

                if len(locs) > 1:
                    string = string[0: locs[0]] + nums[0] + string[locs[0] + 1: locs[-1]] + nums[-1] + string[locs[-1] + 1:]
                else:
                    string = string[0: locs[0]] + nums[0] + string[locs[0] + 1:]

            store_strings.append(string)
        data = store_strings

    # To select the first and last numeral in each string and sum over all selected numbers
    sum = 0
    for string in data:
        find_nums = re.findall(r'\d+', string)
        combine_nums_to_str = "".join(find_nums)

        if len(combine_nums_to_str) > 1:
            first_last_num = combine_nums_to_str[0] + combine_nums_to_str[-1]
        else:
            first_last_num = combine_nums_to_str + combine_nums_to_str

        first_last_num = int(first_last_num)
        sum += first_last_num

    return sum

