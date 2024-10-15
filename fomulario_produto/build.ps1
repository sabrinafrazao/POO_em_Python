$exclude = @("venv", "fomulario_produto.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "fomulario_produto.zip" -Force