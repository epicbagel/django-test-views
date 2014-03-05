from django_test_views.mixins import SingleObjectTestMixin

class UpdateViewTestMixin(SingleObjectTestMixin):
	# Allows the payload to be manipulated before posting back
	def manipulate_payload(self, form, context):
		return form
	# Test to see if an item can be updated
	def test_view(self):
		self.login(self.user)
		response = self.should_be_callable_when_authenticated(self.user)
		# Change the data for the re-post
		data = self.manipulate_payload(response.context["form"].initial, context = response.context)
		response = self.is_callable(user = self.user, extra = {
			"follow" : True,
		}, method = "post", data = data)
		# Logout and test anonymous view
		self.client.logout()
		self.should_redirect_to_login_when_anonymous()
		# Check we cannot access when authanticated
		#if self.create_unauthorized_user():
		#	response = self.is_callable(user = self.user)
		#	self.assertEqual(response.status_code, 302)



