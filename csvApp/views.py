# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.db import models
from django.apps import apps
import csv, os
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.conf import settings

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'csvApp/post_list.html', {'posts': posts})

def import_page(request):	
	models = apps.all_models['csvApp']
	models_list=[]
	for key, value in models.items():
		models_list.append(key)
	return render(request, 'csvApp/import_page.html', {'models': models_list})

def import_csv(request):
	myfile = request.FILES['myfile']
	model_name = request.POST.get('model_name')

	Model = apps.get_model(app_label='csvApp', model_name=model_name)

	reader = csv.reader(myfile)
	header = next(reader)

	fields_dict = Model._meta.get_fields()
	fields_list=[]
	for key in fields_dict:
		fields_list.append(key.name)

	if(header==fields_list):
		# handle error here
		try:
			# Model.objects.bulk_create([Model( r for r in row) for row in reader])
			for row in reader:
				model=Model()
				for r in range(len(row)):
					print header[r]
					line = string(row)
					# model.text='asd'
					model[header[r]]=row[r]
				model.save()
			return HttpResponse('Imported Successfully')
		except Exception as e:
			return HttpResponse(e)

	else:
		return HttpResponse('fields do not match')

def models_list(request):
	models = apps.all_models['csvApp']
	models_list=[]
	for key, value in models.items():
		models_list.append(key)
	return render(request, 'csvApp/models_list.html', {'models': models_list})

def generate_csv(request, model_name):
	file_name = write_csv(model_name)
	wrapper = FileWrapper(file(file_name))
	response = HttpResponse(wrapper, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename='+model_name+'.csv'
	response['Content-Length'] = os.path.getsize(file_name)
	return response

def write_csv(model_name):
	Model = apps.get_model(app_label='csvApp', model_name=model_name)
	fields_dict = Model._meta.get_fields()
	fields_list=[]
	for key in fields_dict:
		fields_list.append(key.name)	
	meta = {
		'file': '/tmp/'+model_name+'.csv',
		'class': Model,
		'fields': fields_list # models fields you want to include 
	}
	f = open(meta['file'], 'w+')
	writer = csv.writer(f)
	writer.writerow( meta['fields'] )
	for obj in meta['class'].objects.all():
		row = [unicode(getattr(obj, field)) for field in meta['fields']]
		writer.writerow(row)
	f.close()
	print 'Data written to %s' % meta['file']
	return '/tmp/'+model_name+'.csv'