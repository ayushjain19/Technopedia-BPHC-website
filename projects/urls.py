from django.conf.urls import url
from . import views

app_name = 'projects'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name = 'index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'details'),
	url(r'^register/$', views.UserFormView.as_view(), name = 'register'),
	url(r'^project_form/$', views.ProjectForm.as_view(), name = 'project_form'),
	# url(r'^add_project/$', views.add_project, name = 'add_project'),
	]