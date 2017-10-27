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
# Note only label is required.
# Descriptions amd examples are optional, but help guide the worker.
categories = [{'label': 'Style' , 'description' : 'Customer mentions appearance or style of item.',
                'positiveExamples':  [{'text': 'Not the color I ordered' },{'text': 'No longer in season'}],
                'negativeExamples': [{'text':'Too large' },{'text': 'Fabric was too thin'}] },
            {'label': 'Fit', 'description': 'Customer mentions the cut or fit of item.',
                'positiveExamples':  [{'text': 'This was too short.' },{'text': 'Doesn\'t work for my body type.'}],
                'negativeExamples': [{'text':'I don\'t like the baggy look' },{'text': 'Neckline is too low cut'}]},
            {'label': 'Quality', 'description': 'Customer mentions the material or quality of item.',
                'positiveExamples':  [{'text': 'Seams are not reinforced.' },{'text': 'Fabric has a low thread count.'}],
                'negativeExamples': [{'text':'Too expensive for what I recieved' },{'text': 'Seams ripped when I tried it on'}]},
            {'label': 'Price', 'description': 'Customer mentiones the cost or price of item.',
                'positiveExamples':  [{'text': 'This is not worth the price' },{'text': 'The price was so great I ordered four and return the ones I don\'t like'}],
                'negativeExamples': [{'text':'I would not recommend anyone to purchase' },{'text': 'Craftmanship is too cheap'}]}]




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
