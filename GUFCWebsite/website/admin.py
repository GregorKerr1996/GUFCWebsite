from django.contrib import admin
from website.models import MatchReport, Report, News

# Register your models here.
class MatchReportAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug":("name",)}
    list_display = ("name","views")

class ReportAdmin(admin.ModelAdmin):

	list_display = ("title","matchReport","text","views")

admin.site.register(MatchReport, MatchReportAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(News)