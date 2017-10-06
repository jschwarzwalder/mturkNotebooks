from mturk_crowd_beta_client import MTurkCrowdClient
import boto3
from boto3.session import Session
import uuid

#Credentials for AWS
session = boto3.Session(
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id='AKIAJOAZQ2P6LYICKCSQ',
    aws_secret_access_key='AtoCOt0lKbA2RMw99EsO9lOu12+MnXOw2HhFYVQn'
)

# This examples assume you have a local AWS profile called
# 'mturk-crowd-caller', but you can authenticate however you like,
# including by directly passing in your access key and secret key.
#session = Session(profile_name='mturk-crowd-caller')

# Create the client
crowd_client = MTurkCrowdClient(session)

##################################################################################################################################################################

function_name = 'image-similarity-test'

##################################################################################################################################################################
task_name = 'my-test-task-' + function_name



##################################################################################################################################################################
# The text we want to compare
image1 = {"url": "https://cdn.pixabay.com/photo/2017/09/18/14/49/egg-sandwich-2761894_960_720.jpg"}
image2 = {"url": "https://cdn.pixabay.com/photo/2017/08/30/04/23/food-2695883_960_720.jpg"}

# Create the task
put_result = crowd_client.put_task(function_name, task_name,
					{'image1': image1, 'image2': image2})

##################################################################################################################################################################

print('PUT response: {}'.format(
  {'api': function_name, 'status_code': put_result.status_code, 'task': put_result.json()}))




# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
    {'status_code': get_result.status_code, 'task': get_result.json()}))
