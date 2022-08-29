def combine_dicts(dict1, dict2):
    dict3 = {}
    print(dict1, dict2)
    for x in dict1.items():
        for y in dict2.items():
            if x[0]==y[0]:
                dict3[x[0]]=x[1]+y[1]
            else:
                dict3[x[0]]=x[1]
                dict3[y[0]]=y[1]
    return dict3

dict1 = eval(input("Input first dictionary: "))
dict2 = eval(input("Input second dictionary: "))

combined_dict = combine_dicts(dict1, dict2)

print(combined_dict)

