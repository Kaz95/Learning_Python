import re


def regex(api):
    rege = re.compile(r'(?<=equipment/)\d{1,3}')
    temp_obj = rege.search(api)
    print(temp_obj)
    string = temp_obj.group()
    return string


url = 'http://www.dnd5eapi.co/api/equipment/21'


if __name__ == '__main__':
    print(regex(url))