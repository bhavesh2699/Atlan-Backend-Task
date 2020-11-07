from django.shortcuts import render

# Create your views here.

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from .tasks import process_file, export_process
from celery.result import AsyncResult
from celery.task.control import revoke

import json

def index(request):
	return render(request, 'collect/base.html')


class UploadView(APIView):

	def get(self, request, task_id, format=None):

		if task_id:	
			result = AsyncResult(task_id)
			if result.state == 'SUCCESS':
				print(result.get('file', ''))
				return Response({
					"status": "Success",
					"result": {
						"state": result.state,
						"done": result.info,
						"result": result.get(),
						"file": "{}{}".format(settings.MEDIA_URL, result.get())
						}
					})	
			return Response({
				"status": "Success",
				"result": {
					"state": result.state,
					"done": result.info
					}
				})
		return Response({
			"status": "Error",
			"message": "Task id is not provided."
			})

	def post(self, request, task_id, format=None):
		
		data = request.data.copy()
		
		file = data.get('file', '')

		if file:
			if settings.CELERY_USE:
				task = process_file.delay(file)
			else:
				task = process_file(file)
			return Response({
				"status": "Success",
				"message": "File is being processed in background.",
				"task_id": task.id
				})
		return Response({
			"status": "Error",
			"message": "File is not uploaded."
			})

	def put(self, request, task_id, format=None):
		
		if task_id:
			try:
				res = revoke(task_id, terminate=True)
				print(res)
				return Response({
					"status": "Success",
					"message": "Task successfully terminated."
					})
			except Exception as e:
				return Response({
					"status": "Error",
					"message": "Task Id does not exists."
					})
		return Response({
			"status": "Error",
			"message": "Something went wrong."
			})


class ExportView(APIView):

	def get(self, request, format=None):
		if settings.CELERY_USE:
			task = export_process.delay()
		else:
			task = export_process()
		return Response({
			"status": "Success",
			"message": "CSV file is getting exported.",
			"task_id": task.id
			})