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
# session = Session(profile_name='mturk-crowd-caller')

# Create the client
crowd_client = MTurkCrowdClient(session)

# For this example, we'll give our task a random, unique name. For prod
# tasks, you'll probably want to pick a name based on your input source.
task_name = 'my-test-task-' + uuid.uuid4().hex
task_name = 'my-test-task-85cb72fbeed547f2ab5c6a2db89e92b2'

# Next, we specify the name of the function to call
# In this example, we're first calling the semantic-similarity-test function.
# The test function doesn't cost any money and is useful for validating that your account is setup correctly and for testing your integration.
# To call the prod semantic-similarity function, uncomment the next line and comment out the emotion-detection-test line
function_name = 'semantic-similarity'
#function_name = 'semantic-similarity-test'

# The text we want to compare
text1 = 'The sky is blue.'
text2 = 'The sky was the color of blue.'

# Create the task              
# put_result = crowd_client.put_task(function_name,
#                                    task_name,
#                                    {'text1': text1, 'text2': text2})

# print('PUT response: {}'.format(
#   {'status_code': put_result.status_code, 'task': put_result.json()}))


           
# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(                     
    {'status_code': get_result.status_code, 'task': get_result.json()}))