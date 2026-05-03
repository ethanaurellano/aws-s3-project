import boto3

s3 = boto3.client('s3')
bucket_name = 'ethan-aws-s3-project'
file_name = 'hello.txt'
download_path = 'downloaded_hello.txt'

s3.download_file(bucket_name, file_name, download_path)

print(f'Downloaded {file_name} from {bucket_name} to {download_path}')

with open(download_path, 'r') as f:
    print(f'File contents: {f.read()}')