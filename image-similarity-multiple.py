from mturk_crowd_beta_client import MTurkCrowdClient
from boto3.session import Session
import csv

# This examples assume you have a local AWS profile called
# 'mturk-crowd-caller', but you can authenticate however you like,
# including by directly passing in your access key and secret key.
session = Session(profile_name='mturk-crowd-caller')

# Create the client
crowd_client = MTurkCrowdClient(session)

# Next, we specify the name of the function to call
function_name = 'image-similarity'

with open('image-comparison-inputs.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        task_name = row[0]
        image1 = row[1]
        image2 = row[2]


        put_result = crowd_client.put_task(function_name,
                                            task_name,
                                            {'image1': {'url': image1}, 'image2': {'url': image2}})


        print('PUT response: {}'.format(
            {'status_code': put_result.status_code, 'task': put_result.json()}))



        get_result = crowd_client.get_task(function_name, task_name)

        print('GET response: {}'.format(
            {'status_code': get_result.status_code, 'task': get_result.json()}))
