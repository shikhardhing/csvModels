from django.conf.urls import url
from . import views

urlpatterns = [
    url('posts', views.post_list, name='post_list'),
	url(r'^(?P<model_name>\w{0,50})/$', views.generate_csv, name='generate_csv'),
    url(r'^$', views.models_list, name='models_list'),
    url('importCsv', views.import_csv, name='import_csv'),
    url('importPage', views.import_page, name='import_page'),
]