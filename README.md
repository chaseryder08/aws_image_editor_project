# AWS Lambda/S3 Thumbnail Image Editor Project
![This is an image](/image_editor.png)

For my internship with Cloud City Architects, I designed this project to automate an image editing/upload process, which uses Python to upload an image to AWS S3, and then triggers AWS Lambda to create a thumbnail of the image, and then upload to a separate S3 bucket. 

This project helps streamline the process of creating and storing new thumbnail images on AWS, resulting in saved time and improved efficiency of processes for the customer.

## The Infrastructure

To initialize the process, I wrote a python script that uses the 'watchfiles' library to check for changes/uploads to a folder, then uses 'Boto3' to upload the photo to an S3 bucket (this runs as a background windows process). Once it is uploaded, an S3 trigger event initializes the lambda function which then uses 'Pillow' to change the image to a thumbnail, and then upload it to a separate bucket specifically for thumbnail images.
