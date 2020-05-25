"""degree of anarray, return the shortest length of the subarrray has same degree with input array."""

from collections import defaultdict

def degree_array(nums):

    records = defaultdict(list)
    degree = len(nums) # largest degree is all numbers are same
    result = 0

    for i, n in enumerate(nums):
        if n not in records:
            records[n].append(i)  # record the start index of element
            records[n].append(1) # record the frequency
        records[n][-1] += 1

        if degree < records[n][-1]:
            degree = records[n][-1]
            result = i - records[n][0] +1   # found a new degree update degree and the length of degree_array

        if degree == records[n][-1]:
            result = min(result, i-records[n][0]+1)  # more than one degree elements choose the shortest

    return result

degree_array([1,2,2,3,1,4,2])
