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

list.append(['intent-detection-test','my-test-task-f8ee4fcb0c3849f3a5a78c143ce1157d'])
list.append(['bounding-box-test','my-test-task-80c4d16d84eb4b5b9558c8857d70ce62'])
list.append(['collect-utterance-for-intent-test','my-test-task-1375d990f252493581dc2b20999a2f2f'])
list.append(['coreference-resolution-test','my-test-task-379e8ca2e09c40a4b75ed7ad2483053a'])
list.append(['emotion-detection-test','my-test-task-7c616098a3f44704958f8d11279d1f87'])
list.append(['image-categorization-test','my-test-task-a1485055dfab4adf984de70b88778ca1'])
list.append(['image-contains-test','my-test-task-8fc5acff3dbb4c988a5ba8803d5f57a8'])
list.append(['image-similarity-test','my-test-task-e67b5a9c86d74287bbab305d1132292e'])
list.append(['key-phrase-extraction-test','my-test-task-f20c954faa0f41f4a8f9ea3b4a824e58'])
list.append(['named-entity-recognition-test','my-test-task-b87bacdffded4b92bb22b3a8a21596dd'])
list.append(['semantic-similarity-test','my-test-task-cd20cc01ba0845e7befddd0225b20f55'])
list.append(['sentiment-analysis-test','my-test-task-ecea9113de1948f78a0091f1c891de89'])
list.append(['text-categorization-test','my-test-task-8330f9ae6243409caf869594d668e727'])




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
# with open('nlp-input-3.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         # print("")
#         # print(row)
#         task_name = row[0]
#         list.append(['co-reference-resolution', task_name])

# with open('image-categorization-inputs.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         # print("")
#         # print(row)
#         task_name = row[0]
#         list.append(['image-categorization', task_name])

for row in list:
    function_name = row[0]
    task_name = row[1]
    get_result = crowd_client.get_task(function_name, task_name)

    print('GET response: {}'.format(
        {'status_code': get_result.status_code, 'api_name': function_name, 'task': get_result.json()}))
