from pprint import pprint
import pandas as pd
import boto3
import json
from botocore.exceptions import ClientError

client = boto3.client('resourcegroupstaggingapi', )
df=pd.DataFrame({'ResourceARN':[],'Key':[],'Value':[]})    
client = boto3.client('resourcegroupstaggingapi', region_name='ap-southeast-2')
paginator = client.get_paginator('get_resources')
pages= paginator.paginate()
for page in pages:
    resources=page['ResourceTagMappingList']
    for resource in resources:
        arn=resource.get('ResourceARN')
        for i,tags in enumerate(resource.get('Tags')):
            if i==0:
                
                df.loc[len(df.index)]=[arn,tags['Key'],tags['Value']]
            else:
                df.loc[len(df.index)]=['',tags['Key'],tags['Value']]
        
df.to_csv('Outputfiletest.csv')

    