import argparse
import os
import sys

from dotenv import load_dotenv

from yc_client import YandexCloudClient

parser = argparse.ArgumentParser()
parser.add_argument(
    "-lfp",
    "--local-file-path",
    help="Full path to the file to be uploaded",
)
parser.add_argument(
    "-sfp",
    "--s3-file-path",
    help="Full path to file to be uploaded in S3",
)
args = parser.parse_args()

if __name__ == "__main__":
    # Загружаем переменные из .env файла
    load_dotenv()
    
    # Берем креды из .env с правильными именами переменных
    bucket_name = os.environ.get("STUDENT_S3_BUCKET")
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    
    # Проверяем что все переменные найдены
    if not bucket_name:
        print("ERROR: STUDENT_S3_BUCKET not found in .env file")
        sys.exit(1)
    if not aws_access_key_id:
        print("ERROR: AWS_ACCESS_KEY_ID not found in .env file")
        sys.exit(1)
    if not aws_secret_access_key:
        print("ERROR: AWS_SECRET_ACCESS_KEY not found in .env file")
        sys.exit(1)
    
    print(f"Using bucket: {bucket_name}")
    
    client = YandexCloudClient(
        bucket_name=bucket_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    client.upload_file(
        local_file_path=args.local_file_path,
        s3_file_path=args.s3_file_path,
    )
    print(f"File {args.local_file_path} uploaded to S3://{bucket_name}/{args.s3_file_path}")