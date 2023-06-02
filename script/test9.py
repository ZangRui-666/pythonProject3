import os

city_list = ['Chicago__crime', 'San', 'NYC']
b_list = [150, 300, 500, 1000, 1500, 2000, 3000, 5000]
base_path = '/Users/patrick/Desktop/hkbu-college/doc/year3/sem1/econ3105/pythonProject3/'
for city in city_list:
    for i in b_list:
        layer_name = city + '_b' + str(i)
        path = base_path + layer_name + '_kdv.png'
        new_path = base_path + layer_name + '_from_py.png'
        os.rename(path, new_path)
