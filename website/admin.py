from django.contrib import admin
from website.models import Report, News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug":("name",)}
    list_display = ("name","views")

class ReportAdmin(admin.ModelAdmin):

	list_display = ("title","news_cat","text","image","date")

admin.site.register(News, NewsAdmin)
admin.site.register(Report, ReportAdmin)