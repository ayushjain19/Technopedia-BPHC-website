from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render, redirect
from .models import Information, Images
from .forms import ProjectForm, UserForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

class IndexView(generic.ListView):
	template_name = 'projects/index.html'
	context_object_name = 'all_projects'

	def get_queryset(self):
		return Information.objects.all()


class DetailView(generic.DetailView):
	model = Information
	template_name="projects/project_detail.html"


 # def project_form(request):
#	return render(request, 'projects/project_form.html')


# def add_project(request):
# 	if request.method == 'POST':
# 		#form = ProjectForm(request.POST, request.FILES)
# 		# if form.is_valid():
# 		info = Information()
# 		# info.project_title = form.cleaned_data['project_title']
# 		# info.description = form.cleaned_data['description']
# 		# info.photos = form.cleaned_data['photos']
# 		# i=0
# 		info.project_title = request.POST.get('project_title')
# 		info.description = request.POST.get('description')
# 		# for photo in request.POST.getlist('photos[]'):
# 		# 	info.photos[i]=request.photo
# 		# 	i=i+1
# 		info.photos = request.POST.getlist('photos[]')
# 		info.save()
# 		all_projects = Information.objects.all()
# 	return render(request, 'projects/index.html', {'all_projects': all_projects})	

class ProjectForm(FormView):
	form_class = ProjectForm
	template_name = 'projects/project_form.html'

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		info = Information()

		info.project_title = request.POST.get('project_title')
		info.description = request.POST.get('description')
		info.save()
		files = request.FILES.getlist('photos')
		if form.is_valid():
			for f in files:
				img = Images()
				img.information = info
				img.photo = f
				img.save()
		all_projects = Information.objects.all()
		# return redirect("index")
		return render(request, 'projects/index.html', {'all_projects': all_projects})

class UserFormView(View):
	form_class = UserForm
	template_name = 'projects/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})
		
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit = False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username = username, password = password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('projects:index')

		return render(request, self.template_name, {'form': form})	
	
















