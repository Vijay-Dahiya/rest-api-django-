from django.contrib import admin
from api.models import Company,Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin) :
    list_display = ('name','location', 'type')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin) :
    list_display = ('name','company','position')
    list_filter = ('company',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin) 


## json.dumps(python_data) it will conver python data to json data ; 
# json.loads(json_data)  vice versa of dumps
# serializeres work -> 
# 1. -> will convert complex data types (such as querryset or models ) into native python datatypes that can easily convertable into json or html etc. 
# 2. -> responsible for deserialization also convert parsed(serialized data) into complex data.

####################

# Serializer class 
 # similar to Django form and model form class

