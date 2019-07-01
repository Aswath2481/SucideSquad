REM %1 command line argument
if "%1%"=="stop" ( 
taskkill /f /im engine.exe
)
if "%1"=="start" (
tasklist /nh /fi "imagename eq engine.exe"|find /i "engine.exe">nul&&(
taskkill /f /im engine.exe
START "" "%programfiles%\sucidesquad\engine.exe"
)||(
START "" "%programfiles%\sucidesquad\engine.exe"
))