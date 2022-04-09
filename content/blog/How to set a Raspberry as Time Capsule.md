---
title: "How to set a Raspberry as Time Capsule (MacOS)"
author: "Toni Czyrnik"
date: 2022-03-31
publishDate: 2022-04-08
lastmod: 2022-04-01

draft: false
hidden: True

categories:
  - Raspberry Pi
  - Coding

keywords:
  - Raspberry Pi
  - Remote
  - Student
  - Tallinn

summary:
---


# How to set a Raspberry as Time Capsule (MacOS)

## Setup Raspberry Pi

	
## Prepare the external drive

We need a hard drive that uses the HFS+ or APFS System. Otherwise, we cannot use it for Time Machine.

Currently, there's only a reliable read-only version for APFS on linux. So, we are going to use HFS+ instead. 

Don't forget to give read and write permissions for everyone using "get info".

### Mount Disk

sudo apt-get install hfsprogs

lsblk -f

create moint point

sudo mkdir -p /TM

sudo mount -t hfsplus -o force,rw /dev/sda2 /TM

sudo nano /etc/fstab

PARTUUID="2db15007-b5b1-4054-9b9b-b4fe7c3d7294" /TM     hfsplus force,rw,user,auto        0       0

## Prepare Time Machine

### Install Samba and avahi

sudo apt-get install samba avahi-daemon

### create user 

sudo adduser timemachine

choose a password for the new user on your pi

### Configure Samba

sudo smbpasswd -a timemachine

sudo nano /etc/samba/smb.conf

[Time Machine]
    comment = Backups
    path = /TM
    valid users = timemachine
    read only = no
    vfs objects = catia fruit streams_xattr
    fruit:time machine = yes
    
sudo service smbd reload

### configure Avahi

sudo nano /etc/avahi/services/samba.service

<?xml version="1.0" standalone='no'?><!--*-nxml-*-->
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
  <name replace-wildcards="yes">%h</name>
  <service>
    <type>_smb._tcp</type>
    <port>445</port>
  </service>
  <service>
    <type>_device-info._tcp</type>
    <port>9</port>
    <txt-record>model=TimeCapsule8,119</txt-record>
  </service>
  <service>
    <type>_adisk._tcp</type>
    <port>9</port>
    <txt-record>dk0=adVN=Time Machine,adVF=0x82</txt-record>
    <txt-record>sys=adVF=0x100</txt-record>
  </service>
</service-group>

sudo service avahi-daemon reload


## Make the Pi read only!

https://core-electronics.com.au/tutorials/read-only-raspberry-pi.html