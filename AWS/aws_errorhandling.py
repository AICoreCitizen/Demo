#Import Python Modules 
import boto3

# Error Handling and Exception Handling with boto3

#*****************************************

# Some of the most common errors are:

# botocore.exceptions.NoCredentialsError: Raised when valid AWS credentials are not found
# botocore.exceptions.ParamValidationError: Raised when input parameters provided to boto3 methods are invalid or do not meet the required constraints
# botocore.exceptions.ClientError: A general exception representing errors returned by the AWS service. It includes information such as the HTTP status code, error code, and error message.

#******************************************

# Example


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

