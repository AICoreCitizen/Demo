
#Import Python Modules 
import boto3

# """Python SDK for AWS - This script is used to interactwith S3 Objects using boto3 """
# # Creating a S3 Bucket using boto3 - use create_bucket() method 
# s3 = boto3.client('s3')
# s3.create_bucket(Bucket='my-boto3-bucket-abs', CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})



# # Uploading Objects to S3 Buckets - use the upload_file() method
# s3 = boto3.client('s3')
# s3.upload_file('E:/CompSkills/Cloud/AWS/BucketPolicies.txt', 'my-boto3-bucket-abs', 'policies/Bucketpolicies.txt')

#In the example above, '/Users/maya/Downloads/cloud-meme.jpeg' represents the local path to the file I wanted to upload to the S3 bucket, 'my-boto3-bucket-abs' is the S3 bucket name and 'policies/Bucketpolicies.txt' is the object key.
#If we now inspect the 'my-boto3-bucket-abs', we can see that running the code above uploaded the desired object to the S3 bucket, and has also create the policies folder to which the object was uploaded.


# Downloading Objects from S3 Buckets - use the download_file() method 
s3 = boto3.client('s3')
s3.download_file('my-boto3-bucket-abs', 'policies/Bucketpolicies.txt', 'E:/CompSkills/Cloud/AWS/Downloads/BucketPolicies.txt')

# In the example above, 'my-boto3-bucket-maya' is the S3 bucket name, 'memes/cloud-meme.jpeg' is the object key and
# '/Users/maya/Downloads/new-cloud-meme.jpeg' represents the local path at which we want to save the S3 object.








