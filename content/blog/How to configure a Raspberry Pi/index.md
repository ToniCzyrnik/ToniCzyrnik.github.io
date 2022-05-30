---
title: "How to Configure a Raspberry Pi"
author: "Toni Czyrnik"
date: 2022-04-10
publishDate: 2022-04-10
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

summary: "Configuration of your Raspberry Pi: Passwordless SSH Access, Wireless Access Point, Backup and Restoring the SD Card 🤓"
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

I used the following "hostapd.conf":

	#ctrl_interface=/var/run/hostapd
#ctrl_interface_group=0
interface=wlan0
driver=nl80211

	### IEEE 802.11
	ssid=YOUR__SSID
	wpa_passphrase=YOUR__PASSWORD
	# a = 5 GHz, g = 2.4 GHz
	hw_mode=a
	# 36 or 149
	channel=149
	# 1=wpa, 2=wep, 3=both
	auth_algs=1

	### DFS
	country_code=US
	# allowed channels and transmit power levels based on the regulatory limits
	ieee80211d=1
	# enables radar detection and DFS support
	ieee80211h=1

	### IEEE 802.11n
	ieee80211n=1
	require_ht=1
	ht_capab=[HT20][HT40+][SHORT-GI-20][SHORT-GI-40][DSSS_CCK-40]

	### IEEE 802.11ac
	ieee80211ac=1
	# 0 = 20 or 40 MHz operating Channel width
	# 1 = 80 MHz channel width
	# 2 = 160 MHz channel width
	# 3 = 80+80 MHz channel width
	vht_oper_chwidth=1
	# channel + 6 for 80 MHz
	# 42 or 155
	vht_oper_centr_freq_seg0_idx=155
	vht_capab=[SHORT-GI-80][MAX-MPDU-3895][SU-BEAMFORMEE]

	### IEEE 802.11i
	wpa=2
	wpa_key_mgmt=WPA-PSK
	rsn_pairwise=CCMP

	### WMM
	wmm_enabled=1
	uapsd_advertisement_enabled=1
	
	### logging
	# Module bitfield (-1 = all)
	# bit 0 (1) = IEEE 802.11
	# bit 1 (2) = IEEE 802.1X
	# bit 2 (4) = RADIUS
	# bit 3 (8) = WPA
	# bit 4 (16) = driver interface
	# bit 5 (32) = IAPP
	# bit 6 (64) = MLME
	
	# Levels (minimum value for logged events):
	#  0 = verbose debugging
	#  1 = debugging
	#  2 = informational messages
	#  3 = notification
	#  4 = warning

	logger_syslog=-1
	logger_syslog_level=4
	logger_stdout=-1
	logger_stdout_level=4

### Finding your channel

You can view possible channels with the following.

	iw list
	
	
Look at your current config
	
	iw dev

Depending on the chosen country, there are different frequencies possible. You can look on [wikipedia](https://en.wikipedia.org/wiki/List_of_WLAN_channels#5_GHz_(802.11a/h/j/n/ac/ax)).

	iw reg get

If you want to know what channels are busy in your environment, you need to install nmcli.

With this service, we get a list of available wifi networks.

	nmcli dev wifi
	
You can force a rescan:

	sudo nmcli dev wifi rescan

#### Installing  Network Management Command-Line Interface (nmcli)

Let's install it.

	sudo apt-get install network-manager

Now, you can start the service.

	sudo systemctl start NetworkManager.service 
	
But make sure, that it is not enabled!

	sudo systemctl disable NetworkManager.service

### Testing the Connection

You can test the connection speed between your computer and the Pi using iPerf.

#### Preparing the Raspberry Pi

Install iperf:

	sudo apt-get install iperf3

If you don't know the IP address of your pi. Use the following on your Raspberry Pi. 

	hostname -I

Let's start the server!
	
	iperf3 -s

#### Preparing the Mac

Install iperf:

	brew install iperf3

Run your mac as client:

	iperf3 -c IP_ADDRESS
	
#### Results

Now, you can see your network speed between your Mac and Raspberry Pi.

### Testing your internet with speedtest

You will find the official instruction [here](https://www.speedtest.net/en/apps/cli)

	sudo apt-get install curl
	
	curl -s https://install.speedtest.net/app/cli/install.deb.sh | sudo bash
	
	sudo apt-get install speedtest
	
## Backing up the SD Card

The most simple way to backup your Pi is coping all the files from the SD card. But creating an image is more reliable. You could store these files on your Mac or iCloud.

### Creating an image using macOS

Let's find the name of our SD card using

	diskutil list
	
Let's create the image. 

	sudo dd if=/dev/DISK_NAME status=progress | gzip -c > PiBackup.dmg.gz
	
This takes a while and will save the image into your user directory. The whole SD-card is copied and afterwards compressed.

### Restoring the image using macOS

Before we can restore a backup, we need to unmount the SD card.

	diskutil unmountDisk /dev/disk_name
	
Now, we can restore our backup image.

	zcat PiBackup.dmg.gz | dd of=/dev/disk_name
	
## Optional: Overlay File System

Changes made are not permanently during Overlay File System is activated. Everything that was changed will not be available once the Pi rebooted. Also, you can make your boot partition read only. That should increase your reliability of the system. But don't forget to disable it before starting your next project!

You will find the setting here:

	sudo raspi-config
	
Go to "Performance Options" and "Overlay File System".


## Conclusion 

That were a few first useful configurations for your Raspberry Pi!