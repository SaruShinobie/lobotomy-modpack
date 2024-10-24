@echo off

cd /D "%~dp0"

set mcroot="%USERPROFILE%\AppData\Roaming\.minecraft"
set modfolder="%USERPROFILE%\AppData\Roaming\.minecraft\mods"
set cusdate=M%DATE:~4,2%D%DATE:~7,2%Y%DATE:~10,4%

echo "################"
echo SCRIPT STARTING
echo "################"
echo.
    @timeout /t 1 >nul 2>&1

cd /d %mcroot%

echo Downloading latest fabric installer...
    curl -k "https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.1/fabric-installer-1.0.1.exe" -o fabricinstaller.exe
    start /WAIT "%mcroot%" fabricinstaller.exe

echo Updating Mods...

    curl -k "https://git.adolin.xyz/saru/lobotomy-mod-pack/src/commit/07dba1b0ab21e3a764f9e31c82fe459e6ab0b133/mods.tar.gz" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Prefer: safe" -H "Alt-Used: git.adolin.xyz" -H "Connection: keep-alive" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Authorization: token ***REMOVED***" -o mods.tar.gz


    echo Compressing and backing up existing mods...
    tar -czf %mcroot%/mods-backup-%cusdate%.tar.gz %modfolder%
    @timeout /t 2 >nul 2>&1

    echo Deleting existing mods...
    @RD /S /Q mods
    @MD mods

    @timeout /t 2 >nul 2>&1
    
    tar -xvzf %mcroot%/mods.tar.gz -C %mcroot%

echo Sigma!
echo All done.
    @timeout /t 10 >nul 2>&1
exit
