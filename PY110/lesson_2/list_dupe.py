'''A developer is trying to remove duplicates from a list. 
They use a set for deduplication, but the order of 
elements is lost. How can we preserve the order?
'''

'''buggy: set does not maintain order
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data) #== [4, 2, 1, 3]) # order not guaranteed # actually [1, 2, 3, 4] 
'''

'''solution: 
loop through original list and add to newlst (unique_data),
 if count of elem is less than 1 in newlst -> append to newlst '''

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
for elem in data:
    if unique_data.count(elem) < 1:
        unique_data.append(elem)

print(unique_data == [4, 2, 1, 3]) # True

''' OR use: if elem not in new_lst (unique_data2) --  a bit more concise'''
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data2 = []
for elem in data:
    if elem not in unique_data2:
        unique_data2.append(elem)  
    
print(unique_data2 == [4, 2, 1, 3]) # True

'''OR LS way: loop through list and it elem not in set add to set and new list
if item in set then dont add bc would be dupe'''
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data3 = []
seen = set()

for item in data:
    if item not in seen:
        seen.add(item)
        unique_data3.append(item)
        # print(unique_data3) # to see how it works

print(unique_data3 == [4, 2, 1, 3]) # True