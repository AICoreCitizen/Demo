# %%
#Import Python Modules 
import boto3

# %%
# Uploading Objects to S3 Buckets - use the upload_file() method
s3 = boto3.client('s3')
s3.upload_file('E:/CompSkills/Cloud/AWS/cert-overview.jpg', 'second-bucket-abs', 'cert-overview.jpg')

#Error Handling

from botocore.exceptions import NoCredentialsError, ClientError

try:
    # Boto3 code that may raise exceptions
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    
    # Process the response or perform other operations
    print(response)

except NoCredentialsError:
    print("AWS credentials not found. Please configure your credentials.")

except ClientError as e:
    if e.response['Error']['Code'] == 'NoSuchBucket':
        print("The specified bucket does not exist.")
    else:
        print("An error occurred:", e)
# %%
