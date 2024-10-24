@echo off

cd /D "%~dp0"

set root="%USERPROFILE%\AppData\Roaming\.minecraft"
set modfolder="%USERPROFILE%\AppData\Roaming\.minecraft\mods"
set cusdate=M%DATE:~4,2%D%DATE:~7,2%Y%DATE:~10,4%

echo "################"
echo SCRIPT STARTING
echo "################"
echo.
    @timeout /t 1 >nul 2>&1

echo Updating Mods...
    cd /d %root%

    curl -k "https://git.adolin.xyz/saru/lobotomy-mod-pack/raw/branch/main/mods.tar.gz" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Prefer: safe" -H "Alt-Used: git.adolin.xyz" -H "Connection: keep-alive" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Authorization: token ***REMOVED***" -o mods.tar.gz


    Compressing and backing up existing mods...
    tar -czf mods-backup-%cusdate%.tar.gz mods/
    @timeout /t 2 >nul 2>&1

    Deleting existing mods...
    @RD /S /Q mods
    @MD mods

    @timeout /t 2 >nul 2>&1
    
    tar -xvzf mods.tar.gz -C %modfolder%

echo Sigma!
echo All done.
    @timeout /t 10 >nul 2>&1
exit