from django.shortcuts import render
from.models import Fake
from django.shortcuts import render
from django.http.response import HttpResponse
import faker
fake=faker.Faker()

def fview(request):
    for i in range(100):
        name=fake.name()
        email=fake.email()
        job=fake.random_element(elements=('hr','tl','pm','admin'))
        sal=fake.random_element(elements=('10000','180000','250000','300000'))
        city=fake.random_element(elements=('pune','hyd','che','bang'))
        dob=fake.date_time()

        data=Fake(
            name=name,
            email=email,
            job=job,
            sal=sal,
            city=city,
            dob=dob,
                   )
        data.save()
    return HttpResponse('data inserted successfully')
def fecthing_data(request):
    fdata=Fake.objects.filter(name__startswith='A+')
    return render(request,'fakedata.html',{'fdata':fdata})





# Create your views here.
