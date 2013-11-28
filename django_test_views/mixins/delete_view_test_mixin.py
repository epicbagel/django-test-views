from django_test_views.mixins import SingleObjectTestMixin

# ToDo - test for another company and check for a user facing message.
class DeleteViewTestMixin(SingleObjectTestMixin):
	def get_post_delete_data(self):
		return list(self.get_data())
	# Test to see if an item can be updated
	def test_view(self):
		self.login(self.user)
		# Check we can access the delete page
		self.is_callable(user = self.user)
		# Delete the item
		response = self.is_callable(user = self.user, extra = {
			"follow" : True,
		}, method = "post")
		# Check the item has been deleted
		self.assertEqual(len(self.get_post_delete_data()), 0)
		# Logout and check we can access the page
		self.client.logout()
		self.should_redirect_to_login_when_anonymous()
		# Check we cannot access when authanticated
		if self.create_unauthorized_user():
			response = self.is_callable(user = self.user)
			self.assertEqual(response.status_code, 302)



