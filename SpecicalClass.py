class Student(object):
	name='kunasaki'
	def __getattr__(self,attr):
		if attr=='age':
			return lambda: 25
		raise AttributeError('\'Student\' object no attribute \'%s\'' % attr)
		