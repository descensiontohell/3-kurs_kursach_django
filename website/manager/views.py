from django.shortcuts import *
from .models import *
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import *

def landing(request):
    return render(request, 'landing.html', {"customers":customer.objects.all()})

def add_customer(request):
	if request.method == "POST":
		form = NewCustomer(request.POST)
		if form["FIRST_NAME"] and form["SECOND_NAME"]:
			if form.is_valid():
				form.save()
				return render(request, 'add_customer.html', {"customers":customer.objects.all()})
		else:
			form['errors'] = u"Введено недостаточно данных"
			return render(request, 'add_customer.html', {"customers":customer.objects.all()})
	else:
		return render(request, 'add_customer.html', {"customers":customer.objects.all()})

def signin(request):
	if request.method == "POST":
		form = {'name': request.POST["name"], 'password':request.POST["password"]}
		if form["name"] and form["password"]:
			user = authenticate(username=form['name'], password=form['password'])
			if user:
				login(request,user)
				return HttpResponseRedirect("http://127.0.0.1:8000/new_customer/")
			else:
				form['errors'] = u"Неверное имя или пароль"
				return render(request,'signin.html',{'form':form})
	return render(request,'signin.html',{})

#def isCommonPart(work_name_string):
#	needed_work = works_list.objects.get(WORK_NAME=work_name_string)
#	needed_parts = needed_work.PART_NAME
#	parts_object = parts.objects.get(PART_NAME=needed_parts)
#	if parts_object.CAR_ID == 0 and parts_object.QUANTITY > 0:
#		return true
#	else:
#		return false

#def isEnoughParts(one_more_work_name, car_id):
#	needed_work = works_list.objects.get(WORK_NAME=work_name_string)
#	needed_parts = needed_work.PART_NAME
#	parts_object = parts.objects.get(PART_NAME=needed_parts)
#	if isCommonPart(one_more_work_name):
#		return true
#	elif parts_object.CAR_ID == car_id and parts_object.QUANTITY > 0:
#		return true
#	else:
#		return false

def new_pending(request):
	if request.method == "POST":
		form = AddPending(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'pending.html', {"tickets":pending_displayer.objects.all().order_by('-WDATE','-WTIME')})
		else:
			form['errors'] = u"Неверные данные"
			return render(request, 'pending.html', {"tickets":pending_displayer.objects.all().order_by('-WDATE','-WTIME')})
	else:
		return render(request, 'pending.html', {"tickets":pending_displayer.objects.all().order_by('-WDATE','-WTIME')})


def add_finished(request):
	if request.method == "POST":
		form = {'TICKET_number': request.POST["TICKET_ID"]}
		number = form["TICKET_number"]
		ticket=pending.objects.get(TICKET_ID=number)
		ticket.IS_FINISHED = 1
		ticket.save()
		return render(request, 'finished.html', {"tickets":finished_displayer.objects.all().order_by('-WDATE','-WTIME')})
	return render(request, 'finished.html', {"tickets":finished_displayer.objects.all().order_by('-WDATE','-WTIME')})


def get_stock(request): 
	return render(request, 'stock.html', {"parts":stock_displayer.objects.all()})


def get_suppliers(request): 
	if request.method == "POST":
		form = NewSupplier(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'suppliers.html', {"supplier_list":suppliers.objects.all()})
		else:
			form['errors'] = u"Неверные данные"
			return render(request, 'suppliers.html', {"supplier_list":suppliers.objects.all()})
	else:
		return render(request, 'suppliers.html', {"supplier_list":suppliers.objects.all()})


def add_worker(request):
	if request.method == "POST":
		form = {'FIRST_NAME': request.POST["FIRST_NAME"], 'SECOND_NAME':request.POST["SECOND_NAME"], 'PATRON_NAME':request.POST["PATRON_NAME"], 'POSITION':request.POST["POSITION"], 'TYPE_NAME':request.POST["TYPE_NAME"], 'WAGE':request.POST["WAGE"]}
		if form["FIRST_NAME"] and form["SECOND_NAME"] and form["PATRON_NAME"] and form["POSITION"] and form["WAGE"]:
			new_worker = worker_list.objects.create(FIRST_NAME=form["FIRST_NAME"],SECOND_NAME=form["SECOND_NAME"],PATRON_NAME=form["PATRON_NAME"],POSITION=form["POSITION"],TYPE_NAME=form["TYPE_NAME"],WAGE=form["WAGE"])
			new_worker.save()
			return render(request, 'workers.html', {"workers":worker_list.objects.all()})
		else:
			form['errors'] = u"Заполните все необходимые поля"
			return render(request, 'workers.html', {"workers":worker_list.objects.all()})
	else:
		return render(request, 'workers.html', {"workers":worker_list.objects.all()})

