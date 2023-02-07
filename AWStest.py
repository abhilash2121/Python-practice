import boto3
from boto3.dynamodb.conditions import Attr, Key

dynamodb = boto3.resource('dynamodb', region_name="eu-west-2")
table = dynamodb.Table("job_details")

# scan_kwargs = {"FilterExpression": Attr("model_version_name").eq("risk_auto_sum_1.0.1")}

params = {"KeyConditionExpression": Key("job_id").eq("100c")}
response = table.query(**params)

result = response["Items"]

print(result[0]["model_version_name"])
