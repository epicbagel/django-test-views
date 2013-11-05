
class AuthenticatedViewTestMixin(object):
	# Test to see fi the page can be correctly accessed by authentication state
	def test_view(self):
		# As an non-authenticated user, it should not be possible to access the URL.
		self.should_redirect_to_login_when_anonymous()
		# Check that the authenticated user can successfully access
		self.should_be_callable_when_authenticated(self.user)
		
