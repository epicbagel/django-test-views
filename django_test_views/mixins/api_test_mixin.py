from django_test_views.mixins import BaseObjectMixin
from tastypie.test import ResourceTestCase

class ApiTestCase(BaseObjectMixin, ResourceTestCase):
	def get_list_url(self):
		return "/api/v1/%s/" % self.get_resource_name()
	def get_detail_url(self):
		return "/api/v1/%s/%s/" % (self.get_resource_name(), self.get_data().pk)
	def get_resource_name(self):
		return self.get_factory_class().FACTORY_FOR._meta.verbose_name
	def test_list(self):
		self.login(self.user)
		self.generate_data()
		# Get the list of items
		response = self.client.get(self.get_list_url(), format='json')
		# Check to see if the JSON is returned and the object exists
		self.assertValidJSONResponse(response)
		data = self.deserialize(response)["objects"][0]
		self.assertEqual(data.get("id"), self.get_data().pk)
		# Get the specific item
		response = self.client.get(self.get_detail_url(), format='json')
		# Check to see if the JSON is returned and the object exists
		self.assertValidJSONResponse(response)
		self.assertEqual(self.deserialize(response).get("id"), self.get_data().pk)


