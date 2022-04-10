---
title: "How to Configure a Raspberry Pi"
author: "Toni Czyrnik"
date: 2022-04-10
publishDate: 2022-04-11
lastmod: 2022-04-10

draft: false
hidden: false

categories:
  - Raspberry Pi
  - Coding

keywords:
  - Raspberry Pi
  - Headless Pi
  - Securing Raspberry Pi 
  - Coding
  - Digital Nomad


summary: Configuration of your Raspberry Pi: Passwordless SSH Access, Wireless Access Point, Backup and Restoring the SD Card
---

We will secure your Raspberry Pi, create a wireless access point and learn how backup the SD Card of the Raspberry Pi. 🤓

## Securing your Raspberry Pi

Please make sure, that your Overlay File System is deactivated and the boot partition writable. 

	sudo raspi-config

After you deactivated the Overlay File System, please reboot.

	sudo reboot

### Passwordless SSH Access

Please check, whether you have already created SSH Keys in the past. If there are files like "id_rsa.pub" or "id_dsa.pub", you don't need to generate new keys.

	ls ~/.ssh

#### Generate new SSH Keys

You can generate the keys with or without a passphrase using:

	ssh-keygen
	
You check them with this line:

	cat ~/.ssh/id_rsa.pub
	
#### Copy the Key to the Raspberry Pi

Now, you can transfer your Key to the Raspberry Pi using ssh.

	ssh-copy-id <USERNAME>@<IP-ADDRESS>

#### Storing the passphrase in the macOS keychain

You can store your passphrase in the macOS keychain using:

	ssh-add --apple-use-keychain ~/.ssh/id_rsa

#### Allow and Deny SSH Access

You can specify which users are allowed to use SSH using:

	sudo nano /etc/ssh/sshd_config

Append to the end of the file

	AllowUsers alice bob
	DenyUsers jane john

You can find all created users, which have a home directory:
	
	cat /etc/passwd | grep home

#### Using key-based authentication only

Let's make one additional adjustment, so only key-based authentication are allowed.

	sudo nano /etc/ssh/sshd_config

Search and edit the following:

	ChallengeResponseAuthentication no
	PasswordAuthentication no
	UsePAM no

## Wireless Access Point

If your WiFi is unreliable but you have access to an ethernet cable, you could try to set up a wireless access point with your Raspberry Pi!

You can read a great tutorial for setting up a Routed Wireless Access Point in the [official documentation](https://www.raspberrypi.com/documentation/computers/configuration.html#setting-up-a-routed-wireless-access-point).

## Backing up the SD Card

The most simple way to backup your Pi is coping all the files from the SD card. But creating an image is more reliable. You could store these files on your Mac or iCloud.

### Creating an image using macOS

Let's find the name of our SD card using

	diskutil list
	
Let's create the image

	sudo dd if=/dev/disk_name of=PiBackup.dmg
	
This takes a while and will save the image into your user directory.

### Restoring the image using macOS

Before we can restore a backup, we need to unmount the SD card.

	diskutil unmountDisk /dev/disk_name
	
Now, we can restore our backup image.

	sudo dd if=~/PiBackup.dmg of=/dev/disk_name
	
## Optional: Overlay File System

Changes made are not permanently during Overlay File System is activated. Everything that was changed will not be available once the Pi rebooted. Also, you can make your boot partition read only. That should increase your reliability of the system. But don't forget to disable it before starting your next project!

You will find the setting here:

	sudo raspi-config
	
Go to "Performance Options" and "Overlay File System".


## Conclusion 

That were a few first useful configurations for your Raspberry Pi! 

 

