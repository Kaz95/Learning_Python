import json
import requests
import re
# This module contains functions that interact with the API and those that rely on API sourced data
# url = "http://www.dnd5eapi.co/api/equipment/"


def call_api(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


# Converts json data to python dictionary
def get_api_all(json_data):
    return json.loads(json_data)


# Concatenates an api url frame with a given variable
def make_api_url(some_api_dict):
    return f'http://www.dnd5eapi.co/api/{some_api_dict}/'


# Slices a nested dictionary at a given top level key
def get_nested_api_dict(api_dump, dict_to_slice):
    return api_dump[dict_to_slice]


# some_dict = {'name': 'some_name', 'url': 'some_url'}
def url_call(name, some_dict):
    if some_dict['name'] == name:
        new_call = some_dict['url']
        return new_call


# Expects list of dictionaries
# similar to [{'name': 'some_name', 'url': 'some_url'}, {'name': 'some_name', 'url': 'some_url'}]
def get_api_info(name, list_of_dicts):
    for dic in list_of_dicts:   # For dict in list of dicts
        if dic['name'] == name:   # If dic['name'] == item searched for
            api_info = list([dic['name']] + [dic['url']])  # Double bracket to make sure string isn't slice by character
            return api_info


# Expects list of dictionaries
# similar to [{'name': 'some_name', 'url': 'some_url'}, {'name': 'some_name', 'url': 'some_url'}]
def get_item_url(name, list_of_dicts):
    for i in list_of_dicts:  # For dictionary in list of dictionaries
        # if i['name'] == name:
        #     new = i['url']
        #     return new
        new_url = url_call(name, i)
        if new_url is not None:
            return new_url


# Takes input as {'quantity': 'x', 'unit': 'y'}
def convert_price_info(price_dict):
    if price_dict['unit'] == 'gp':
        converted_value = price_dict['quantity'] * 100  # Converts gp prices to universal cp unit used for back end math
        return converted_value
    elif price_dict['unit'] == 'sp':
        converted_value = price_dict['quantity'] * 10   # Converts sp prices to universal cp unit used for back end math
        return converted_value
    if price_dict['unit'] == 'cp':
        return price_dict['quantity']


# Slices index number from api url
def regex(api, yup):
    reg = re.compile(r'(?<=' + re.escape(yup) + r')\d{1,3}')
    temp_obj = reg.search(api)
    # print(temp_obj)
    # print(reg)
    string = temp_obj.group()
    return string


if __name__ == '__main__':
    equip = 'http://www.dnd5eapi.co/api/equipment/145'
    spells = 'http://www.dnd5eapi.co/api/spells/12'
    feat = 'http://www.dnd5eapi.co/api/features/312'
    classes = 'http://www.dnd5eapi.co/api/classes/5'
    a = '{"results": [{"name": 1, "url": 1},{"name": 2, "url": 2}]}'
    b = '{"results": 1}'
    # print(get_api_all(make_api_url('equipment')))
    # pprint.pprint(get_api_results(make_api_url('Equipment'), 'results'))
    # print(get_api_cost(get_api_all(get_item_url('Club', get_api_results(make_api_url('Equipment'))))))
    # print(get_api_all(get_item_url('Acid Arrow', get_api_dictionary('spells'))))
    print(regex(equip, 'equipment/'))
    print(regex(spells, 'spells/'))
    print(regex(feat, 'features/'))
    print(regex(classes, 'classes/'))
