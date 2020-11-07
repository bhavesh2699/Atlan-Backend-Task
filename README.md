# Atlan_Task

## Introduction

Atlan Task - Backend

Technologies/Tools Used:
  - Python3
  - Django
  - Celery
  - Redis
  - Gunicorn
  - VueJs
  - Bootstrap
 
## Run the production build of project in Docker Container
Make sure you have [Docker](https://docs.docker.com/installation/) and [docker-compose](http://docs.docker.com/compose/install/) installed in your system.
  1. Clone the project
  `https://github.com/Jeet-007/Atlan_Task.git`
  2. Move to project folder
  `cd Atlan_Task`
  3. Run `docker-compose up --build` and wait for Docker to set up the container and start the server.
  4. Open `http://localhost:8000/` in your browser to open the app
  
  ## APIs
   1. **API to Upload CSV file**
   
   `http://localhost:8000/upload/`  
   Method: POST  
   Server receives file with key as `file`  
   This API starts a celery process that traverses through the CSV file starting from the first row till last row. You can also see the progress bar of the uploading process at the frontend.
   The unique Task ID is returned as the response in the webpage which is used to stop this task.  
   
  
   Note: A `test_data.csv` file is present in root directory that can be used to check this example task.
   
   
  2. **API to Export Dummy Data**
   
   `http://localhost:8000/export/`  
   Method: GET  
   This API starts a celery procees to export dummy data in a CSV file. Also, you can see the progress bar of the export process at the frontend.
   The unique Task ID is returned as the response in the webpage which is used to stop this task.  
   
 
  3. **API to Stop a Task**
   
   `http://localhost:8000/upload/<task_id>/`  
   Method: PUT  
   Server receives `task_id` in the API URL  
   This API stops the task from the execution if the task hasn't finished yet.  
 
