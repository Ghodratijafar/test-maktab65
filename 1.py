def tuple_dict_converter(list_tuple_dict):
    if isinstance(list_tuple_dict,(list,tuple)):
        list_1 = []
        list_2 = []
        for i in list_tuple_dict:
            list_1.append(i[0]) 
            list_2.append(i[1])
        dictionary = dict(zip(list_1,list_2))
    elif isinstance(list_tuple_dict,dict):
        list_1 = list(list_tuple_dict.keys())
        list_2 = list(list_tuple_dict.values())
        dictionary =list(zip(list_1,list_2))
    return dictionary

print(tuple_dict_converter({'a':1,'b':2}))
print(tuple_dict_converter([('a',1),('b',2)]))