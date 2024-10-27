@echo off

set mcroot="%USERPROFILE%\AppData\Roaming\.minecraft"
set modfolder="%USERPROFILE%\AppData\Roaming\.minecraft\mods"
set cusdate=%DATE:~4,2%-%DATE:~7,2%-%DATE:~10,4%

echo "################"
echo SCRIPT STARTING
echo "################"
echo.
    @timeout /t 1 >nul 2>&1


echo Downloading latest fabric installer...
    cd %mcroot%
    curl -k "https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.1/fabric-installer-1.0.1.exe" -o fabricinstaller.exe
    ECHO ###### !!!!! ######
    echo MAKE SURE YOU PICK THE CURRENT SERVER MINECRAFT VERSION, 1.20.1
    echo You only need to change the minecraft version, don't worry about the launcher version option.
    ECHO ###### !!!!! ######
    start /WAIT "%mcroot%" fabricinstaller.exe


echo Updating...
    cd /d %mcroot%

    curl -k "https://git.adolin.xyz/saru/lobotomy-mod-pack/raw/branch/main/mods.tar.gz" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "DNT: 1" -H "Sec-GPC: 1" -H "Alt-Used: git.adolin.xyz" -H "Connection: keep-alive" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Sec-Fetch-User: ?1" -H "Priority: u=0, i" -H "TE: trailers" -H "Authorization: token ***REMOVED***" -o mods.tar.gz

    echo Compressing and backing up existing mods...
    tar -czf %mcroot%/mods-backup-%cusdate%.tar.gz %modfolder%
        @timeout /t 2 >nul 2>&1

    echo Deleting existing mods...
    rmdir /S /Q mods
    mkdir mods
        @timeout /t 2 >nul 2>&1
    
    tar -xvzf %mcroot%/mods.tar.gz -C %modfolder%
:::
:::            へ   ♡   ╱|、
:::      ૮  -   ՛ )      (`   -  7
:::        /   ⁻  ៸|       |、⁻〵
:::  乀 (ˍ, ل ل      じしˍ,)ノ
:::

for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A)
echo Sigma!
echo All done. C:
echo .
echo This window will close in ten seconds.
    @timeout /t 10 >nul 2>&1
exit
