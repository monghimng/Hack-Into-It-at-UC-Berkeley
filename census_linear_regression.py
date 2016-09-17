__author__ = 'chuang'

from numpy import array,ones,linalg
from pylab import plot,show

import requests
                              # income     # household size
census_variables = ['NAME', 'B01001_001E', 'B25010_001E']

params = {
    'get': ','.join(census_variables),
    'for': 'state:*',
    'key': '65574da907a7e319b5fabb998098789b74e2092a'
}
data = requests.get("http://api.census.gov/data/2015/acs1", params=params)
hh_size = []
income = []
for row in data.json()[1:]:
    income.append(float(row[1]))
    hh_size.append(float(row[2]))
xi = array(hh_size)
y = array(income)
A = array([xi, ones(len(xi))])
w = linalg.lstsq(A.T,y)[0]
line = w[0]*xi+w[1]
plot(xi, line,'r-',xi,y,'o')
show()

