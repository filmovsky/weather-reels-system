python -m venv venv

.\venv\Scripts\Activate.ps1

pip install --upgrade pip

pip install -r requirements.txt

playwright install

Write-Host ""
Write-Host "Environment ready."
Write-Host "Next steps:"
Write-Host "1. scripts\start_worker.ps1"
Write-Host "2. scripts\start_scheduler.ps1"
Write-Host "3. scripts\start_api.ps1"