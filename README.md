# LabJackInstallReady
Python script to autoinstall LabJack drivers and python libraries for full use.
Read the README text file for installation instructions.

#Instructions:
1. Turn on and log into your Raspberry Pi (default credentials for jessie OS is username: pi   Password: raspberry)
2. Make sure you have internet connection via ethernet cable or connect to a wifi network using the integrated wifi module.
3. Install git by runnin the following command without quotations ' sudo apt-get install -y git '
4. Now that git is installed pull the repo with the following command 'git clone https://github.com/xavidram/LabJackInstallReady.git'
5. change directory into the new folder 'cd LabJackInstallReady/'
6. python should be installed by default with the Jessie os for Raspberry Pi so run the install 'python setup.py'
7. the installer will run and install all binaries and drivers needed as well as the library for labjack python.
8. Reconnect the LabJack if you have it connected.

