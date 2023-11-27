# %%
#Import Python Modules 
import boto3

"""Python SDK for AWS - This script is used to interactwith S3 Objects using boto3 """
# Creating a S3 Bucket using boto3 - use create_bucket() method 
s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-boto3-bucket-abs', CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})


# %%
# Uploading Objects to S3 Buckets - use the upload_file() method
s3 = boto3.client('s3')
s3.upload_file('E:/CompSkills/Cloud/AWS/BucketPolicies.txt', 'my-boto3-bucket-abs', 'policies/Bucketpolicies.txt')

#In the example above, '/Users/maya/Downloads/cloud-meme.jpeg' represents the local path to the file I wanted to upload to the S3 bucket, 'my-boto3-bucket-abs' is the S3 bucket name and 'policies/Bucketpolicies.txt' is the object key.
#If we now inspect the 'my-boto3-bucket-abs', we can see that running the code above uploaded the desired object to the S3 bucket, and has also create the policies folder to which the object was uploaded.

# %%
# Downloading Objects from S3 Buckets - use the download_file() method 
s3 = boto3.client('s3')
s3.download_file('my-boto3-bucket-abs', 'policies/Bucketpolicies.txt', 'E:/CompSkills/Cloud/AWS/Downloads/BucketPolicies.txt')

# In the example above, 'my-boto3-bucket-maya' is the S3 bucket name, 'memes/cloud-meme.jpeg' is the object key and
# '/Users/maya/Downloads/new-cloud-meme.jpeg' represents the local path at which we want to save the S3 object.

# %%


#Copying, moving, and deleting S3 objects

s3 = boto3.client('s3')
# copy
s3.copy_object(Bucket='my-bucket', Key='new-folder/file.txt', CopySource='my-bucket/folder/file.txt')
# move
s3.move_object(Bucket='my-bucket', Key='new-folder/file.txt', CopySource='my-bucket/folder/file.txt')
# delete
s3.delete_object(Bucket='my-bucket', Key='folder/file.txt')


# %%

# Error Handling and Exception Handling with boto3

#*****************************************

# Some of the most common errors are:

# botocore.exceptions.NoCredentialsError: Raised when valid AWS credentials are not found
# botocore.exceptions.ParamValidationError: Raised when input parameters provided to boto3 methods are invalid or do not meet the required constraints
# botocore.exceptions.ClientError: A general exception representing errors returned by the AWS service. It includes information such as the HTTP status code, error code, and error message.

#******************************************

# Example

import boto3
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

