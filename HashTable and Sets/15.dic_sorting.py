my_dict = {'apple': 3, 'banana': 3, 'orange': 5}
sorted_dic=sorted(my_dict.items())
print(sorted_dic)

sorted_by_value_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=False))
print(sorted_by_value_desc)

