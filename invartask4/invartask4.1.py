import os
from pprint import pprint
from prettytable import PrettyTable


modules_list = ['json']
for i in modules_list:
    try:
        import i
    except ImportError:
        print(f'{i} module not found.', end='')
        print('Do you want for me to install it?', end='')
        prompt = input('Type something to install, press Enter to skip.\n')
        if prompt:
            os.system(f'pip3 install {i}')


def read_json():
    is_opened = False
    while not is_opened:
        try:
            data = json.load(open(input('Enter a filename: ') or 'data.json'))
            is_opened = True
        except FileNotFoundError:
            file_list = []
            for i in os.listdir('.'):
                if i.endswith('.json'):
                    file_list.append(i)
            print('Here are the list of JSON files that I have found:')
            for i in file_list:
                print(i)
            print('\nDo you want to open any of these? Enter a filename.')
        except JSONDecodeError:
            is_opened = False


read_json()

"""
pprint(data[0])
print('\n')
"""
"""
print('Some info about me:')
t = PrettyTable(['Parameter', 'Value'])

for i in range(len(data[0])):
    t.add_row(
                    [
                        list(data[0].keys())[i],
                        list(data[0].values())[i]
                    ]
             )

print(f'{t}\n')
"""
print('My friends:')
t = PrettyTable(['ID', 'Name'])
for i in data[0]['friends']:
    t.add_row(i.values())

print(t)
