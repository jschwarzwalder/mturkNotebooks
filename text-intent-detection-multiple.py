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
task_name = 'my-test-task-' + uuid.uuid4().hex

# Next, we specify the name of the function to call
function_name = 'text-intent-detection'

with open('text-intent-detection-inputs.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        task_name = row[0]
        text = row[1]

        # and an  intention, for worker to select.
        intents = [{'label': 'Borrow Car', 'description':'They want to borrow their parent\'s car tonight'},
                    {'label': 'Extension', 'description':'They want to ask the teacher for an extension on the due date'},
                    {'label': 'Keep Number', 'description':'They are switching phone companies and want to keep their old phone number'},
                    {'label': 'Make Appointment', 'description':'they are not feeling well, and call the doctor\'s office to schedule and appointment'},
                    {'label': 'Order', 'description':'They have a gluten allergy and want to know what items on the menu are safe to eat'},
                    {'label': 'Reference', 'description':'They are up for a promotion at work and want a co-worker to provide a reference'},
                    {'label': 'Return', 'description':'They want to return a phone or shirt'},
                    {'label': 'Update Address', 'description':'They have recently moved and want to update their address with the credit card company.'},
                    {'label': 'Understand Bill', 'description':'They recieved a bill with charges they do not recognize'} ]



        put_result = crowd_client.put_task(function_name,
                                           task_name,
                                           {'text': text,
                                           'intents': intents })


        print('PUT response: {}'.format(
            {'status_code': put_result.status_code, 'task': put_result.json()}))



        get_result = crowd_client.get_task(function_name, task_name)

        print('GET response: {}'.format(
            {'status_code': get_result.status_code, 'task': get_result.json()}))
