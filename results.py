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

# list.append(['co-reference-resolution','my-test-task-3e7723884f424076a6db5446a0f3a2de'])
# list.append(['co-reference-resolution','my-test-task-850e2da9234147b8b0851e5e8bc51ca2'])
# list.append(['co-reference-resolution', 'my-test-task-4fa8706d75164531839c74813b82b058'])
list.append(['co-reference-resolution', 'my-test-task-77fc9a6cbaee49d1867c1871f3eb5e8c'])
list.append(['key-phrase-extraction', 'my-test-task-7f57fd7f17ee47399012f6cd514ee282'])
# # list.append(['key-phrase-extraction', 'customer_review_3k'])
# # list.append(['key-phrase-extraction', 'customer_review_4k'])
# list.append(['key-phrase-extraction', 'customer_review_5ke'])
# list.append(['key-phrase-extraction', 'customer_review_6ke'])
# # list.append(['key-phrase-extraction', 'customer_review_7k'])
# # list.append(['key-phrase-extraction', 'customer_review_8k'])
# # list.append(['key-phrase-extraction', 'customer_review_9k'])
# list.append(['key-phrase-extraction', 'customer_review_10ke'])
list.append(['named-entity-recognition', 'my-test-task-32433536f6964355944d5b5c5ac69b75'])
# list.append(['named-entity-recognition', 'customer_review_2n'])
# list.append(['named-entity-recognition', 'customer_review_3n'])
# # list.append(['named-entity-recognition', 'customer_review_4n'])
# list.append(['named-entity-recognition', 'customer_review_5n'])
# list.append(['named-entity-recognition', 'customer_review_6n'])
# list.append(['named-entity-recognition', 'customer_review_7n'])
# list.append(['named-entity-recognition', 'customer_review_8n'])
# list.append(['named-entity-recognition', 'customer_review_9n'])
# # list.append(['named-entity-recognition', 'customer_review_10n'])

# list.append(['collect-utterance-text','say_something_0d'])
# list.append(['collect-utterance-text','say_something_11c'])
# list.append(['collect-utterance-text','say_something_12a'])
# list.append(['collect-utterance-text','say_something_14a'])
# list.append(['collect-utterance-text','say_something_14d'])
# list.append(['collect-utterance-text','say_something_15b'])
# list.append(['collect-utterance-text','say_something_15c'])
# list.append(['collect-utterance-text','say_something_16d'])
# list.append(['collect-utterance-text','say_something_17c'])
# list.append(['collect-utterance-text','say_something_18a'])
# list.append(['collect-utterance-text','say_something_18c'])



# with open('collect-text-utterance-inputs.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         # print("")
#         # print(row)
#         task_name = row[0]
#         list.append(['collect-utterance-text', task_name])
#         list.append(['key-phrase-extraction', task_name + 'k'])
#         list.append(['key-phrase-extraction', task_name + 'ke'])
#         list.append(['named-entity-recognition', task_name])
#         list.append(['named-entity-recognition', task_name + 'a'])
#         list.append(['named-entity-recognition', task_name + 'n'])
#
# with open('nlp-input-1.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         # print("")
#         # print(row)
#         task_name = row[0]
#         list.append(['key-phrase-extraction', task_name])
#
with open('text-intent-detection-inputs.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # print("")
        # print(row)
        task_name = row[0]
        list.append(['text-intent-detection', task_name])

for row in list:
    function_name = row[0]
    task_name = row[1]
    get_result = crowd_client.get_task(function_name, task_name)

    print('GET response: {}'.format(
        {'status_code': get_result.status_code, 'api_name': function_name, 'task': get_result.json()}))
