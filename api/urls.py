from django.conf.urls import url

from .views import index, UploadView, ExportView

app_name = 'api'

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^upload/(?P<task_id>[\d\w-]*)(/?)', UploadView.as_view(), name='upload'),
	url(r'^export/$', ExportView.as_view(), name='export'),
]