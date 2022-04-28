#!/bin/bash

## create s3 bucket
for i in {1..10}
do
   aws s3api create-bucket --bucket "epam-$i" --region us-east-1
   aws s3 cp logging.json s3://epam-$i
done


## Enable versioning

aws s3 put-bucket-versioning --bucket epam-1 --versioning-configuration MFADelete=Disabled,Status=Enabled


##Enable Access logs

aws s3api put-bucket-logging --bucket epam-2 --bucket-logging-status file://logging.json
