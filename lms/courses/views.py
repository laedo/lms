from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .forms import FormCourse

# Create your views here.
class CoursesView(View):
    def get(self, request):
        return render(request, 'courses.html')

    def post(self, request):
    	return HttpResponse('post')

class CreateView(View):
	def get(self, request):
		form = FormCourse()

		return render(request, 'create.html', {'form': form})

	def post(self, request):
		return request
