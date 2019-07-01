; -- 64Bit.iss --
; Demonstrates installation of a program built for the x64 (a.k.a. AMD64)
; architecture.
; To successfully run this installation and the program it installs,
; you must have a "x64" edition of Windows.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=Sucide Squad beta
AppVersion=1.11
WizardStyle=modern
DefaultDirName={autopf}\Sucidesquad
DefaultGroupName=Sucidesquad
UninstallDisplayIcon={app}\MyProg.exe
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Inno Setup Examples Output
OutputBaseFilename=sucidesquad_beta_v1.11
; "ArchitecturesAllowed=x64" specifies that Setup cannot run on
; anything but x64.
ArchitecturesAllowed=x64
; "ArchitecturesInstallIn64BitMode=x64" requests that the install be
; done in "64-bit mode" on x64, meaning it should use the native
; 64-bit Program Files directory and the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64
    
[Files]
Source: "C:\Users\Zero\Desktop\sucidesquad\dist\spawnshield.exe"; DestDir: "{app}"; DestName: "spawnshield.exe"
Source: "C:\Users\Zero\Desktop\sucidesquad\dist\engine.exe"; DestDir: "{app}"; DestName: "engine.exe"
Source: "C:\Users\Zero\Desktop\sucidesquad\dist\core.exe"; DestDir: "{app}"; DestName: "core.exe"
Source: "C:\Users\Zero\Desktop\sucidesquad\dist\e_start.lnk"; DestDir: "{win}"; DestName: "e_start.lnk"
Source: "C:\Users\Zero\Desktop\sucidesquad\dist\e_stop.lnk"; DestDir: "{win}"; DestName: "e_stop.lnk"
Source: "C:\Users\Zero\Desktop\sucidesquad\dist\readme.txt"; DestDir: "{app}"; DestName: "readme.txt"; Flags:isreadme

[Icons]
Name: "{group}\Sucide Squad"; Filename: "C:\Users\Zero\Desktop\sucidesquad\img\setup.png"
Name: "{userstartup}\Engine"; Filename: "{app}\engine.exe"

[Registry]
Root: HKCR; Subkey: "Directory\Background\shell\Protect this folder\command"; ValueType: string; ValueName: ""; ValueData: "{app}\spawnshield.exe"
Root: HKCR; Subkey: "Directory\Background\shell\Protect this folder\"; Flags: uninsdeletekey