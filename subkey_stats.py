#!/usr/bin/env python

from ktantan import k_a_index, k_b_index

if __name__ == '__main__':
    last  = [None] * 80 # last round the bit used
    for i in range(254):
        last[k_a_index[i]] = i
        last[k_b_index[i]] = i

    first = [None] * 80 # first round the bit used
    for i in range(253, -1, -1):
        first[k_a_index[i]] = i
        first[k_b_index[i]] = i

    first_list = zip(range(254), first)
    last_list = zip(range(254), last)

    first_list.sort(key = lambda tup: tup[1], reverse = True)
    last_list.sort(key = lambda tup: tup[1])

    print first_list[:9]
    print last_list[:9]

