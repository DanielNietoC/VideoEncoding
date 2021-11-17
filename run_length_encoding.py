#Credit:  https://www.geeksforgeeks.org/run-length-encoding-python/

from collections import OrderedDict


def runLengthEncoding(input):
    # Generate ordered dictionary of all lower
    # case alphabets, its output will be
    # dict = {'first_character':0, 'second_char':0, 'third_char':0, etc}
    dict = OrderedDict.fromkeys(input, 0)

    # Now iterate through input string to calculate
    # frequency of each character, its output will be
    # dict = {'first_char':n_times,'second_char':m_times, etc}
    for ch in input:
        dict[ch] += 1

    # now iterate through dictionary to make
    # output string from (key,value) pairs
    output = ''
    for key, value in dict.items():
        output = output + key + str(value)
    return output


