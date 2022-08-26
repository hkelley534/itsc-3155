def combine_dicts(dict1, dict2):
    for x in dict1:
        if x in dict2:
            dict1[x] = dict2[x] + dict1[x]
        else:
            dict1[x]=dict2[x]
            
    return dict1

# dict1 = input("Input first dictionary: ")
# dict2 = input("Input second dictionary: ")

dict1 = {'a':100, 'b':200}
dict2 = {'a':300, 'c':100}

combined_dict = combine_dicts(dict1, dict2)

print(combined_dict)
