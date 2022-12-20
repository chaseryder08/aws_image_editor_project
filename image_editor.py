from watchfiles import watch
from pathlib import Path
import sys
import boto3 


PROJ_DIR = Path(sys.argv[0]).absolute().parent
IMG_DIR = Path(PROJ_DIR, "images")
NEW_IMG_DIR = Path(PROJ_DIR, "new_images")

while True:
    
    for change in watch(IMG_DIR):
        # changes set to list - set = list but every item is unique*
        path = Path(list(change)[0][1])
                     
        # Boto3 upload to S3
        s3 = boto3.client('s3')
             
        # TO DO: file uploads, but need to have new img saved in new_image folder   
        with open(path, 'rb') as f:
            s3.upload_fileobj(f, "image-editor-bucket", path.name)
        
        print("success!")


           
 