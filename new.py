import io
import datetime
import boto3
import pandas as pd
from xlrd.book import open_workbook_xls


def read_output_from_s3(s3_client, model_output_path, model_inference_timestamp=None, start_time=None, end_time=None):
    bucket_name, key = model_output_path.split("/", 3)[2:]
    bucket = s3_client.Bucket(bucket_name)
    for file in bucket.objects.filter(Prefix=key):
        data = None
        if str(file.key).upper().endswith(".XLSX"):
            data = read_xlsx_from_s3(file)
    return data


def read_xlsx_from_s3(file_object):
    excel_body = file_object.get()["Body"].read()
    # dataframe = pd.read_excel(io.BytesIO(excel_body))
    workbook = open_workbook_xls(file_contents=excel_body)
    return workbook


def filter_data(data, start_time, end_time, model_inference_timestamp):
    filtered_data = data.loc[
        (data[model_inference_timestamp] >= start_time) & (
                data[model_inference_timestamp] < end_time)]
    data = filtered_data.to_dict()
    return data


s3_client = boto3.resource("s3", region_name="us-east-1")
model_output_path = "s3://tri-dana-test-bucket/risk-auto-sum/ML Expense Forecast Jan23.xlsx"
model_inference_timestamp = "Date"
start_time = "2023-01-01"
end_time = "2023-02-02"
res = read_output_from_s3(s3_client, model_output_path, model_inference_timestamp, start_time, end_time)
print(res)
