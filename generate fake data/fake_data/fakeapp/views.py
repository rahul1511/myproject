from django.shortcuts import render
from .models import FakeData
from django.http.response import HttpResponse
import faker
fake=faker.Faker()
def fake_view(request):
    for i in range(1000):
        first_name=fake.first_name()
        last_name=fake.last_name()
        job=fake.random_element(elements=('HR','TL','ADMIN','PM'))
        email = fake.email()
        salary=fake.random_element(elements=(10000,20000,30000))
        city=fake.random_element(elements=('HYD','BANG','PUNE','CHE'))
        dob=fake.date_time()
        address=fake.address()
        data=FakeData(
            first_name=first_name,
            last_name=last_name,
            job=job,
            email=email,
            salary=salary,
            city=city,
            dob=dob,
            address=address)
        data.save()
    return HttpResponse('data inserted')

def fecthing_data(request):
    fdata=FakeData.objects.all()
    return render(request,'fakedata.html',{'fdata':fdata})










