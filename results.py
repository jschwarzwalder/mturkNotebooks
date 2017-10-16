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


# Next, we specify the name of the function to call

list = []

list.append(['co-reference-resolution','my-test-task-a8b19a88f51143a08726e9774e882bf1'])
list.append(['collect-utterance-text','say_something_1'])
list.append(['collect-utterance-text','say_something_2'])
list.append(['collect-utterance-text','say_something_3'])
list.append(['collect-utterance-text','say_something_4'])
list.append(['collect-utterance-text','say_something_5'])
list.append(['collect-utterance-text','say_something_6'])
list.append(['collect-utterance-text','say_something_7'])
list.append(['collect-utterance-text','say_something_8'])
list.append(['collect-utterance-text','say_something_9'])
list.append(['collect-utterance-text','say_something_10'])




with open('collect-text-utterance-inputs.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # print("")
        # print(row)
        task_name = row[0]
        list.append(['collect-utterance-text', task_name])



for row in list:
    function_name = row[0]
    task_name = row[1]
    get_result = crowd_client.get_task(function_name, task_name)

    print('GET response: {}'.format(
        {'status_code': get_result.status_code, 'api_name': function_name, 'task': get_result.json()}))
