import random 
import hashlib 

class GroupGenerator(object):
	def __init__(self,names,groups={}):
		self.names = names 
		self.past_groups = groups
		self.groups = {}

	def generate_key(self,group):
		"""
		group: list of email addresses

		Generate a unique key for each group.
		Sort names within group before generating key to maintain reproducibility.
		Returns a hashed key.
		"""
		group.sort()
		key = ':'.join(group)
		key_unicode = key.encode('utf-8')
		hash_object = hashlib.sha1(key_unicode)
		hex_dig = hash_object.hexdigest()

		return hex_dig

	def pick_from_existing_groups(self,limit=5):
		"""
		limit: maximum allowed number of people in a group

		Pick a group from an existing set of groups.
		Returns a group (list of people).
		"""
		group_id = random.choice(list(self.groups.keys()))
		group = self.groups[group_id]
		if len(group)>limit-1:
			self.pick_from_existing_groups()
		return group


	def generate_groups(self,group_len=3,names=None,pick_from_existing=False):
		"""
		group_len: Number of people to be selected for a group
		pick_from_existing: Assign a generated group to employees(if we are picking through leftovers!)
		names: Set of people to be assigned groups

		Generate a set of groups
		"""
		if names==None:
			names = self.names
		shuffle_num = random.choice(list(range(5,11)))
		[random.shuffle(names) for i in list(range(shuffle_num))]

		i = 0 
		while len(names[i:])>=group_len: #iter through list till we have fewer than group_len
			success = False
			group = names[i:i+group_len]
			if pick_from_existing:
				group += self.pick_from_existing_groups()
			key = self.generate_key(group)

			while not success:
				if key in self.past_groups:
					if pick_from_existing:
						group += self.pick_from_existing_groups()
					key = self.generate_key(group)
				else:
					success = True

			self.groups[key] = group
			i+=group_len

		if i<len(names)-1:
			print ('remaining:',names[i:])
			self.generate_groups(group_len=1,assign_groups=True,names=names[i:])

		return self.groups


def driver():
	db = Database()
	names = db.get_employees()
	groups = set(db.get_groups())

	generator = GroupGenerator(names,groups=groups)
	groups = generator.generate_groups(group_len=4)
	db.update_groups(groups)

	db.client.close()

if __name__=='__main__':
	from database import Database
	driver()

	