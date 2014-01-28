class BaseObjectMixin(object):
	factory_class = None
	data = None
	factory_kwargs = {}
	delete = True
	# Returns the Factory used to create the object
	def get_factory_class(self):
		# Factory class will be set on the class fetched with this method.
		if self.factory_class:
			return self.factory_class
		raise NotImplementedError('You need to specify the factory to be used.')
	# Can be overwritten to supply custom kwargs to the factory class
	def get_factory_kwargs(self):
		return self.factory_kwargs
	# Callback to update any models created
	def update_generated_data(self):
		return self.data
	# Generate a list of objects from the factory and the object kwargs
	def generate_data(self):
		if not self.data and self.delete:
			# Delete all instances of this object
			self.factory_class.FACTORY_FOR.objects.all().delete()
		if self.data:
			return self.data
		kwargs = self.get_factory_kwargs()
		if "size" in kwargs:
			# Create the list of objects
			self.data = self.get_factory_class().create_batch(**kwargs)
		else:
			# Create the list of objects
			self.data = self.get_factory_class().create(**kwargs)
		self.data = self.update_generated_data()
		return self.data
	# Returns the data generated from the factory
	def get_data(self):
		return self.data
	
	
	

