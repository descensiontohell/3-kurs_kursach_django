from django.db import models
from django import forms
from . models import *
from datetime import *
from django.contrib.auth.models import User

class customer(models.Model):
	FIRST_NAME = models.TextField()
	SECOND_NAME = models.TextField()
	PATRON_NAME = models.TextField()
	PHONE_NUMBER = models.CharField(max_length = 14)

class NewCustomer(forms.ModelForm):
	class Meta(object):
		model = customer
		fields = ("FIRST_NAME", "SECOND_NAME", "PATRON_NAME", "PHONE_NUMBER")

class LoginForm(forms.ModelForm):
	class Meta(object):
		model = User
		fields = ("username", "password")

class works_list(models.Model):
	WORK_TYPE = models.IntegerField()
	TYPE_NAME = models.TextField()
	WORK_ID = models.AutoField(primary_key=True)
	WORK_NAME = models.TextField()
	PART_NAME = models.TextField()
	WORK_COST = models.IntegerField()
	WARRANTY = models.IntegerField()

class cars_info(models.Model):
	CAR_ID = models.AutoField(primary_key=True)
	CAR_BRAND = models.TextField()
	CAR_MODEL = models.TextField()
	CAR_YEAR = models.IntegerField()
	CAR_ENGINE = models.TextField()

class NewCar(forms.ModelForm):
	class Meta(object):
		model = cars_info
		fields = ("CAR_BRAND", "CAR_MODEL", "CAR_YEAR", "CAR_ENGINE")

class worker_list(models.Model):
	WORKER_ID = models.AutoField(primary_key=True)
	FIRST_NAME = models.TextField()
	SECOND_NAME = models.TextField()
	PATRON_NAME = models.TextField()
	POSITION = models.TextField()
	TYPE_NAME = models.TextField(null=True)
	WAGE = models.IntegerField()

class NewWorker(forms.ModelForm):
	class Meta(object):
		model = worker_list
		fields = ("FIRST_NAME", "SECOND_NAME", "PATRON_NAME", "POSITION", "TYPE_NAME", "WAGE")

class pending(models.Model):
	TICKET_ID = models.AutoField(primary_key=True)
	WDATE = models.TextField()
	WTIME = models.TextField()
	WORK_ID = models.ForeignKey(works_list, on_delete=models.DO_NOTHING)
	CUSTOMER_ID = models.ForeignKey(customer, on_delete=models.CASCADE)
	CAR_ID = models.ForeignKey(cars_info, on_delete=models.CASCADE)
	IS_FINISHED = models.IntegerField(default=0)


class AddPending(forms.ModelForm):
	class Meta(object):
		model = pending
		fields = ("WDATE", "WTIME","WORK_ID", "CUSTOMER_ID", "CAR_ID")
		#extra_kwargs = {'TIME': {'format': '%H:%M'}}


class finished_works(models.Model):
	TICKET_ID = models.ForeignKey(pending, on_delete=models.DO_NOTHING)
	DATE = models.DateField(datetime.now().date())
	CAR_ID = models.ForeignKey(cars_info, on_delete=models.DO_NOTHING)
	CUSTOMER_ID = models.ForeignKey(customer, on_delete=models.DO_NOTHING)
	WORK_ID = models.ForeignKey(works_list, on_delete=models.DO_NOTHING)
	COST = models.IntegerField()
	WORKER_ID = models.ForeignKey(worker_list, on_delete=models.DO_NOTHING)
	WARRANTY = models.IntegerField()


class parts(models.Model):
	PART_ID = models.AutoField(primary_key=True)
	PART_NAME = models.TextField()
	CAR_ID = models.IntegerField(default=0)
	QUANTITY = models.IntegerField(null=False)
	PART_COST = models.IntegerField(null=False)


class suppliers(models.Model):
	SUPPLIER_ID = models.AutoField(primary_key=True)
	SUPPLIER_NAME = models.TextField()
	CONTACT_PHONE = models.TextField()
	CONTACT_MAIL = models.TextField()


class NewSupplier(forms.ModelForm):
	class Meta(object):
		model = suppliers
		fields = ("SUPPLIER_ID", "SUPPLIER_NAME", "CONTACT_PHONE", "CONTACT_MAIL")


class bought_parts(models.Model):
	PART_ID = models.AutoField(primary_key=True)
	PART_NAME = models.TextField(null=False)
	CAR_ID = models.IntegerField()
	QUANTITY = models.IntegerField(null=False)
	PART_COST = models.IntegerField(null=False)
	SUPPLIER_ID = models.ForeignKey(suppliers, on_delete=models.DO_NOTHING)
	DATE = models.DateField(auto_now_add=True)


class AddBought(forms.ModelForm):
	class Meta(object):
		model = bought_parts
		fields = ("PART_NAME", "CAR_ID", "QUANTITY", "PART_COST", "SUPPLIER_ID")


class AddToStock(forms.ModelForm):
	class Meta(object):
		model = parts
		fields = ("PART_NAME", "QUANTITY","PART_COST", "CAR_ID")


class stock_displayer(models.Model):
	PART_ID = models.AutoField(primary_key=True)
	CAR_BRAND = models.TextField()
	CAR_MODEL = models.TextField()
	CAR_YEAR = models.IntegerField()
	CAR_ENGINE = models.TextField()
	PART_NAME = models.TextField()
	QUANTITY = models.IntegerField()
	PART_COST = models.IntegerField()
	class Meta:
		managed = False
		db_table = 'manager_display_stock'

class pending_displayer(models.Model):
	TICKET_ID = models.AutoField(primary_key=True)
	WDATE = models.TextField()
	WTIME = models.TextField()
	WORK_NAME = models.TextField()
	SECOND_NAME = models.TextField()
	FIRST_NAME = models.TextField()
	CAR_BRAND = models.TextField()
	CAR_MODEL = models.TextField()
	class Meta:
		managed = False
		db_table = 'manager_pending_displayer'

class finished_displayer(models.Model):
	TICKET_ID = models.AutoField(primary_key=True)
	WDATE = models.TextField()
	WTIME = models.TextField()
	WORK_NAME = models.TextField()
	SECOND_NAME = models.TextField()
	FIRST_NAME = models.TextField()
	CAR_BRAND = models.TextField()
	CAR_MODEL = models.TextField()
	class Meta:
		managed = False
		db_table = 'manager_finished_displayer'

#class finished_displayer(models.Model):