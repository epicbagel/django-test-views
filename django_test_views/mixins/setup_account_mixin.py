from django_libs.tests.mixins import ViewTestMixin
from django.conf import settings
from django_test_views.factories import UserFactory

class SetupAccountMixin(ViewTestMixin):
	def setUp(self):
		self.user = self.get_user_factory().create()

	def login(self, user, password = "password"):
		return self.client.login(username = user.email, password = password)

	def get_login_url(self):
		return settings.LOGIN_URL

	def get_user_factory(self):
		raise NotImplementedError('Specify a user factory')






