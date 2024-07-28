from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils import timezone

import pandas as pd
from .tasks import duplicate_task, missing_values_task

#We can send the order of execution of tasks in our API call in JSON format, 
#Each key-value will indicate the attributes and type of task
#for example we are using numbers here 1 means access missing values! 2 means identify duplicate rows! 
#We will generalize this by creating a python script which will take 2 inputs 
#first number which is kind of task, second is attributes for the task! 
#we will verify the input attributes and process accordingly
#In this way you can add more tasks! 

@csrf_exempt
@require_http_methods(["POST"])

def run_pipeline(request):
    #static path and data, can be modified to take dynamic data! 
    PATH = 'C:\\Users\\Sonu-PC\\OneDrive\\Desktop\\New folder\\civic_task\\civic_test\\data.csv'
    data = json.loads(request.body)
    df = pd.read_csv(PATH)
    list = df.columns.values.tolist()

    map = {}
    #Add tasks here
    map["1"] = duplicate_task.DuplicateTask
    map["2"] = missing_values_task.MissingTask
    res = {}
    try:
        i = 1
        for d in data:
            if d not in map:
                res[i] = "Invalid Request Number"
            else:
                res[i] = map[d].processTask(df, data, list)
            i += 1    
        return JsonResponse(res) 
    except ValueError:
        return JsonResponse({"Result" : "Invalid Json!"})  

