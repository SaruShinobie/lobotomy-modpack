import wget
import tarfile
import os
import platform
import time
import shutil
from pathlib import Path

#detect operating system and find home, minecraft, & mod folders
homedir = os.path.expanduser("~")
os.chdir(homedir)

# `global` sets these variables to exist outside of the scope of these specific `if` statements.
global mcfolder
global modfolder

if platform.system() == "Linux":
    print("Operating system detected: Linux")
    os.chdir(homedir + '/.minecraft')
    mcfolder = Path.cwd()
    modfolder = homedir + '/.minecraft/mods'
    os.chdir(mcfolder)
    print("Changed current working directory to '" + str(mcfolder) + "'")
    time.sleep(2)

elif platform.system() == "Windows":
    print("Operating system detected: Windows")
    os.chdir("AppData/Roaming/.minecraft/mods")
    mcfolder = Path.cwd()
    os.chdir("mods")
    modfolder = Path.cwd
    os.chdir(mcfolder) 
    print("Changed current working directory to '" + str(mcfolder) + "'")
    time.sleep(2)

os.chdir(mcfolder)

# delete previous mods
# WARN: THIS DOESN'T CURRENTLY BACK UP EXISTING MODS.
def del_dir():
    try:
        shutil.rmtree(str("mods"))
        print("Cleared previous mods.")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
del_dir()

os.mkdir(str("mods"))



# download mod archive from https://git.adolin.xyz/saru and extract
#this snippet below defines a tar extract FUNCTION
def extract_tar_archive(tar_file_path, extract_to):
    with tarfile.open(tar_file_path, 'r') as tar:
        tar.extractall(extract_to)

print("Starting install...")

print("Fetching mods...")
#  #this is the SIMPLEST implementation of curl i have ever seen i just NUTTED SO FUCKING HARD
# take the last one back, this is fucking insane. wget the fucking goat. who knew windows package manager was so damn cool?
wget.download('https://git.adolin.xyz/saru/lobotomy-mod-pack/raw/branch/main/mods.tar.gz')

print("Extracting and writing to disk...")

tar_file_path = 'mods.tar.gz'
extract_to = 'mods'
extract_tar_archive(tar_file_path, extract_to)

def ascii():
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
ascii()

print("sigma")
print("all done!")
print("This script will exit and close in ten seconds. :)")
time.sleep(10)