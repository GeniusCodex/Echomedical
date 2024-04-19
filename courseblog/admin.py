from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'price', 'description', 'image')
  prepopulated_fields = {'slug': ('title', )}
admin.site.register(Courses, CourseAdmin)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartitems)