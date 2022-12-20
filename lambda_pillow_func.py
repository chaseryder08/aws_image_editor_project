import json
import urllib.parse
from PIL import Image
from io import BytesIO
import boto3

print('Loading function')

#TODO: need to learn how to install pillow lib on lambda
# NOTE: follow youtube vid, found pillow package, zipped file, added layer to lambda
# Now gettinge error : 

{
  "errorMessage": "Unable to import module 'lambda_function': cannot import name '_imaging' from 'PIL' (/opt/python/PIL/__init__.py)",
  "errorType": "Runtime.ImportModuleError",
  "stackTrace": []
}

s3 = boto3.client('s3')


def lambda_handler(event, context):
    print(event)
    print(context)
    
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    print(bucket)
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print(key)
    try:
        file_byte_string = s3.get_object(Bucket=bucket, Key=key)['Body'].read()
        print(file_byte_string)
        image = Image.open(BytesIO(file_byte_string))
        MAX_SIZE = (165, 165)
        
        # creating thumbnail
        image.thumbnail(MAX_SIZE) 
        
        # store image in memory
        in_mem_file = io.BytesIO()
        image.save(in_mem_file, format=image.format)
        in_mem_file.seek(0)
        thumb_bucket = 't'
        
        # Upload image to s3
        s3.upload_fileobj(
            in_mem_file, # This is what i am trying to upload
            "thumbnail-image-editor",
            "thumb" + key,
            ExtraArgs={
                'ACL': 'public-read'
            }
        )
    
        print('Put Complete!')
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
        
