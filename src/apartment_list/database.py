from pymongo import MongoClient
import hashlib

# client = MongoClient()

class Database(object):
	def __init__(self,db='apartment_list',collection='lunch_groups'):
		"""
		db: name of the database
		collection: name of the relevant collection
		"""
		self.client = MongoClient()
		self.db = self.client.get_database(db)
		self.collection = self.db.get_collection(collection)

	def add_records(self,data):
		"""
		Add record(s) to the collection.
		Works for single as well as multiple records (bulk insert).

		data: single/multiple records given as an array.
		"""
		self.collection.insert(data)


	def update_groups(self,groups):
		"""
		For each employee, update their group for Friday's lunch.
		Every group has a unique key (generated with the combination of the members' email addressed).
		The key is used to make sure the same group is not generated for next friday.

		groups: [{'key':key,'group':[email1,email2,email3]}]
		"""
		for key in groups.keys():
			group = groups[key]
			for member in group:
				self.collection.update({'email':member},
						{'$set':{'group_id':key,
						         'group':group}
						 },upsert=True)

	def get_employees(self):
		"""
		Get email address of all employees to form lunch groups
		"""
		cur = self.collection.find({},{'email':1,'_id':0})
		emails = [record['email'] for record in cur]
		return emails


	def get_groups(self):
		"""
		Get a list of all generated groups.
		This will go in as a set of restricted keys
		"""
		cur = self.collection.find({'group_id':{'$exists':1}},
			                       {'group_id':1})
		groups = [record['group_id'] for record in cur]
		return groups


	def get_group_list(self):
		"""
		Returns a list of groups generated
		"""
		cur = self.collection.find({'group':{'$exists':1}},
			                       {'group':1})
		groups = [record['group'] for record in cur]
		return groups


	def get_group(self,email):
		"""
		Lookup group by email
		email: email to be used to query for the group
		Returns the group associated with the email
		"""
		cur = self.collection.find({'email':email},
			                       {'group':1})
		group = [record['group'] for record in cur][0]
		return group
