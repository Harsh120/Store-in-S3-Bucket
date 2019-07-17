import os
import boto3
import mimetypes
from botocore.client import Config

def s3(): 
    ACCESS_KEY_ID = '' #Access key ID
    ACCESS_SECRET_KEY = '' #Access Secret key
    BUCKET_NAME = '' #Bucket name

    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )

    '''
        For the given path, get the List of all files in the directory tree 
    '''
    def getListOfFiles(dirName):
    # create a list of file and sub directories 
        # names in the given directory  
        listOfFile = os.listdir(dirName)
        allFiles = list()
        # Iterate over all the entries
        for entry in listOfFile:
            # Create full path
            fullPath = os.path.join(dirName, entry)
            # If entry is a directory then get the list of files in this directory 
            if os.path.isdir(fullPath):
                allFiles = allFiles + getListOfFiles(fullPath)
            else:
                allFiles.append(fullPath)
                    
        return allFiles      

    dirName = 'D:\Laravel\python' # Directory path, where all files are stored
        
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
        
    # Print the files
    for elem in listOfFiles:
        print(elem)
    
    print ("****************")
        
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
            
            
    # Print the files    
    for elem in listOfFiles:
        data = open(elem, 'rb')
        elem = elem.replace(dirName+'\\','')
        if elem.endswith('.php'):
            elem = os.path.splitext(elem)[0]+".html"  #Convert .php to .html
        mime_type = mimetypes.guess_type(elem)    
        
        elem = elem.replace('\\','/')
        print(elem)
       
        if mime_type[0]==None:
            s3.Bucket(BUCKET_NAME).put_object(Key='public/'+elem, Body=data, ACL='public-read', ContentType='text/plain')
        else:
            s3.Bucket(BUCKET_NAME).put_object(Key='public/'+elem, Body=data, ACL='public-read', ContentType=mime_type[0])
        print('Done') 
           
