#!/bin/bash

echo "Initialization script started"

sudo bash -c 'echo 192.168.30.2 master >> /etc/hosts'

cd

TARGET_PARTITIONS=$(awk '{print $4}' /proc/partitions | sed -e '/name/d' -e '/^$/d' -e '/loop[0-9]?/d' -e '/[1-9]/!d')
POINT="point"
DATA="data"
#MINSIZE=10000000
MINSIZE=300000
mkdir $POINT
for device in $TARGET_PARTITIONS; do
  echo "Trying $device..."
  #sudo mount /dev/$device $POINT -o uid=ubuntu,gid=ubuntu && \
  #    echo "Successfully mounted $device" || (echo "Failed to mount $device"; continue)
  sudo mount /dev/$device $POINT -o uid=ubuntu,gid=ubuntu && \
      echo "Successfully mounted $device" || continue
  size=$(df -k $POINT | awk '{print $4}' | tail -1)
  echo "$device have $size K bytes free"
  if [ $size -gt $MINSIZE ]; then
    tmpdir=$(mktemp -d --tmpdir=$POINT tmp`date +%s`.XXXXXXXXXX)
    ln -s $tmpdir $DATA
    echo "Using $tmpdir on $device for files storage"
    echo
    break
  else
    sudo umount $POINT
  fi
  echo
done

if [ ! -e $DATA ]; then
  echo "Device with enough free space not found!"
  exit 1
fi

echo "Copying data..."
cp -R /cluster/data/* $DATA/

echo "Setting up Hadoop environment..."
. $DATA/hadoop_env.sh

echo "Setting up SSH..."
. $DATA/setup_ssh.sh

echo "Setting up symbolic links for configuration..."
rm -rf $DATA/hadoop/conf/
ln -s /cluster/data/hadoop/conf $DATA/hadoop/conf

echo "Register at master server..."
ip=$(ifconfig eth0 | awk '/inet addr/ {split ($2,A,":"); print A[2]}')
echo "IP: $ip"
ssh master "bash -c \"echo $ip >> data/hadoop/conf/slaves.new\""

echo "All done!"
