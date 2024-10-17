$exclude = @("venv", "GerenciamentoVeiculos.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "GerenciamentoVeiculos.zip" -Force