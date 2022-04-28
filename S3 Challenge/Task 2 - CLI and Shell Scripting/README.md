## Configuring AWS CLI with secret key and secret access key
    aws configure

## Script execution steps

### Script for s3 bucket creation
    vim s3.sh

### Changing Script File Permissions
     chmod 700 s3.sh

### Executing the script
sh s3.sh
 
### Command For Uploading Data in each Bucket

 aws s3 cp sample.mp4 s3://epam-1

### To make object public
 aws s3 cp sample1.mp4 s3://epam-10 --acl public-read
