from django.shortcuts import render
from testing.models import PmpAuditTesting

# Create your views here.
def  list_jobs (request):
    return render(request,'list_jobs.html',{'jobs' : PmpAuditTesting.objects.all()})