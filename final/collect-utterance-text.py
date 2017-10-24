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
function_name = 'collect-utterance-for-intent'

# We ask the worker to provide text for what to say in a specific situation.
# Given a context
context = 'They recieved a bill that is higher than expected'

# and an  intention, for situation.
intent = 'They want to get bill reduced to expected amount'



# Create the task
put_result = crowd_client.put_task(function_name,
                                   task_name,
                                   {'context': context,
                                   'intent': intent })



print('PUT response: {}'.format(
    {'status_code': put_result.status_code, 'task': put_result.json()}))


# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'api-name': function_name, 'status_code': get_result.status_code, 'task': get_result.json()}))
