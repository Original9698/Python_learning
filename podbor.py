def flatten_dict(d: dict, parent_key = '', sep = '_') -> dict:
    d1 = {}
    for k,v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v,dict):
            d1.update(flatten_dict(v, new_key, sep = sep))
        else:
            d1[new_key]=v
    return d1

print(flatten_dict({'Germany': {'berlin': 7},
          'Europe': {'italy': {'Rome': 3}},
          'USA': {'washington': 1, 'New York': 4}}))
