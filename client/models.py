from datetime import date, timedelta
from django.db import models
from django.contrib.auth.models import User

from common.utils import (
	EMPLOYEE_SIZE_CHOICES,
	CLIENT_VALUE_CHOICES,
	)

#################################################### SECONDARY INFORMATION ####################################################

class AddClient(models.Model):

	# NAME OF THE ORGANISATION

	user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)

	client_name = models.CharField(max_length=255, blank=False)
	organisation_name = models.CharField(max_length=255, blank=False) 
	# MultipleChoiceField or django-multiselectfield
	#https://stackoverflow.com/questions/45153419/django-how-to-use-multiplechoicefield-in-a-form-admin
	address = models.CharField(max_length=255, blank=False)
	phone_number = models.IntegerField(blank=False)
	# email_org = models.EmailField(max_length=100, blank=False)
	# introduction = models.TextField(max_length=999, blank=False)
	# ownership_type = models.CharField(max_length=255, blank=False)
	employee_size = models.CharField(max_length=255, choices=EMPLOYEE_SIZE_CHOICES)
	client_value  = models.CharField(max_length=15, choices=CLIENT_VALUE_CHOICES)
# 	created = models.DateField(auto_now=True)

# 	logo = models.ImageField(upload_to = 'common/files/images', default = 'common/files/images/display.png')
# 	# attachments
# 	#client_pic = models.ImageField(upload_to = 'common/files/images', default = 'common/files/images/display.png')

# 	# HEAD OF THE ORGANIZATION

# 	designation = models.CharField(max_length=255, blank=False)
# 	mobile_no_head = models.IntegerField(blank=False)
# 	email_head = models.EmailField(max_length=100, blank=False)
# 	social_media_id_head = models.CharField(max_length=255, blank=False)

# 	#CORE CONTACT PERSON DETAIL

# 	full_name = models.CharField(max_length=255, blank=False)
# 	designation = models.CharField(max_length=255, blank=False)
# 	office_phone = models.IntegerField(blank=False)
# 	mobile_no = models.IntegerField(blank=False)
# 	email = models.EmailField(max_length=100, blank=False)
# 	social_media_id = models.CharField(max_length=255, blank=False)

# #################################################### SECONDARY INFORMATION ####################################################

# 	#REFERENCE

# 	reference_website = models.CharField(max_length=255, blank=False)
# 	facebook_id = models.CharField(max_length=255, blank=False)
# 	linked_in_id = models.CharField(max_length=255, blank=False)

# 	# BILLING INFO

# 	pan_no = models.CharField(max_length=255, blank=False)
# 	billing_name = models.CharField(max_length=255, blank=False)

# 	# BUSINESS OUTFLOW -- SHOULD BE MULTIPLE

# 	outflowed_to = models.CharField(max_length=255, blank=False)
# 	service_outflowed = models.CharField(max_length=255, blank=False)
# 	outflow_date = models.DateField(auto_now_add=True)
# 	amount = models.PositiveIntegerField(default=0)
# 	# attachment image

# 	# BRANCHES

# 	branch_incharge = models.CharField(max_length=255, blank=False)
# 	branch_address = models.CharField(max_length=255, blank=False)
# 	branch_phone = models.CharField(max_length=255, blank=False)
# 	branch_email = models.EmailField(max_length=100, blank=False)


	def __str__(self):
		return "{}".format(self.client_name)

	# Calculating Today's, Yesterday's, This Week's, This month's and This year's Client count.

	def today_created(self):
		# count the number of entries since the given date -- in this case, yesterday to today
		date_from = date.today() - timedelta(1)
		ctdays = AddClient.objects.filter(created__gte=date_from).count()
		return ctdays

	def yesterday_created(self):
		# count the number of client entries from the day before yesterday to yesterday
		yesterday = date.today() - timedelta(1)
		day_before_yesterday = date.today() - timedelta(2)
		ctdays = AddClient.objects.filter(created__range=(yesterday, day_before_yesterday)).count()
		return ctdays

	def this_week_created(self):
		# you know the drill by now
		date_from = date.today() - timedelta(7)
		ctdays = AddClient.objects.filter(created__gte=date_from).count()
		return ctdays

	def this_month_created(self):
		# stop reading the code comments already!
		date_from = date.today() - timedelta(30)
		ctdays = AddClient.objects.filter(created__gte=date_from).count()
		return ctdays

	def this_year_created(self):
		# you're not gonna listen, are you?
		date_from = date.today() - timedelta(365)
		ctdays = AddClient.objects.filter(created__gte=date_from).count()
		return ctdays

class ListOfProduct(models.Model):

	# LIST OF PRODUCT/SERVICES

	user = models.ForeignKey(User, related_name='users_listofproduct', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_listofproduct', on_delete=models.CASCADE)

	service_name = models.CharField(max_length=255, blank=False)
	service_detail = models.CharField(max_length=255, blank=False)
	# attachment image