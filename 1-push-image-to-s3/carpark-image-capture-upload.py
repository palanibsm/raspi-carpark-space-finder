#!/usr/bin/python
import sys, os, glob, time, boto3, urllib2, StringIO
from boto3.s3.transfer import S3Transfer

AWS_BUCKET = "senthil-raspi-carpark-space"
directory = 'basinreserve/'
session = boto3.Session(profile_name='senthil.ryde')
s3client = session.resource('s3')
s3putclient = session.client('s3')
bucket = s3client.Bucket(AWS_BUCKET)
#print (bucket)
sourceurl = 'https://images.freeimages.com/images/large-previews/bd7/falloxbow-1058032.jpg'



# def list_bucket_contents(bucket):
#    for object in bucket.objects.all():
#       print (object.key)
#
def put_object_into_s3(s3putclient):

   # file_path = "abcd.txt"
   file_object = urllib2.urlopen(sourceurl)
   fp = StringIO.StringIO(file_object.read())

   response = s3putclient.put_object(
      ACL='public-read',
      Bucket=AWS_BUCKET,
      Body=fp,
      Key=directory + 'carpark.jpg'
   )
   print (response)

   # transfer = S3Transfer(s3putclient)
   # transfer.upload_file(file_path, AWS_BUCKET, file_path)

   #print (response)

# list_bucket_contents(bucket)
put_object_into_s3(s3putclient)
