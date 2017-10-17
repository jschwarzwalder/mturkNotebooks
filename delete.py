from mturk_crowd_beta_client import MTurkCrowdClient
from boto3.session import Session
import uuid
import csv

# This examples assume you have a local AWS profile called
# 'mturk-crowd-caller', but you can authenticate however you like,
# including by directly passing in your access key and secret key.
session = Session(profile_name='mturk-crowd-caller')

# Create the client
crowd_client = MTurkCrowdClient(session)

# For this example, we'll give our task a random, unique name. For prod
# tasks, you'll probably want to pick a name based on your input source.


# Next, we specify the name of the function to call

list = []
list.append(['text-intent-detection', 'text-intent-task28'])
list.append(['text-intent-detection', 'text-intent-task29'])
list.append(['text-intent-detection', 'text-intent-task30'])
list.append(['text-intent-detection', 'text-intent-task31'])
list.append(['text-intent-detection', 'text-intent-task32'])
list.append(['text-intent-detection', 'text-intent-task33'])
list.append(['text-intent-detection', 'text-intent-task34'])
list.append(['text-intent-detection', 'text-intent-task35'])
list.append(['text-intent-detection', 'text-intent-task36'])
list.append(['text-intent-detection', 'text-intent-task37'])
list.append(['text-intent-detection', 'text-intent-task38'])
list.append(['text-intent-detection', 'text-intent-task39'])
list.append(['text-intent-detection', 'text-intent-task40'])
list.append(['text-intent-detection', 'text-intent-task41'])
list.append(['text-intent-detection', 'text-intent-task42'])
list.append(['text-intent-detection', 'text-intent-task43'])
list.append(['text-intent-detection', 'text-intent-task44'])
list.append(['text-intent-detection', 'text-intent-task45'])
list.append(['text-intent-detection', 'text-intent-task46'])
list.append(['text-intent-detection', 'text-intent-task47'])
list.append(['text-intent-detection', 'text-intent-task49'])
list.append(['text-intent-detection', 'text-intent-task48'])
list.append(['text-intent-detection', 'text-intent-task50'])
list.append(['text-intent-detection', 'text-intent-task51'])

for row in list:
    function_name = row[0]
    task_name = row[1]
    delete_result = crowd_client.delete_task(function_name,task_name)
