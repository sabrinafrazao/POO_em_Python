$exclude = @("venv", "Bot_Biblioteca.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Bot_Biblioteca.zip" -Force