#def add_customer(request):
#	if request.method == "POST":
#		form = NewCustomer(request.POST)
#		if form["FIRST_NAME"] and form["SECOND_NAME"]:
#			form.save()
#			return render(request, 'add_customer.html', {"customers":customer.objects.all()})
#		else:
#			return render(request, 'add_customer.html', {"customers":customer.objects.all()})
#	else:
#		return render(request, 'add_customer.html', {"customers":customer.objects.all()})


def cars(request):
	if request.method == "POST":
		form = NewCar(request.POST)
		if form["CAR_BRAND"] and form["CAR_MODEL"] and form["CAR_ENGINE"] and form["CAR_YEAR"]:
			all_cars = cars_info.objects.all()
			for car in all_cars:
				if car.CAR_BRAND == form["CAR_BRAND"] and car.CAR_MODEL == form["CAR_MODEL"] and car.CAR_MODEL == form["CAR_ENGINE"] and car.CAR_YEAR == form["CAR_YEAR"]:
					form['errors'] = u"Автомобиль есть в базе"
					return render(request, 'cars.html', {"cars":cars_info.objects.all().order_by('CAR_BRAND', 'CAR_MODEL')})
			form.save()
			return render(request, 'cars.html', {"cars":cars_info.objects.all().order_by('CAR_BRAND', 'CAR_MODEL')})
		else:
			form['errors'] = u"Заполните все необходимые поля"
			return render(request, 'cars.html', {"cars":cars_info.objects.all().order_by('CAR_BRAND', 'CAR_MODEL')})
	else:
		return render(request, 'cars.html', {"cars":cars_info.objects.all().order_by('CAR_BRAND', 'CAR_MODEL')})


def works(request):
	if request.method == "POST":
		form = {'TYPE_NAME': request.POST["TYPE_NAME"], 'WORK_NAME':request.POST["WORK_NAME"], 'PART_NAME':request.POST["PART_NAME"], 'WORK_COST':request.POST["WORK_COST"], 'WARRANTY':request.POST["WARRANTY"]}
		if form["TYPE_NAME"] and form["WORK_NAME"] and form["WORK_COST"] and form["WARRANTY"]:
			all_works = works_list.objects.all()
			for work in all_works:
				if work.WORK_NAME == form["WORK_NAME"]:
					form['errors'] = u"Название уже занято"
					return render(request, 'works.html', {"works":works_list.objects.all().order_by('TYPE_NAME')})
			typenametoid={
				'КУЗОВНЫЕ РАБОТЫ': 1,
				'ТЕХНИЧЕСКОЕ ОБСЛУЖИВАНИЕ': 2,
				'ШИНОМОНТАЖ': 3,
			}
			new_work = works_list.objects.create(WORK_TYPE=typenametoid[form["TYPE_NAME"]],TYPE_NAME=form["TYPE_NAME"],WORK_NAME=form["WORK_NAME"],PART_NAME=form["PART_NAME"],WORK_COST=form["WORK_COST"],WARRANTY=form["WARRANTY"])
			new_work.save()
			return render(request, 'works.html', {"works":works_list.objects.all().order_by('TYPE_NAME')})
		else:
			return render(request, 'works.html', {"works":works_list.objects.all().order_by('TYPE_NAME')})
	else:
		return render(request, 'works.html', {"works":works_list.objects.all().order_by('TYPE_NAME')})


def bought(request):
	if request.method == "POST":
		new_part = AddBought(request.POST)
		addpart = AddToStock(request.POST)
		new_part.save()
		stock_list = parts.objects.all()
		counter = 0
		for part in stock_list:
			if part.CAR_ID == new_part.cleaned_data.get('CAR_ID') and part.PART_NAME == new_part.cleaned_data.get('PART_NAME'):
				part.QUANTITY = part.QUANTITY + new_part.cleaned_data.get('QUANTITY')
				part.save()
				counter = counter + 1
		if counter == 0:
			addpart.save()
		return render(request, 'bought.html', {"bought_list": bought_parts.objects.all().order_by('-PART_ID')})
	else:
		return render(request, 'bought.html', {"bought_list": bought_parts.objects.all().order_by('-PART_ID')})

# Create your views here.
