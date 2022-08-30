from datetime import datetime
from models import Product

# one of our columns is type DATE so lets create today"s date:
today = datetime.today().strftime('%Y-%m-%d')

# instatiate the class
db = Product()

# we have 6 columns in the table and need 6 matching bits of date: 
'''
date DATE UNIQUE PRIMARY KEY,
category TEXT,
store TEXT,
name TEXT,
price REAL,
link TEXT
'''

# matching data
item = (f'{today}', 
    'T-Shirts',
    'Awesome tshirts',
    'Black Logo Tee',
    '24.99',
    'seznam'
)

# insert the data above into the table using method we called insert
# insert the same data
db.insert(item)

# read all the data in the db back, and loop over the rows
for item in db.read():
    print(item)
