import os, subprocess

#install essentials and base tools
subprocess.call(["sudo" , "apt-get" , "-y" , "update"])
subprocess.call(["sudo" , "apt-get" , "-y" , "upgrade"])
subprocess.call(["sudo" , "apt-get" , "install" , "libusb-1.0" , "git"])

#pull git repositories
#exo driver first
subprocess.call(["git" , "clone" , "https://github.com/labjack/exodriver.git"])
subprocess.call(["python" , "exodriver/setup.py"])
#labjackpython library
subprocess.call(["git" , "clone" , "https://github.com/labjack/LabJackPython.git"])
subprocess.call(["python" , "LabJackPython/setup.py"])

#setup complete.