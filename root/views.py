from django.shortcuts import render
from .models import FQA, Services, Services_two,Testimonials,Pros,Prices

# Create your views here.
def home(request):
    services=Services.objects.filter(status=True)
    services_two=Services_two.objects.filter(status=True)
    tests=Testimonials.objects.all()
    pros=Pros.objects.filter(status=True)
    prices=Prices.objects.filter(status=True)
    fqas=FQA.objects.all()


    context= {
        'services':services,
        'services_two':services_two,
        'pros':pros,
        'prices':prices,
        'tests':tests,
        'fqas':fqas,
    }



    return render(request,"root/index.html",context=context)