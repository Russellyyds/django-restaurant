from django.contrib import admin

admin.site.site_header = 'Feane'
admin.site.site_title = 'Feane Management'
admin.site.index_title = 'Feane Management'

from Home_App.models import *

# Register your models here.
admin.site.register(ItemList)
admin.site.register(Items)
admin.site.register(AboutUs)
admin.site.register(Feedback)
admin.site.register(BookTable)
