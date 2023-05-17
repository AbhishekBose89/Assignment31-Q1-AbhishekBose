from django.http import HttpResponse

def index(response):
    return HttpResponse("I am an upcoming fullstack developer")
