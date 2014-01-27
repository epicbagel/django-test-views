from django_test_views.mixins import ViewTestMixin
from django.conf import settings
from django_test_views.factories import UserFactory

class SetupAccountMixin(ViewTestMixin):
	def setUp(self):
		super(SetupAccountMixin, self).setUp()
		self.user = self.get_user_factory().create()
	# Accepts a user and logs them in to the test client
	def login(self, user, password = "password"):
		return self.client.login(username = user.email, password = password)
	# Creates a user which is not authorized to perform an action. If nothing is set
	# here, then we won't test.
	def create_unauthorized_user(self):
		return None
	# If a different login URL is used, this can be set here
	def get_login_url(self):
		return settings.LOGIN_URL
	# The factory used to create the user. Needs to be set.
	def get_user_factory(self):
		raise NotImplementedError('Specify a user factory')






