from django.db import models
from django.contrib.auth.models import User
from lead.models import LeadProcess
from common.utils import MEDIUM_CHOICES, YES_NO, SALES_STAGES

class Clientlist(models.Model):
	
    client_name = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    medium = models.CharField(max_length=255, choices=MEDIUM_CHOICES)
    medium_status = models.CharField(max_length=10, choices=YES_NO)
    contact_person = models.CharField(max_length=255, blank=False)
    remarks = models.TextField(max_length=999, blank=False)
    lead = models.ForeignKey(LeadProcess, related_name='lead', on_delete=models.CASCADE)

    def get_contact_person(self):
        return self.client_name + ' is in touch with ' + self.contact_person

    def __str__(self):
        return "{}".format(self.client_name)

class SalesStage(models.Model):
    substage = models.CharField(max_length=100)
    sales_stage = models.CharField(max_length=100, choices=SALES_STAGES)
    client = models.ForeignKey(Clientlist, related_name='client_sales', on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{}-{}".format(self.sales_stage, self.substage)