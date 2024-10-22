$exclude = @("venv", "AluguelVeiculo.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "AluguelVeiculo.zip" -Force