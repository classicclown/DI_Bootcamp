def merge_dictionaries (*args):
    merged_dicts ={}
    for arg in args:
        if arg in merged_dicts.keys():
            merged_dicts[key]+=value
        else:
            merged_dicts[key]=value
    return(merged_dicts)


dict1 = {'a': 100, 'b': 200}
dict2 = {'a': 200, 'c': 300}
merge_dictionaries(dict1,dict2)
