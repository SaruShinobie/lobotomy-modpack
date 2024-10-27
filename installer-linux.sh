#!/bin/bash
# shebang!

echo "################"
echo SCRIPT STARTING
echo "################"

# template
# printf "${process0}"\\r;
# zip;
# printf "${process0} \e[32m[DONE!]\e[0m"

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
sudo curl -k "https://git.adolin.xyz/saru/lobotomy-mod-pack/raw/branch/main/mods.zip" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "DNT: 1" -H "Sec-GPC: 1" -H "Alt-Used: git.adolin.xyz" -H "Connection: keep-alive" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Sec-Fetch-User: ?1" -H "Priority: u=0, i" -H "TE: trailers" -H "Authorization: token ***REMOVED***" -o mods.tar.gz -O -J -L -s && printf "${process2} \e[32m[DONE!]\e[0m"
# fixed!
echo
sleep 1

process3="Extracting package..."
printf "${process3}"\\r;
unzip -q mod-archive.zip;
    # HATE. that this still uses a zip archive. need to replace with a tarball.
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
