#!/bin/bash

echo "################"
echo SCRIPT STARTING
echo "################"

#template
#printf "${process0}"\\r;
#zip;
#printf "${process0} \e[32m[DONE!]\e[0m"

moddir="~/.minecraft"
cd ${moddir}



process0="Backing up existing mod folder..."
printf "${process0}"\\r;
zip -r -q ./mods/.mod-folder-backup.zip mods && printf "${process0} \e[32m[DONE!]\e[0m"
#i didnt even know `zip` as a standalone command existed.
#this needs to be a tar.gz archive.
echo
sleep 1

process1="Removing old mods..."
printf "${process1}"\\r;
sudo rm /home/$USER/.minecraft/mods/* && printf "${process1} \e[32m[DONE!]\e[0m"
echo
sleep 1



moddir="/home/$USER/.minecraft/mods"
cd ${moddir}



process2="Downloading mod package..."
printf "${process2}"\\r;
sudo curl http://192.168.7.208:420/api/shares/YxMjU3N/files/e641be0e-bccd-4f3d-8a86-7dbbb8f88263 -O -J -L -s && printf "${process2} \e[32m[DONE!]\e[0m"
#what the fuck?
#how does this work?
#fix this.
echo
sleep 1


process3="Extracting package..."
printf "${process3}"\\r;
unzip -q mod-archive.zip;
printf "${process3} \e[32m[DONE!]\e[0m"
echo
sleep 1

#yes this is all for show it looks cool shut up
printf "Finalizing"\\r; sleep 1; printf "Finalizing."\\r; sleep 1; printf "Finalizing.."\\r; sleep 1; printf "Finalizing..."\\r; sleep 1;printf "Finalizing... \e[32m[DONE!]\e[0m";
echo
sleep 1
echo Exiting...
sleep 4

#god bash is so much nicer than windows CMD scripts
exit
