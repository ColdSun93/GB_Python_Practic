import controller as cont


def sort_table(direct):
    print('Выберете операцию: 1 - сортировать по id или 0 - сортировать по имени')
    key = cont.get_module()
    st_direct = sorted(direct, key=lambda x: x[key][key])
    return st_direct
