#!/usr/bin/python
# import sys, os, glob, time, boto
# from boto.s3.connection import S3Connection
# from boto.s3.key import Key
import boto3

print ('Senthil how are you...')

# dev = boto.session.Session(profile_name='senthil.ryde')
s3 = boto3.resource('s3')
# print (dev)
# AWS_ACCESS =
# AWS_SECRET =
#
# conn = S3Connection(AWS_ACCESS,AWS_SECRET)
# bucket = conn.get_bucket('be.wapptastic')
# directory = '/home/pi/Programs/'
#
# def percent_cb(complete, total):
#     sys.stdout.write('.')
#     sys.stdout.flush()
#
# def getFiles(dir):
# 	return [os.path.basename(x) for x in glob.glob(str(dir) + '*.jpg')]
#
# def upload_S3(dir, file):
# 	k = Key(bucket)
# 	k.key = f
# 	# k.set_contents_from_filename(dir + f, cb=percent_cb, num_cb=10)
#
#
# # filenames = getFiles(directory)
# # print filenames
#
# for f in filenames:
#         print 'rnUploading %s to Amazon S3 bucket %s' % (f, bucket)
# 	upload_S3(directory, f)
#         removeLocal(directory, f)
