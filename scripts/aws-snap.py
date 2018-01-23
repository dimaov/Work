#!/usr/bin/env python3
import argparse
import sys
import boto3
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(description="Manage instances' snapshots. You need to specife your access key, secret key and region in the ~/.aws/credentials file" )
parser.add_argument('--action', type=str, help="value can be: snasphot - takes snaphot from instance, clean - remove snapshot")
parser.add_argument('--ec2_tag', type=str, help="instance you want to take snapshot from")
parser.add_argument('--clean_time', type=str, help="expects a number of days. Snaphots older than this value will be removed")

args = parser.parse_args(sys.argv[1:])

if args.action == 'backup':
    ec2 = boto3.resource('ec2')
    print(args.ec2_tag)
    instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': ['%s' % args.ec2_tag]}])
    for instance in instances:
        ins = ec2.Instance('%s' % instance.id)
        vols = ins.volumes.all()
        for v in vols:
            snapshot = ec2.create_snapshot(VolumeId='%s' % v.id, Description="shapshot from %s for %s volume" % (instance.id,v.id))
            print("Snaphot has been taken successfuly")

if args.action == 'clean':
    ec2 = boto3.client('ec2')
    days = int(args.clean_time)
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])
    for snap in snapshots['Snapshots']:
         snap_created = snap['StartTime'].date()
         current_date = datetime.now().date()
         d = current_date - snap_created
         if d.days < days:
             id = snap['SnapshotId']
             ec2.delete_snapshot(SnapshotId=id)
