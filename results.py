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


# list.append(['bounding-box-test','my-test-task-80c4d16d84eb4b5b9558c8857d70ce62'])
# list.append(['bounding-box','my-test-task-df56af5706af4723a05e7193e522b0f4'])
# list.append(['collect-utterance-for-intent-test','my-test-task-2a1a6df4732e4d3394141a85f49168b8'])
# list.append(['collect-utterance-for-intent-test','my-test-task-1375d990f252493581dc2b20999a2f2f'])
# list.append(['collect-utterance-for-intent','my-test-task-778babbebbdc46b78246520e9126ae54'])
# list.append(['coreference-resolution-test','my-test-task-379e8ca2e09c40a4b75ed7ad2483053a'])
# list.append(['coreference-resolution','my-test-task-5d26ac02ca2f4f928920e32f1b69a47c'])
# list.append(['emotion-detection-test','my-test-task-7c616098a3f44704958f8d11279d1f87'])
# list.append(['emotion-detection','my-test-task-6883821856b647daa18966cb93385b9f'])
# list.append(['image-categorization-test','my-test-task-a1485055dfab4adf984de70b88778ca1'])
# list.append(['image-categorization-test','my-test-task-93afbb2c9c2f47e48c45ff3257827d65'])
# list.append(['image-categorization','my-test-task-ebcd3d3eb7d14408852fe46e29a83829'])
# list.append(['image-contains-test','my-test-task-8fc5acff3dbb4c988a5ba8803d5f57a8'])
# list.append(['image-similarity-test','my-test-task-e67b5a9c86d74287bbab305d1132292e'])
# list.append(['intent-detection-test','my-test-task-f8ee4fcb0c3849f3a5a78c143ce1157d'])
# list.append(['intent-detection', 'my-test-task-090e1a5b741a4736b15500a4b31598c5'])
# list.append(['intent-detection-test','my-test-task-68459b1eb22b4827a9eff10cebbb104b'])
# list.append(['intent-detection', 'my-test-task-6fae27f64ede4cefbb71c633ba4049a7'])
# list.append(['key-phrase-extraction-test','my-test-task-f20c954faa0f41f4a8f9ea3b4a824e58'])
# list.append(['key-phrase-extraction','my-test-task-385989de574a4f7fa750703b923d8296'])
# list.append(['named-entity-recognition-test','my-test-task-b87bacdffded4b92bb22b3a8a21596dd'])
# list.append(['named-entity-recognition','my-test-task-aaa462fd31ce485ca13c5f7a3a78206a'])
# list.append(['semantic-similarity-test','my-test-task-cd20cc01ba0845e7befddd0225b20f55'])
# list.append(['semantic-similarity','my-test-task-894c3a320188485dac368a3cd7ebd6e7'])
# list.append(['sentiment-analysis-test','my-test-task-ecea9113de1948f78a0091f1c891de89'])
# list.append(['sentiment-analysis','my-test-task-ab81e08e1f9343738b0a10663b2ae3c7'])
# list.append(['text-categorization-test','my-test-task-8330f9ae6243409caf869594d668e727'])
# list.append(['text-categorization','my-test-task-f65d5ee942ca4174b7b8c99e61e54278'])
# list.append(['text-categorization-test','my-test-task-e6c135a5d159443e9fd1fbc6e63f0160'])
# list.append(['text-categorization','my-test-task-90775c1de67e40159abcfea31c10b79c'])

list.append(['named-entity-recognition','my-test-task-7e55ccb771084c88bc13d1c46a1a84e1'])
list.append(['named-entity-recognition','my-test-task-39512a85fd784b82b5d8ebd1f19bc59c'])

with open('NER.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # print("")
        # print(row)
        task_name = row[0]
        list.append(['key-phrase-extraction', task_name + 'nkkey'])
        list.append(['named-entity-recognition', task_name + 'nnner'])
        list.append(['coreference-resolution', task_name + 'ncc'])

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
