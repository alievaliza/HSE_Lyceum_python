import collections
    
s = input()

d, ans = dict(), ""

for el in s:
    if el in d:
        d[el] += 1
    else:
        d[el] = 1
  
for el in d_ans:
    d_ans[el] = ""

while len(d) >= 2:
    least_common = list(reversed(collections.Counter(d).most_common()[-2:]))
    d[least_common[0][0]+least_common[1][0]] = least_common[0][1] + least_common[1][1]
    del d[least_common[0][0]]
    del d[least_common[1][0]]
    
    if least_common[0][1] == least_common[1][1] and len(least_common[0][0]) > len(least_common[1][0]):
        d_new[least_common[0][0]] = "1"
        d_new[least_common[1][0]] = "0"
    else:
        d_new[least_common[0][0]] = "0"
        d_new[least_common[1][0]] = "1"

d_new = dict(collections.OrderedDict(sorted(d_new.items(), key=lambda i: -len(i[0]))))

for el_1 in d_copy:
    for el_2 in d_new:
        if el_1 in el_2:
            d_ans[el_1] += d_new[el_2]  
            
if len(d_copy) == 1:
    for el in d_copy:
        d_ans[el] = "0"
    
for letter in s:
    ans += d_ans[letter]
    
print(len(d_ans), len(ans))
for key, value in d_ans.items():
    print("{0}: {1}".format(key,value))
print(ans)
