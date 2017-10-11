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
function_name = 'image-categorization'

# The image we want labeled
image_url = 'https://requester.mturk.com/assets/simon.jpg'

# The type of thing we're looking for.
# Descriptions are optional, but help guide the worker.
label1 = 'Plant'
description1 =  'multicellular photosynthetic eukaryotes often refered to as green plants.'
label2 = 'Animal'
description2 =  'multicellular biological eukaryotes which includes vertebrates like fish, reptitles, birds and mammels, and invertebrates like worms and fruit flies.'
label3 = 'Bacteria'
description3 =  'small prokaryotic microorganisms about a few micrometers in length.'
label4 = 'Fungi'
description4 =  'eukayotic organisms such as yeasts and molds.'
label5 = 'Protists'
description5 =  'unicellular eukayotic organisms that often cluster together.'

# Create the task
put_result = crowd_client.put_task(function_name,
                                   task_name,
                                   {'image': {'url': image_url},
                                   'categories': [ {'label': label1,  "description":  description1 },
                                                   {'label': label2,  "description":  description2 },
                                                   {'label': label3,  "description":  description3 },
                                                   {'label': label4,  "description":  description4 },
                                                   {'label': label5,  "description":  description5 }] })


print('PUT response: {}'.format(
    {'status_code': put_result.status_code, 'task': put_result.json()}))


# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'status_code': get_result.status_code, 'task': get_result.json()}))
