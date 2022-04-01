# camunda-cloud-robot
This is a simple project that shows how you can integrate Robotframework with Camunda Clould. It uses the pyzeebe worker.


## Description

The project shows a simple example on how to use RPA with Camunda Cloud. It uses Robotframework as RPA tool (task.robot). 


In order to connect to Camunda Cloud the PyZeebe client is used. The task.py contains the business logic and starts the task.robot. 
A robotframework listener is used to get the variables from the robotframe work task. 

The worker.py polls task from Camunda Cloud. 
