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
# In this example, we're first calling the image-categorization-test function.
# The test function doesn't cost any money and is useful for validating that your account is setup correctly and for testing your integration.
# To call the prod image-categorization function, uncomment the next line and comment out the image-categorization-test line
# function_name = 'image-categorization'
function_name = 'image-categorization-test'

# The image we want labeled
image_url = 'https://requester.mturk.com/assets/simon.jpg'

# The type of thing we're looking for
label1 = 'Plant'
label2 = 'Animal'
label3 = 'Bacteria'
label4 = 'Fungi'
label5 = 'Protists'

# Create the task
put_result = crowd_client.put_task(function_name,
                                   task_name,
                                   {'image': {'url': image_url},
                                   'categories': [ {'label': label1},
                                                   {'label': label2},
                                                   {'label': label3},
                                                   {'label': label4},
                                                   {'label': label5}] })


print('PUT response: {}'.format(
    {'status_code': put_result.status_code, 'task': put_result.json()}))


# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'status_code': get_result.status_code, 'task': get_result.json()}))
