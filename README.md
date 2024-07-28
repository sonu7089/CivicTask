# CivicTask

We can send the order of execution of tasks in our API call in JSON format, 

Each key-value will indicate the attributes and type of task

for example we are using numbers here 1 means access missing values! 2 means identify duplicate rows! 
We will generalize this by creating a python script which will take 2 inputs 
first number which is kind of task, second is attributes for the task! 
we will verify the input attributes and process accordingly
In this way you can add more tasks! 

Inorder to add more task we just need to add python script in tasks folder in myapp folder, and then add that task in views.py like 
    map["1"] = duplicate_task.DuplicateTask

In this way, it would be easy to add more tasks and update existing tasks in a swift way! Debugging would be easier! 

Example Requests and There Response: 
Request 1: 
{
    "1" : {
        "columns" : ["Email"]
    }, "2": {
        "columns" : ["Name", "Email"],
        "threshold" : 10
    }
}

Response: 
{"Task 1": 12, "Task 2": {"Name": "Acceptable", "Email": "Acceptable"}}

Request 2: 
{
    "2": {
        "columns" : ["Last_Login", "Gender"],
        "threshold" : 10
    }, "1" : {
        "columns" : ["Name", "Join_Date"]
    }
}

Response: 
{
    "Task 1": {
        "Last_Login": "Acceptable",
        "Gender": "Acceptable"
    },
    "Task 2": 5
}

Request 3: 
{
    "2": {
        "columns" : ["Last_Login", "Gender1"],
        "threshold" : 10
    }, "1" : {
        "columns" : ["Name", "Join_Date"]
    }
}

Response: 
{
    "Task 1": "Invalid Column name in List provided",
    "Task 2": 5
}
