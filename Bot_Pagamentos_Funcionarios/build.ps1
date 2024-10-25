$exclude = @("venv", "Bot_Pagamentos_Funcionarios.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Bot_Pagamentos_Funcionarios.zip" -Force