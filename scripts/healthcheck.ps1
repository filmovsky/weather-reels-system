Write-Host "Checking Python..."
python --version

Write-Host "Checking pip..."
pip --version

Write-Host "Checking Redis..."
redis-cli ping

Write-Host "Checking project structure..."
Test-Path "..\app"
Test-Path "..\config"
Test-Path "..\storage"

Write-Host "Healthcheck completed."