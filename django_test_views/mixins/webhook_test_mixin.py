# Loads a URL, posts data and checks the result
class WebhookTestMixin(object):
	# This is the data that is passed to the webhook view.
	def get_json_data(self):
		raise NotImplementedError('You need to specify JSON data from the webhook.')
	# Additional checks on the returned context
	def check_response(self, response):
		return
	# Runs the check on the form view
	def test_view(self):
		# Check we can get an error when nothing is passed
		response = self.client.post(self.get_url(), data = self.get_json_data(), content_type = 'text/javascript')
		self.assertEqual(response.status_code, 200)


