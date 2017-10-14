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

list = [['named-entity-recognition', 'my-test-task-359b74a52b5e4446a7feb2ab4d97fd1a'],]
list.append(['named-entity-recognition', 'customer_review_1'])
list.append(['named-entity-recognition', 'customer_review_2'])
list.append(['named-entity-recognition', 'customer_review_3'])
list.append(['named-entity-recognition', 'customer_review_4'])
list.append(['named-entity-recognition', 'customer_review_5'])
list.append(['named-entity-recognition', 'customer_review_6'])
list.append(['named-entity-recognition', 'customer_review_7'])
list.append(['named-entity-recognition', 'customer_review_8'])
list.append(['named-entity-recognition', 'customer_review_9'])
list.append(['named-entity-recognition', 'customer_review_10'])




with open('image-categorization-inputs.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        task_name = row[0]
        get_result = crowd_client.get_task('image-categorization', task_name)

        print('GET response: {}'.format(
            {'status_code': get_result.status_code, 'api_name': 'image-categorization', 'task': get_result.json()}))

for row in list:
    function_name = row[0]
    task_name = row[1]
    get_result = crowd_client.get_task(function_name, task_name)

    print('GET response: {}'.format(
        {'status_code': get_result.status_code, 'api_name': function_name, 'task': get_result.json()}))
