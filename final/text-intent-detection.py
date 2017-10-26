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
function_name = 'intent-detection'

# We ask the worker to provide text for what to say in a specific situation.
# Given a context
text = 'my son was stung by bees and I need to know if I need to go to the ER.'

# and an  intention, for worker to select.
intents = [{'label': 'Schedule an appointment', 'description': 'Caller expresses an intent to visit with health care professional',
            'positiveExamples':  [{'text': 'I need to make an appointment with Dr. Smith' },{'text': 'Can the doctor see me today?'}],
            'negativeExamples': [{'text':'Do you sell burritos?' },{'text': 'Do you accept credit cards?'}] } ,
            {'label': 'Medical Record Request', 'description': 'Caller expresses a desire to obtain copies of their medical history',
            'positiveExamples': [{'text':'I need a copy of my kids’ immunization records' },{'text': 'Can you fax my test results to my surgeon'}] ,
            'negativeExamples': [{'text':'I need to refill my prescription' },{'text': 'Do you have my test results?'} ] }  ]


# Create the task
put_result = crowd_client.put_task(function_name,
                                   task_name,
                                   {'text': text,
                                   'intents': intents })


print('PUT response: {}'.format(
    {'status_code': put_result.status_code, 'task': put_result.json()}))


# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'status_code': get_result.status_code, 'task': get_result.json()}))
