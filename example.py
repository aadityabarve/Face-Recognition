my_dict = {'a':1, 'b':2, 'c':1}
test_dict={}
for k,v in sorted(my_dict.items()):
    # if v not in test_dict:
    #     test_dict[v]=[]
    # test_dict[v].append(k)
    if v not in test_dict:
        test_dict[v]=k
    else:
        temp=test_dict[v]
        test_dict[v]=[]
        test_dict[v].append(temp)
        test_dict[v].append(k)
for k,v in sorted(test_dict.items()):
    print(k,v)