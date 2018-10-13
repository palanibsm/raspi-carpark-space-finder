#!/usr/bin/python
import sys, os, glob, time, boto3

session = boto3.Session(profile_name='senthil.ryde')
s3client = session.resource('s3')
s3putclient = session.client('s3')
bucket = s3client.Bucket('senthil-raspi-carpark-space')
#print (bucket)

directory = '/basinreserve/'

def list_bucket_contents(bucket):
   for object in bucket.objects.all():
      print (object.key)

def put_object_into_s3(s3putclient):
   response = s3putclient.put_object(
      ACL='private',
      Bucket='senthil-raspi-carpark-space',
      Body='<h1>Hello Senthil</h1>',
      Key='basin-reserve/index.html'
   )
   
   print (response)

 
list_bucket_contents(bucket)
put_object_into_s3(s3putclient)
