#Import Python Modules 
import boto3


#Copying, moving, and deleting S3 objects

s3 = boto3.client('s3')
# copy
s3.copy_object(Bucket='my-bucket', Key='new-folder/file.txt', CopySource='my-bucket/folder/file.txt')
# move
s3.move_object(Bucket='my-bucket', Key='new-folder/file.txt', CopySource='my-bucket/folder/file.txt')
# delete
s3.delete_object(Bucket='my-bucket', Key='folder/file.txt')