from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

@method_decorator(csrf_exempt, name='dispatch')
class InfoView(View):
    def post(self, request):
       request_body = request.body
       form_data = loads(request_body)
       id = form_data.get('id')
       name = form_data.get('name')
       Age = form_data.get('Age')
       place = form_data.get('place')
       email = form_data.get('email')
       course = form_data.get('course')
       phone = form_data.get('phone')
       data = {
           'id': id,
           'name': name,
           'Age': Age,
           'place': place,
           'email': email,
           'course': course,
           'phone': phone
       }
       return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class MarksView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)

        name = form_data.get('name')
        python = form_data.get('python')
        django = form_data.get('django')
        database = form_data.get('database')
        total = python + django + database
        average = total / 3

        data = {
            'Name': name,
            'Python': python,
            'Django': django,
            'Database': database,
            'Total out of 300': total,
            'Average': average
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class ResultView(View):
    def get(self, request):
        data = {
            'message': 'Please send a POST request with student marks to get the result.'
        }
        return JsonResponse(data)
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)

        name = form_data.get('name')
        python = form_data.get('python')
        django = form_data.get('django')
        database = form_data.get('database')
        total = python + django + database
        average = total / 3
        if average >= 90:
            grade = 'A+'
        elif average >= 80:
            grade = 'A'
        elif average >= 70:
            grade = 'B'
        elif average >= 60:
            grade = 'C'
        elif average >= 50:
            grade = 'D'
        else:
            grade = 'F'

        if average >= 50:
            status = 'Pass'
        else:
            status = 'Fail'

        data = {
            'Name': name,
            'Python': python,
            'Django': django,
            'Database': database,
            'Total out of 300': total,
            'Average': average,
            'Grade': grade,
            'Status': status
        }
        return JsonResponse(data)
   






# Create your views here.
