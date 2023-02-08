import boto3
from boto3.dynamodb.conditions import Attr, Key


abc = False
dynamodb = boto3.resource('dynamodb', region_name="eu-west-2")
table = dynamodb.Table("job_details")

scan_kwargs = {"FilterExpression": Attr("model_version_name").eq("risk_auto_sum_1.0.1")}

response = table.scan(**params)

result = response["Items"]

for i in result:
    print(i)
