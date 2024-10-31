import wget
import tarfile
import os
import platform
import time
import shutil
from pathlib import Path



#define some functions ahead of time
def delete_directory(directory):
    try:
        shutil.rmtree(str(directory))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
#this defines a function to delete a directory (no shit)

def extract_tar_archive(tar_file_path, extract_to):
    with tarfile.open(tar_file_path, 'r') as tar:
        tar.extractall(extract_to)
#this defines a function to decompress a tar.gz file

def ascii_art():
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
    print()
#someone's gonna think im a furry or a femboy or some shit because of this.



#detect operating system and find home, minecraft, & mod folders
homedir = os.path.expanduser("~")
os.chdir(homedir)

global mcfolder
global modfolder
    # `global` sets these variables to exist outside of the scope of these specific `if` statements.

if platform.system() == "Linux":
    print("Operating system detected: Linux")
    os.chdir('/.minecraft')
    mcfolder = Path.cwd()
    modfolder = mcfolder + '/mods'

elif platform.system() == "Windows":
    print("Operating system detected: Windows")
    os.chdir("AppData/Roaming/.minecraft/mods")
    mcfolder = Path.cwd()
    modfolder = mcfolder + '/mods'


os.chdir(mcfolder) 
print("Changed current working directory to '" + str(mcfolder) + "'")
time.sleep(2)



#clear out preexisting mods
delete_directory("mods")
print("Deleted mod folder contents.")
os.mkdir(str("mods"))



# download mod archive from https://git.adolin.xyz/saru and extract
print("Starting install...")
print("Fetching mods...")
wget.download('https://git.adolin.xyz/saru/lobotomy-mod-pack/raw/branch/main/mods.tar.gz')
    #  #this is the SIMPLEST implementation of curl i have ever seen i just NUTTED SO FUCKING HARD
    # take the last one back, this is fucking insane. `wget` the fucking goat. who knew windows package manager was so damn cool?

print("Extracting and writing to disk...")

extract_tar_archive('mods.tar.gz', 'mods')
    #              ('tarfile', 'directory to extract to')

ascii_art()
    #call func to print ascii art to console

print("sigma!")
print("all done!")
print("This script will exit and close in ten seconds. :)")
time.sleep(10)