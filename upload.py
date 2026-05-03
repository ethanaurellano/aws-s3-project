import boto3

s3 = boto3.client('s3')

bucket_name = 'ethan-aws-s3-project'
file_name = 'hello.txt'

with open(file_name, 'w') as f:
    f.write('My first AWS upload!')

s3.upload_file(file_name, bucket_name, file_name)

print(f'Successfully uploaded {file_name} to {bucket_name}')