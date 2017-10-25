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
task_name = 'my-test-task-' + uuid.uuid4().hex

# Next, we specify the name of the function to call
function_name = 'text-categorization'

# We ask the worker to provide text for what to say in a specific situation.
# Given a context
text = 'These are great. They do run a touch small. I almost could go a half size up from my normal size.'

# and an  intention, for worker to select.
# Descriptions are optional, but help guide the worker
categories = [{'label': 'Style' , 'description' : 'Customer mentions apperance or style of item.'},
            {'label': 'Fit', 'description': 'Customer mentions the cut or fit of item.' },
            {'label': 'Quality', 'description': 'Customer mentions the material or quality of item.'},
            {'label': 'Price', 'description': 'Customer mentiones the cost or price of item.'}]




# Create the task
put_result = crowd_client.put_task(function_name,
                                   task_name,
                                   {'text': text,
                                   'categories': categories })


print('PUT response: {}'.format(
    {'status_code': put_result.status_code, 'task': put_result.json()}))


# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'status_code': get_result.status_code, 'task': get_result.json()}))
