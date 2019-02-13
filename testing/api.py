import json
import requests
import pprint


def call_api(some_api):
    response = requests.get(some_api)
    response.raise_for_status()
    return response.text


def slice_dict_results(some_dict):
    return some_dict['results']


def get_api_all(api_url):
    return json.loads((call_api(api_url)))


def make_api_url(some_api_dict):
    return f'http://www.dnd5eapi.co/api/{some_api_dict}/'


def get_api_results(api_url):
    return get_api_all(api_url)['results']


def get_api_cost(item_info_dict):
    return item_info_dict['cost']


def url_call(name, i):
    if i['name'] == name:
        new_call = i['url']
        return new_call


def get_api_info(name, list_of_dicts):
    for dic in list_of_dicts:   # For dict in list of dicts
        if dic['name'] == name:   # If dic['name'] == item searched for
            api_info = list([dic['name']] + [dic['url']])  # Double bracket to make sure string isn't slice by character
            return api_info


def get_item_url(name, list_of_dicts):
    for i in list_of_dicts:  # For dictionary in list of dictionaries
        # if i['name'] == name:
        #     new = i['url']
        #     return new
        new_call = url_call(name, i)
        if new_call is not None:
            return new_call



if __name__ == '__main__':
    a = '{"results": [{"name": 1, "url": 1},{"name": 2, "url": 2}]}'
    b = '{"results": 1}'
    # print(get_api_all(make_api_url('equipment')))
    # pprint.pprint(get_api_results(make_api_url('Equipment'), 'results'))
    print(get_api_cost(get_api_all(get_item_url('Club', get_api_results(make_api_url('Equipment'))))))
    # print(get_api_all(get_item_url('Acid Arrow', get_api_dictionary('spells'))))
