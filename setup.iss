#define AppVersion GetEnv('LSG_VERSION')
[Setup]
AppId={{C831F464-2732-4CB1-B89E-EC24A7CFAE38}
AppName=London Session Guide
AppVersion={#AppVersion}
DefaultDirName={localappdata}\Programs\LondonSessionGuide
DefaultGroupName=London Session Guide
PrivilegesRequired=lowest
OutputDir=installer
OutputBaseFilename=LondonSessionGuide_Setup
Compression=lzma2
SolidCompression=yes
CloseApplications=yes
RestartApplications=no
UninstallDisplayIcon={app}\LondonSessionGuide.exe
[Files]
Source: "dist\LondonSessionGuide.exe"; DestDir: "{app}"; Flags: ignoreversion
[Icons]
Name: "{autoprograms}\London Session Guide"; Filename: "{app}\LondonSessionGuide.exe"
Name: "{autodesktop}\London Session Guide"; Filename: "{app}\LondonSessionGuide.exe"
[Run]
Filename: "{app}\LondonSessionGuide.exe"; Description: "Open London Session Guide"; Flags: nowait postinstall skipifsilent; Check: not IsAppUpdate; BeforeInstall: ResetFrozenAppEnvironment

Filename: "{app}\LondonSessionGuide.exe"; Flags: nowait; Check: IsAppUpdate; BeforeInstall: ResetFrozenAppEnvironment
[Code]
{ When Setup is launched by a PyInstaller onefile executable, it inherits
  the old _PYI_APPLICATION_HOME_DIR from that instance. Reset the environment
  just before [Run] starts the freshly installed executable. }
function SetEnvironmentVariableW(lpName: string; lpValue: string): Boolean;
  external 'SetEnvironmentVariableW@kernel32.dll stdcall';

procedure ResetFrozenAppEnvironment;
begin
  if not SetEnvironmentVariableW('PYINSTALLER_RESET_ENVIRONMENT', '1') then
    RaiseException('Could not reset the application launch environment.');
end;

function IsAppUpdate: Boolean;
begin
  Result := (ExpandConstant('{param:LSGUPDATE|0}') = '1') or
            (ExpandConstant('{param:LSGUPDATE|0}') = '2');
end;

function InitializeSetup(): Boolean;
begin
  Result := True;
  { The old v1.0.2 updater launches Setup before its own process exits.
    Give it time to close and release the running EXE on this first upgrade. }
  if ExpandConstant('{param:LSGUPDATE|0}') = '1' then
    Sleep(8000);
end;
