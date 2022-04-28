## Python function for S3 bucket creation with required properties

### Boto3 APIs used in the function:
    1. create_bucket :- to create the bucket
    2. BucketVersioning :- to enable the versions in s3 buckets
    3. put_bucket_logging :- to enable the Access logs in bucket

### Resources Created
    1. 10 s3 buckets with prefix "epam-test"
    2. 1 bucket has versioning enabled!
    3. 1 of the bucket has access log enabled!
    4. 1 bucket is public


