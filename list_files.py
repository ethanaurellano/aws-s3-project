import boto3

s3 = boto3.client('s3')
bucket_name = 'ethan-aws-s3-project'

response = s3.list_objects_v2(Bucket=bucket_name)

if 'Contents' in response:
    print(f'Files in {bucket_name}:')
    for obj in response['Contents']:
        print(f'  - {obj["Key"]} ({obj["Size"]} bytes)')
else:
    print('Bucket is empty')