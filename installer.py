import urllib
import urllib.request
import tarfile
import os
import platform
import time
import shutil
import sys
from pathlib import Path

#detect operating system and find home folder
homedir = os.path.expanduser("~")

#operating system specific operations.
#we find the minecraft folder in this section.
if platform.system() == "Linux":
    print("Operating system detected: Linux")
    global mcfolder
    global modfolder
    os.chdir(homedir + '/.minecraft')
    mcfolder = Path.cwd()
    modfolder = homedir + '/.minecraft/mods'
    os.chdir(mcfolder)
    print("Changed current working directory to '" + str(mcfolder) + "'")
    time.sleep(2)

elif platform.system() == "Windows":
    print("Operating system detected: Windows")
    os.chdir(homedir)
    os.chdir("AppData")
    os.chdir("Roaming")
    os.chdir(".minecraft")
    mcfolder = Path.cwd()
    os.chdir("mods")
    modfolder = Path.cwd
    os.chdir(mcfolder) 
    print("Changed current working directory to '" + str(mcfolder) + "'")
    time.sleep(2)

os.chdir(mcfolder)

#begin mod backup and deletion
#THIS DOESN'T CURRENTLY BACK UP EXISTING MODS.
try:
    shutil.rmtree(str("mods"))
    print("Cleared previous mods.")
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))

os.mkdir(str("mods"))



#begin download and extract
#this snippet below defines a tar extract FUNCTION
def extract_tar_archive(tar_file_path, extract_to):
    with tarfile.open(tar_file_path, 'r') as tar:
        tar.extractall(extract_to)

print("Starting install...")

print("Fetching mods...")
#this is the SIMPLEST implementation of curl i have ever seen i just NUTTED SO FUCKING HARD
url = 'https://git.adolin.xyz/saru/lobotomy-mod-pack/raw/branch/main/mods.tar.gz'
urllib.request.urlretrieve(url, 'mods.tar.gz')

print("Extracting and writing to disk...")

tar_file_path = 'mods.tar.gz'
extract_to = 'mods'
extract_tar_archive(tar_file_path, extract_to)


print()
print()
print("      :+++++=")
print("      -++++++.")
print("      :++++++.               .")
print("      .++++++.             -=. -:           .::")
print("       =+++++.           :=.    =-       .--:. -")
print("       =+++++.          .+       =:     -=.    :=")
print("       =+++++.          +.     :.=*   .=:       =:")
print("       =++++=          .+      +. -- :+         .=")
print("      .+++++=          .=    ..=:    :.          =")
print("      .++=++-          .=   .+-                  =")
print("       ==++*=::..       *                        +")
print("       =*#-+- .:---:.   :=-- .-=%.  --=#-  ..::.--")
print("       :#=-*-     .::--:.*: .+ #@.  - *@@- .. -#:")
print("        ++:*.           .:--==:--::   .%%-.. :=.")
print("         =++.:...::::::..... :---+-:.  .:.: --")
print("                          *=..:::..        .=.")
print("                            :-.          .=:::")
print("                         ..:=.            :-..-:---:")
print("                        ==:-                 .=-:  :=-")
print("                        .=                      =-   :--.    .--")
print("                         --            :-:.      -=    .::::-:=.")
print("                         :-              =-      :+          .+")
print("                         ---            -:      .+           +.")
print("                           :=          -=      .+           =:")
print("                            +.         -:       =:        :=.")
print("                             -.        .=:      --.....::-:")
print("                            .=-     .=   :-:----- .::::.")
print("                          .-:        .=     ..+:")
print("                          -=......:.:-:+      :=")
print("                           .::--::...  :=      -")
print("                                        =:     =:")
print("                                         --::.--")
print("                                           ....")
#someone's gonna think im a furry or a femboy or some shit because of this.
print()

print("sigma")
print("all done!")
print("This script will exit and close in ten seconds. :)")
time.sleep(10)