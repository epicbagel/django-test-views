import factory
from django.contrib.auth import get_user_model

class UserFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = get_user_model()
	email = factory.Sequence(lambda n: 'user{0}@example.com'.format(n))
	password = factory.PostGenerationMethodCall('set_password', 'password')