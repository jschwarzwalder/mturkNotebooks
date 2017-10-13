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
task_name = 'my-test-task-2c28dbb029f4400a8d90219b3909d7da'

# Next, we specify the name of the function to call
function_name = 'image-similarity'


task_name = 'my-test-task-27f7a6f1052540dd8e4a29298f5d8967'

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


task_name = 'my-test-task-58a07ec626ee492b93a679e5cad79a2d'

# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'status_code': get_result.status_code, 'name': function_name, 'task': get_result.json()}))
