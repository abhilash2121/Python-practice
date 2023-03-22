import boto3
from boto3.dynamodb.conditions import Attr, Key
from typing import Optional
from pydantic import BaseModel, validator


class PydanticBase(BaseModel):
    @validator("*")
    def check_sum(cls, v):
        if v == "":
            raise ValueError("Value cannot be an empty string")
        return v

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ModelDetails(PydanticBase):
    records_processed: str
    status: str
    test: Optional[str]


class Test(PydanticBase):
    ground_truth_records_processed: int
    model_version_name: str
    execution_id: str
    created: str
    is_adhoc: bool
    job_id: str
    model_details: Optional[ModelDetails]
    modified: str


dynamodb = boto3.resource('dynamodb', region_name="eu-west-2")
table = dynamodb.Table("job_details")

scan_kwargs = {"FilterExpression": Attr("model_version_name").eq("risk_auto_sum_1.0.1")}

response = table.scan(**scan_kwargs)

result = response["Items"]

results = result[0]

snapshot_obj = Test(**results)

print(snapshot_obj.model_details.test)

assert snapshot_obj.model_details.test
