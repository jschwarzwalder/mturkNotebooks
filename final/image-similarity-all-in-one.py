from mturk_crowd_beta_client import MTurkCrowdClient
from boto3.session import Session
import uuid

# This examples assume you have a local AWS profile called
# 'mturk-crowd-caller', but you can authenticate however you like,
# including by directly passing in your access key and secret key.
session = Session(profile_name='mturk-crowd-caller')

# Create the client
crowd_client = MTurkCrowdClient(session)

# For this example, we'll give your task a random, unique name.
# For prod tasks, you'll probably want to pick a name based on your input source.
# You will need to use this task_name to get your results.
task_name = 'my-test-task-' + uuid.uuid4().hex

# Next, we specify the name of the api to call
# In this example, we're first calling the image-similarity api which requires you to
# have prepurchased HITs to cover worker and mturk fees.
#
# The test api doesn't cost any money and is useful for validating that your account
# is setup correctly and for testing your integration.
#
# However the test api will return random sample results so can not be used beyond validating.
#
# If you want to use the test image-similarity api,
# uncomment the next line and comment out the image-similarity line
#
# function_name = 'image-similarity-test'
function_name = 'image-similarity'

# To request a result from the api, you need to specify task_name, function_name, and an input
# for image-similarity we pass in urls for two images.
# To make it easier to read the code we've created variables for the images we want to compare
image1 = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-a1.jpg'
image2 = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-g1.png'

# To create your request, we call put_task with your MTurkCrowdClient Session and pass in
# function_name, task_name, and your input.
put_result = crowd_client.put_task(function_name, task_name,
                                   {'image1': {'url': image1}, 'image2': {'url': image2} } )

# We print out the results so you can preview
print('Put Task response: {}'.format(
    {'api': function_name, 'status_code': put_result.status_code, 'task': put_result.json()}))


# Next we Get the task we just created. Note that since workers need to complete the task,
# we'd have to poll periodically until the task is submitted.
#
# To get results for a Taks you've created, update the task_name on line 16 and
# comment out lines 41, 42, 45 and 46 before you run this script again 
get_result = crowd_client.get_task(function_name, task_name)

# We print out the results so you can preview
print('Get Task response: {}'.format(
    {'api': function_name, 'status_code': get_result.status_code, 'task': get_result.json()}))

# A user can optionally delete a finished task (one whose state is either “completed” or “failed”).
# Note: Deleting a task that is still being processed (i.e., a task whose state is “processing”) is not allowed.
# To delete a completed task, uncomment the line below.
#
# crowd_client.delete_task(function_name, task_name)
