from django_test_views.mixins import BaseObjectMixin

class ListViewTestMixin(BaseObjectMixin):
	# Generate a list of objects from the factory and the object kwargs
	# Test to see if a set of objects appears in a view
	def get_factory_kwargs(self):
		kwargs = {}#super(ListViewTestMixin, self).get_factory_kwargs()
		kwargs.update({"size" : 10})
		return kwargs
	def test_view(self):
		self.should_redirect_to_login_when_anonymous()
		# Login and generate the data
		self.login(self.user)
		data = self.generate_data()
		response = self.should_be_callable_when_authenticated(self.user)
		# Check that the item appears in the list view
		self.assertEqual(
			# List of items on the page
			sorted([object.pk for object in response.context['object_list']]),
			# Expected list of items, force to a list object
			sorted([object.pk for object in data])
		)
		# Ensure that an empty list wasn't passed
		self.assertNotEqual(len(self.get_data()), 0)



