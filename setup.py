from setuptools import setup, find_packages
import django_test_views
setup(name='django-test-views',
	version=django_test_views.__version__,
	packages = find_packages(),
	license='The MIT License',
	platforms=['OS Independent'],
	keywords='django, testing',
	author='Jon Bolt',
	author_email='jon@epicbagel.com',
	url="https://github.com/epicbagel/django-test-views",
)
