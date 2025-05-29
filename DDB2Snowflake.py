from datetime import datetime
import pandas as pd
import boto3
from io import StringIO

def handle_insert(record):
    print("Handling Insert: ", record)
    data_dict = {}

    for key, value in record['dynamodb']['NewImage'].items():
        for data_type, column_value in value.items():
            data_dict[key] = column_value

    dff = pd.DataFrame([data_dict])
    return dff

def lambda_handler(event, context):
    print("Received event:", event)

    # Safely handle missing 'Records' key
    if 'Records' not in event:
        print("No 'Records' key found. Exiting Lambda.")
        return {
            'statusCode': 400,
            'body': "Invalid event format. 'Records' key missing."
        }

    df_list = []

    for record in event['Records']:
        if record['eventName'] == "INSERT":
            df_insert = handle_insert(record)
            df_list.append(df_insert)
            table = record['eventSourceARN'].split("/")[1]  # assuming all records from same table

    if df_list:
        final_df = pd.concat(df_list, ignore_index=True)
        all_columns = list(final_df)
        final_df[all_columns] = final_df[all_columns].astype(str)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{table}_{timestamp}.csv"
        s3_key = f"snowflake/{filename}"
        print("Generated S3 key:", s3_key)

        csv_buffer = StringIO()
        final_df.to_csv(csv_buffer, index=False)

        s3 = boto3.client('s3')
        bucketName = "wrt-bkt1"

        s3.put_object(Bucket=bucketName, Key=s3_key, Body=csv_buffer.getvalue())

        print(f"Successfully processed {len(df_list)} INSERT records and saved to S3.")
        return {
            'statusCode': 200,
            'body': f"Processed {len(df_list)} records and saved to {s3_key}."
        }

    else:
        print("No INSERT records found.")
        return {
            'statusCode': 204,
            'body': "No records to process."
        }
