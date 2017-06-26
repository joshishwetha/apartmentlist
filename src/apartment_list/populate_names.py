import random 
from database import Database

def get_names():
	names = open('names.txt','r').read()
	names = [n.replace('\xc2\xa0','') for n in names.split('\n')]
	names = list(filter(lambda x:len(x)>0,names))
	return names 

def insert_names(names):
	db = Database()
	records = []

	for i,name in enumerate(names):
		row = {}
		row['first_name'] = name.split(' ')[0]
		row['last_name'] = name.split(' ')[1]
		row['email'] = row['first_name'].lower()+\
		             '.'+\
		             row['last_name'].lower()+\
		             str(i+1)+\
		             '@gmail.com'
		records.append(row)

	db.add_records(records)


names = get_names()
insert_names(names)

