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
# In this example, we're first calling the co-reference-resolution-test function.
# The test function doesn't cost any money and is useful for validating that your account is setup correctly and for testing your integration.
# To call the prod co-reference-resolution function, uncomment the next line and comment out the co-reference-resolution-test line
# function_name = 'co-reference-resolution'
function_name = 'co-reference-resolution-test'

# We ask the worker to find all expressions that refer to the same entity in a text
text = 'For the home or professional bread-maker, this is the book . It comes from a man many consider to be the best bread baker in the United States: Chad Robertson, co-owner of Tartine Bakery in San Francisco, a city that knows its bread. To him, bread is the foundation of a meal, the center of daily life, and each loaf tells the story of the baker who shaped it. He developed his unique bread over two decades of apprenticeship with the finest artisan bakers in France and the United States, as well as experimentation in his own ovens. Readers will be astonished at how elemental it is. A hundred photographs from years of testing, teaching, and recipe development provide step-by-step inspiration, while additional recipes provide inspiration for using up every delicious morsel.'


# Create the task
put_result = crowd_client.put_task(function_name,
                                   task_name,
                                   {'text': text,})


print('PUT response: {}'.format(
    {'status_code': put_result.status_code, 'task': put_result.json()}))


# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
# Since we are running a test, this will return mock results. s
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'api-name': function_name, 'note': 'SAMPLE RESULTS ONLY', 'status_code': get_result.status_code, 'task': get_result.json()}))
