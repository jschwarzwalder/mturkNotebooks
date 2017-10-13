from mturk_crowd_beta_client import MTurkCrowdClient
from boto3.session import Session
import uuid

# This examples assume you have a local AWS profile called
# 'mturk-crowd-caller', but you can authenticate however you like,
# including by directly passing in your access key and secret key.
session = Session(profile_name='mturk-crowd-caller')

# Create the client
crowd_client = MTurkCrowdClient(session)

# For this example, we'll give our task a random, unique name. For prod
# tasks, you'll probably want to pick a name based on your input source.


# Next, we specify the name of the function to call
function_name = 'image-similarity'


task_name = 'my-test-task-359b74a52b5e4446a7feb2ab4d97fd1a'

# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'status_code': get_result.status_code, 'name': function_name, 'task': get_result.json()}))

# Next, we specify the name of the function to call
function_name = 'image-similarity'


task_name = 'my-test-task-93bf495576eb48378e656d098c2f421f'

# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'status_code': get_result.status_code, 'name': function_name, 'task': get_result.json()}))



function_name = 'text-intent-detection'


task_name = 'my-test-task-326f0ffff29b40d8847f4545fd570d5d'

# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'status_code': get_result.status_code, 'name': function_name, 'task': get_result.json()}))



function_name = 'text-categorization'


task_name = 'my-test-task-1c040e329ee44f90b40f056ed0e65cd9'

# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'status_code': get_result.status_code, 'name': function_name, 'task': get_result.json()}))



function_name = 'named-entity-recognition'


task_name = 'my-test-task-359b74a52b5e4446a7feb2ab4d97fd1a
'

# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'status_code': get_result.status_code, 'name': function_name, 'task': get_result.json()}))
