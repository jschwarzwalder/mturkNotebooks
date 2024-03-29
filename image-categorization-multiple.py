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

with open('image-categorization-inputs.csv') as f:
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
        description1 = 'Closed toe shoe that covers entire foot up to ankle'
        description2 = 'Closed toe shoe that covers entire foot and leg up to knee'
        description3 = 'Closed toe shoe that covers foot and has no heel'
        description4 = 'Open toe shoe that connects to foot through a single strap'
        description5 = 'Open toe shoe that connects to foot through straps'
        description6 = 'Closed toe shoe with no back on the heel of wear\'s foot'
        description7 = 'Heeled shoe where sole is in the form of a wedge'

        # Create the task
        put_result = crowd_client.put_task(function_name,
                                           task_name,
                                           {'image': {'url': image_url},
										    'categories': [ {'label': label1,  'description':  description1 },
                                                   {'label': label2,  'description':  description2 },
                                                   {'label': label3,  'description':  description3 },
                                                   {'label': label4,  'description':  description4 },
                                                   {'label': label5,  'description':  description5 },
                                                   {'label': label6,  'description':  description6 },
                                                   {'label': label7,  'description':  description7 }] })


        print('PUT response: {}'.format(
            {'status_code': put_result.status_code, 'task': put_result.json()}))


        # Get the task we just created. Note that for a prod (i.e., non-test) task,
        # we'd have to poll periodically until the task completed.
        get_result = crowd_client.get_task(function_name, task_name)

        print('GET response: {}'.format(
        {'status_code': get_result.status_code, 'task': get_result.json()}))
