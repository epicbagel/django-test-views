
class AnonymousUserOnlyTestMixin(object):
	# Test to see fi the page can be correctly accessed by authentication state
	def test_view(self):
		# As an non-authenticated user, it should be possible to access the URL.
		resp = self.client.get(self.get_url())
		self.assertEqual(resp.status_code, 200)
		# Check that the authenticated user has been successfully directed to the approparite view.
		self.login(self.user)
		resp = self.client.get(self.get_url())
		self.assertEqual(resp.status_code, 302)
