from django_test_views.mixins import UpdateViewTestMixin

class UpdateWithInlinesViewTestMixin(UpdateWithInlinesViewTestMixin):
	def manipulate_payload(self, form, context):
		# Loop through each formset in the view, populating the initial data
		for formset in context["inlines"]:
			# Add the management form details
			for label, value in formset.management_form.initial.items():
				form.update({"%s-%s" % (formset.prefix, label) : value})
			i = 0
			# Add the fields
			for formset_form in formset:
				# Add each field to the post data
				for label, value in formset_form.initial.items():
					form.update({"%s-%s-%s" % (formset.prefix, i, label) : value})
				# The ID field for the formset
				form.update({"%s-%s-id" % (formset.prefix, i) : i + 1})
				i += 1
		return form