#!/usr/bin/python
import sys, os, glob, time, boto3, urllib2, StringIO
from boto3.s3.transfer import S3Transfer

AWS_BUCKET = "senthil-raspi-carpark-space"
directory = 'basin-reserve/'
session = boto3.Session(profile_name='senthil.ryde')
s3client = session.resource('s3')
s3putclient = session.client('s3')
bucket = s3client.Bucket(AWS_BUCKET)
#print (bucket)
#sourceurl = 'http://202.142.12.41/snapshotJPEG?Resolution=640x480&Quality=Clarity'
sourceurl = 'http://192.168.1.69:81/videostream.cgi?user=admin&pwd=Jose1001&resolution=32&rate=0'

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
