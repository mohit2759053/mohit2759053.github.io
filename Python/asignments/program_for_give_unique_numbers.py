test_list = [45,78,12,55,44,55,"a","v","a"]
print ("The original list is : " +  str(test_list))

res = []
for i in test_list:
    if i not in res:
        res.append(i)
  
print ("The list after removing duplicates : " + str(res))