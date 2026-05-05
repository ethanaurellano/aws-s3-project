# AWS S3 File Manager

A Python project that interacts with Amazon S3 using boto3.

## What it does
- Uploads files to an S3 bucket
- Lists all files in the bucket
- Downloads files from the bucket

## AWS Services used
- **S3** — stores the files
- **IAM** — manages permissions for the scripts

## Prerequisites
- Python 3.8+
- An AWS account
- AWS CLI installed

## Setup

### 1. Install dependencies
```bash
pip install boto3
```

### 2. Configure AWS credentials
aws configure

### 3. Run the scripts
python upload.py
python list_files.py
python download_file.py

MIT License
