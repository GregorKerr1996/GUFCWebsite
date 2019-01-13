from django.contrib import admin
from website.models import MatchReport, Report, News

# Register your models here.
class ReportAdmin(admin.ModelAdmin):

	list_display = ("title","matchReport","text","views")

admin.site.register(MatchReport)
admin.site.register(Report,ReportAdmin)
admin.site.register(News)