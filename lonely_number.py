#program to find lonely number in the array
print("input numbers in order")
x = raw_input().split(' ')
dict1 = {}
for i in x:
    j = dict1.get(i)
    if j:
        dict1[i] +=1
    else:
        dict1[i] = 1
for i in x:
    if (dict1[i] ==1):
        print i,
#O(2n) time complexity
#O(n+m) space complexity
                      
