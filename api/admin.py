from django.contrib import admin
from .models import Company, Advocate, AdvocateLink

# Register your models here.
admin.site.register(Company)
admin.site.register(Advocate)
admin.site.register(AdvocateLink)
