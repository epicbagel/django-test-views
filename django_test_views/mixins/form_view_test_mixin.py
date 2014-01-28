# Loads a URL, posts data and checks the result
class FormViewTestMixin(object):
	# Allows the payload to be manipulated before posting back
	def manipulate_payload(self, form, context):
		return form
	# Allows a custom form name to be passed
	def get_form_name(self):
		return "form"
	# Additional checks on the returned context
	def check_form_response(self, response):
		return
	# Runs the check on the form view
	def test_view(self):
		# Check we can access the page
		#response = self.client.get(reverse("accounts:change-password"))
		response = self.should_be_callable_when_authenticated(self.user)
		# Load and set the form data
		data = self.manipulate_payload(response.context[self.get_form_name()].initial, context = response.context)
		# Post the data
		response = self.is_callable(user = self.user, extra = {
			"follow" : True,
		}, method = "post", data = data)
		# Check the new password has been set
		self.assertEqual(response.status_code, 200)
		# Run any additional checks
		self.check_form_response(response)
		# Log out and access the page
		self.client.logout()
		self.should_redirect_to_login_when_anonymous()
		
		