# https://www.hackerrank.com/challenges/arrays-ds/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def reverseArray(a):
    # Write your code here
    end = len(a) - 1
    arr = []
    for i in range(end, -1, -1):
        arr.append(a[i])
        
    return arr
