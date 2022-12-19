# fav_dict = {'d': 3, 'a': 5, 'c': 4, 'b': 6, 'e': 9, 'g': 7}
#
# sort_list = sorted(fav_dict.keys())
# print(sort_list)
# print(type(sort_list))
#
# sorted_value = sorted(fav_dict, key=fav_dict.get, reverse=True)
# print(sorted_value)
# print(type(sorted_value))


def abc_sorted_list(fav_dict: dict):
    return sorted(fav_dict.keys())


def count_sorted_list(fav_dict: dict):
    return sorted(fav_dict, key=fav_dict.get, reverse=True)


def city_views_counter(city_name, city_dict):
    pass
