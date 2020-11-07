# Atlan Backend Task

## Problem Statement

We want to offer an implementation through which the user can stop the long-running task at any given point in time, and can choose to resume or terminate it. This will ensure that the resources like compute/memory/storage/time are used efficiently at our end, and do not go into processing tasks that have already been stopped (and then to roll back the work done post the stop-action)
# 💡 Approach

### Upload

- A dummy CSV file is read using pandas and added row by row to a table in database.
  #### Pause
  Number of lines read are constantly being recorded, when paused an Interrupt Exception is raised which stops the upload.
  #### Resume
  The upload start funtion is called again but this time the CSV file is read from the checkpoint that we stored earlier.
  ### Terminate
  In this situation, the application needed to get back to the work done before this wrong upload started, so I dropped this particular table.
  ### Progress
  Some basic maths is being used to calculate the percentage of upload completed.

### Download/Export

- A database tabke from the server can be exported as a CSV file.
  #### Pause
  Number of lines read are constantly being recorded, when paused an Interrupt Exception is raised which stops the export.
  #### Resume
  The download start funtion is called again but this time the database table is read from the checkpoint that we stored earlier.
  ### Terminate
  In this situation, the application needed to get back to the work done before this wrong upload started, so I removed the exported CSV file.
  ### Progress
  Some basic maths is being used to calculate the percentage of download completed.

## 🔨 Features

- `Upload a CSV File` A dummy CSV file can be uploaded to the server.
- `Download/Export` Any database table can be exported as a CSV file.
  Following features are available in both upload/downlaod.
- `Pause` Pauses the upload/downlaod.
- `Resume` Resumes the upload/downlaod.
- `Terminate` Terminates/Rollbacks the upload/downlaod.

## Technologies/Tools Used:
  - Python3
  - Django
  - Celery
  - Redis

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
 
