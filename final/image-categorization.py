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

# The image we want identified
image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1m.png'

# The type of thing we're looking for
# Descriptions amd example images are optional, but help guide the worker.
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
example1_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1d.jpg'
example2_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1z.jpg'
example3_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1dd.png'
example4_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1b.png'
example5_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1r.png'
example6_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1x.png'
example7_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1l.png'
example1b_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1i.jpg'
example2b_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1f.jpg'
example3b_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1y.png'
example4b_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1l.jpg'
example5b_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1q.jpg'
example6b_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1t.png'
example7b_image_url = 'https://s3-us-west-2.amazonaws.com/mturk-sample-media/images-to-compare/image-similarity-1i.png'

# Create the task
put_result = crowd_client.put_task(function_name,
                                   task_name,
                                   {'image': {'url': image_url},
                                   'categories': [ {'label': label1,  'description':  description1 ,
                                                    'positiveExamples': [{'image': {'url': example1_image_url}}] ,
                                                    'negativeExamples': [{'image': {'url': example1b_image_url}}] },
                                                   {'label': label2,  'description':  description2,
                                                    'positiveExamples': [{'image': {'url': example2_image_url}}] ,
                                                    'negativeExamples': [{'image': {'url': example2b_image_url}}]  },
                                                   {'label': label3,  'description':  description3,
                                                    'positiveExamples': [{'image': {'url': example3_image_url}}] ,
                                                    'negativeExamples': [{'image': {'url': example3b_image_url}}]  },
                                                   {'label': label4,  'description':  description4,
                                                    'positiveExamples': [{'image': {'url': example4_image_url}}] ,
                                                    'negativeExamples': [{'image': {'url': example4b_image_url}}]  },
                                                   {'label': label5,  'description':  description5,
                                                      'positiveExamples': [{'image': {'url': example5_image_url}}] ,
                                                      'negativeExamples': [{'image': {'url': example5b_image_url}}]  },
                                                   {'label': label6,  'description':  description6,
                                                      'positiveExamples': [{'image': {'url': example6_image_url}}] ,
                                                      'negativeExamples': [{'image': {'url': example6b_image_url}}]  },
                                                   {'label': label7,  'description':  description7,
                                                    'positiveExamples': [{'image': {'url': example7_image_url}}] ,
                                                    'negativeExamples': [{'image': {'url': example7b_image_url}}]  }] })

print('PUT response: {}'.format(
    {'status_code': put_result.status_code, 'task': put_result.json()}))


# Get the task we just created. Note that for a prod (i.e., non-test) task,
# we'd have to poll periodically until the task completed.
get_result = crowd_client.get_task(function_name, task_name)

print('GET response: {}'.format(
{'status_code': get_result.status_code, 'task': get_result.json()}))
