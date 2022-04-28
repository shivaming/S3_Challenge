import boto3
import settings

client = boto3.client('s3',
		aws_access_key_id='settings.Access_Key_Id',
		aws_secret_access_key='settings.Secret Access_Key_Id',
		region_name=settings.AWS_REGION)


location = {'LocationConstraint': AWS_REGION}
for i in range(10):
  bucket_name="epam-{}".format(i)
  response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
  response_public = client.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        },
    )



#Uploading objects in Buckets

client.upload_file(Filename='Path of the File', Bucket='epam-1', Key='Filename')


#Bucket Versioning

s3 = boto3.resource('s3')
versioning = s3.BucketVersioning('epam-1')
versioning.enable()


# To enable public access


client.upload_file(Filename='Path of the File', Bucket='epam-5', Key='Filename',settings.ExtraArgs)


# Bucket Logging

logging = client.put_bucket_logging(
Bucket='epam-2',
BucketLoggingStatus={
       'LoggingEnabled': {
         'TargetBucket': 'epam-2',
         'TargetPrefix': 'epam-2' + '/logs/'
        }
})
