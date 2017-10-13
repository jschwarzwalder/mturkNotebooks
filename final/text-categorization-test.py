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
# In this example, we're first calling the text-categorization-test function.
# The test function doesn't cost any money and is useful for validating that your account is setup correctly and for testing your integration.
# To call the prod text-categorization function, uncomment the next line and comment out the text-categorization-test line
# function_name = 'text-categorization'
function_name = 'text-categorization-test'

# We ask the worker to provide text for what to say in a specific situation.
# Given a context
text = 'Banana'

# and an  intention, for worker to select.
# Descriptions are optional, but help guide the worker
categories = [{'label': 'Protein' , 'description' : 'Animal based but also includes eggs, soy, beans, and legumes.'},
            {'label': 'Fruit', 'description': 'Grow on trees or plants and often high in sugary carbohydrates.' },
            {'label': 'Vegetable', 'description': 'Grown in the ground or on a plant including the roots or leaves.'},
            {'label': 'Dairy', 'description': 'Milk based products'},
            {'label': 'Grain', 'description': 'Carbohydrates including wheat, rice, oats, barley, bread, and pasta'} ]




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
