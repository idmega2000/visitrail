from django.contrib import admin
from .models import Visitor, User, Company, CompanyCenter

# Register your models here.

from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active', 'phone')
    list_display_links = ('id', 'email')
    search_fields = ('email', 'first_name', 'last_name')
    list_per_page = 25


class CompnayAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'industry_type','phone')
    list_display_links = ('id', 'company_name')
    search_fields = ('company_name',)
    list_per_page = 25


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'host_id', 'first_name', 'last_name', 'email', 'phone', 'address', 'visit_start_period', 'visit_end_period')
    list_display_links = ('id', 'host_id', 'email')
    search_fields = ('host_id', 'email', 'visit_start_period', 'visit_end_period')
    list_per_page = 25

class CompanyCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_id', 'center')
    list_display_links = ('id', 'center')
    search_fields = ('company_id', 'center')
    list_per_page = 25


admin.site.register(User, UserAdmin)
admin.site.register(Company, CompnayAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(CompanyCenter, CompanyCenterAdmin)
