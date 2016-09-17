import requests
import csv
def is_valid_state_num(num):
    lst = [3, 7, 43]
    return type(num)==type(5) and num not in lst and (num > 0 and num < 57 or num == 72)

def select_state():
    params = {
        'get': 'NAME',
        'for': 'state:*',
        'key': '65574da907a7e319b5fabb998098789b74e2092a'
    }
    data = requests.get("http://api.census.gov/data/2015/acs1", params=params)

    print('Please select your desired state to work in.')
    for state in data.json()[1:]:
        print(state[1], state[0])
    workplace = int(input())
    while not is_valid_state_num(workplace):
        workplace = int(input('Not a valid state input. Please try again.'))
    print('-----------')

def select_field_of_work():
    f = open('B24021.csv', 'r')
    csvf = csv.reader(f)
    print('Please select your desired field of work')
    for row in csvf:
        print(row[1], row[2])
    field = int(input())
    while type(field)!=type(5) or field < 1 or field > 36:
        print('Not a valid Field of work. Please try again.')
        field = int(input())
    return field

def average_salary():
	occupation = #getmethod#
	state_num = #getmethod#
	
	census_variables = ['NAME', occupation]
	state = 'state:{}'.format(state_num)

	params = {
		'get': ','.join(census_variables),
		'for': state,
		'key': '65574da907a7e319b5fabb998098789b74e2092a'
	}
	
	data = requests.get("http://api.census.gov/data/2015/acs1", params=params)
	income = []
	for row in data.json()[1:]:
		income.append(float(row[1]))
	print(income)
