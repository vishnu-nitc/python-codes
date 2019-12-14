#program for intersection'
a = [2,16,8,9]
b = [14,15,2,20]
dict1= {}
out = []
if (len(a) < len(b)):
    for i in a:
        j = dict1.get(i)
        if j:
            dict1[i] +=1
        else:
            dict1[i] = 1
    for i in b:
        j = dict1.get(i)
        if j:
            if i not in out:
                out.append(i)
else:
    for i in a:
        j = dict1.get(i)
        if j:
            dict1[i] +=1
        else:
            dict1[i] = 1
    for i in b:
        j = dict1.get(i)
        if j:
            if i not in out:
                out.append(i)
print(out)
