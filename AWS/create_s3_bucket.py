import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-boto3-bucket-abs', CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})