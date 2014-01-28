from django_test_views.mixins import BaseObjectMixin

class CreateViewTestMixin(BaseObjectMixin):
	def get_view_name(self):
		raise NotImplementedError('This is an abstract method')
	def get_post_data(self):
		raise NotImplementedError('You need to provide POST data for create view.')
	def test_view(self):
		self.login(self.user)
		response = self.should_be_callable_when_authenticated(self.user)
		# Change the data for the re-post
		data = self.manipulate_payload(response.context["form"].initial, context = response.context)
		response = self.is_callable(user = self.user, method = "post", data = data)
		# Make sure we were redirected successfully. Only happens when the object is
		# successfully created. TODO check for a success message
		self.assertEqual(response.status_code, 302)
		# Logout and test anonymous view
		self.client.logout()
		self.should_redirect_to_login_when_anonymous()
		# Check we cannot access when authanticated
		if self.create_unauthorized_user():
			response = self.is_callable(user = self.user)
			self.assertEqual(response.status_code, 302)

