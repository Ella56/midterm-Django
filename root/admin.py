from django.contrib import admin

from .models import FQA,Prices,Pros,Services,Services_two,Testimonials



admin.site.register(Pros)
admin.site.register(Testimonials)
admin.site.register(FQA)
admin.site.register(Prices)
admin.site.register(Services)
admin.site.register(Services_two)

