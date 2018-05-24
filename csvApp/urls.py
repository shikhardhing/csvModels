from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^posts$', views.post_list, name='post_list'),
	url(r'^exportPage/$', views.models_list, name='models_list'),
	url(r'^exportPage/(?P<model_name>\w{0,50})$', views.generate_csv, name='generate_csv'),
	url(r'^importCsv$', views.import_csv, name='import_csv'),
	url(r'^importPage$', views.import_page, name='import_page'),
]