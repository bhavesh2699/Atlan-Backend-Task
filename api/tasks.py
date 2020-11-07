from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

import time
from django.http import HttpResponse
import csv
from django.conf import settings

@task(bind=True)
def process_file(self, file):
	logger.info("File is being processed")
	reader = csv.reader(file)
	total = len(list(reader))
	# total = 5
	for i in range(total):
		print(i)
		self.update_state(state='PROGRESS', meta={'done': round((i*100.0)/(total*1.0), 2)})
		time.sleep(0.5)
	return True

@task(bind=True)
def export_process(self):
	total = 45
	with open('{}/{}.csv'.format(settings.MEDIA_ROOT, self.request.id), 'w') as csvfile:
		writer = csv.writer(csvfile)
		for i in range(total):
			writer.writerow(["Hello", "Atlan!", "Hello", "Atlan!"])
			self.update_state(state='PROGRESS', meta={'done': round((i*100.0)/(total*1.0), 2)})
			time.sleep(1.4)
	return "{}.csv".format(self.request.id)