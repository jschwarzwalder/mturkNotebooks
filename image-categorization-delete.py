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
function_name = 'image-categorization'

with open('shoes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        task_name = row[0]
        image_url = row[1]

        # The type of thing we're looking for.
        # Descriptions are optional, but help guide the worker.
        label1 = 'Ankle Boot'
        label2 = 'Knee High Boot'
        label3 = 'Ballet Flats'
        label4 = 'Flip Flops'
        label5 = 'Sandal'
        label6 = 'Mule'
        label7 = 'Wedge'

        # Create the task
        delete_result = crowd_client.delete_task(function_name,task_name)
