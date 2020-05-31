list1 = [1,2,2,3,3,4,5,5,5]
unique =[]
for ele in list1:
    if ele not in unique:
        unique.append(ele)
print(unique)
