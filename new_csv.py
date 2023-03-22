import csv
from datetime import datetime
import boto3

s3_client = boto3.resource("s3", region_name="us-east-1")


def read_model_output_from_s3(s3_client,
                              model_output_location,
                              model_inference_timestamp,
                              start_time,
                              end_time):
    bucket_name, key = model_output_location.split("/", 3)[2:]
    bucket = s3_client.Bucket(bucket_name)
    data_list = []
    for file in bucket.objects.filter(Prefix=key):
        if str(file.key).upper().endswith(".CSV"):
            data = read_csv_files_s3(file)
        if data:
            for item in data:
                if model_name == item["model_name"] and model_version == item["model_version"]:
                    data_list.append(item)
            filtered_data = list(filter(lambda item: (format_timestamp(start_time) <= format_timestamp(
                item[model_inference_timestamp]) < format_timestamp(end_time)
                                                      ), data))
    return filtered_data


def format_timestamp(timestamp: str):
    return datetime.strptime(timestamp, "%m-%d-%Y")


def read_csv_files_s3(file):
    csv_body = file.get()["Body"].read().decode('utf-8').split('\r')
    dict_reader_object = csv.DictReader(csv_body)
    # list_of_dictionary = list(dict_reader_object)
    return dict_reader_object


def final_output(model_output, model_inference_unique_feature, model_inference_target_feature,
                 ground_truth_target_feature=None):
    all_records = []
    gt_records = []
    for model_prediction in model_output:
        to_append = {
            "modelOutputGuid": model_prediction[model_inference_unique_feature],
            "model_output": model_prediction[model_inference_target_feature],
            "ground_truth": model_prediction[model_inference_target_feature]
        }
        if ground_truth_target_feature and len(model_prediction[ground_truth_target_feature]) != 0:
            to_append["ground_truth"] = model_prediction[ground_truth_target_feature]
            gt_records.append(to_append)

        all_records.append(to_append)
    preprocess_data = {"all_rec": (all_records, len(all_records)), "gt": (gt_records, len(gt_records))}
    return preprocess_data


def upload_data_on_s3(s3_client, merged_data, output_path):
    bucket_name, _ = output_path.split("/", 3)[2:]


model_output_location = "s3://tri-dana-test-bucket/risk-auto-sum/Actuals2.csv"
model_inference_timestamp = "Date"
# ground_truth_timestamp = "Date2"
start_time = "01-01-2023"
end_time = "01-02-2023"
model_inference_unique_feature = "unique"
model_inference_target_feature = "doc amt"
ground_truth_target_feature = "doc amt1"
model_output = read_model_output_from_s3(s3_client, model_output_location, model_inference_timestamp, start_time,
                                         end_time)
print(model_output)
processing_data_gt_all_rec = final_output(model_output, model_inference_unique_feature, model_inference_target_feature,
                                          ground_truth_target_feature)
