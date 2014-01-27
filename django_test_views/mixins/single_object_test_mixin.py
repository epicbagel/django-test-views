
from django_test_views.mixins import BaseObjectMixin

class SingleObjectTestMixin(BaseObjectMixin):
	def get_view_kwargs(self):
		# Create the object if not created yet
		if not self.generate_data():
			self.generate_data()
		return {"pk" : self.get_data().pk}