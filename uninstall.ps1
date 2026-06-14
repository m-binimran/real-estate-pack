<#
.SYNOPSIS
  Remove real-estate-pack from a target workspace. Only deletes files it installed.
.EXAMPLE
  ./uninstall.ps1 -ProjectPath "C:\path\to\your\workspace"
#>
param(
  [Parameter(Mandatory = $true)]
  [string]$ProjectPath
)

$ErrorActionPreference = "Stop"
$src = $PSScriptRoot

if (-not (Test-Path $ProjectPath)) {
  throw "Project path not found: $ProjectPath"
}

Write-Host "Removing real-estate-pack from $ProjectPath" -ForegroundColor Cyan

Get-ChildItem (Join-Path $src "hooks\*.py") | ForEach-Object {
  $t = Join-Path $ProjectPath ".claude\hooks\$($_.Name)"
  if (Test-Path $t) { Remove-Item $t -Force }
}
Get-ChildItem (Join-Path $src "skills") -Directory | ForEach-Object {
  $t = Join-Path $ProjectPath ".claude\skills\$($_.Name)"
  if (Test-Path $t) { Remove-Item $t -Recurse -Force }
}
Get-ChildItem (Join-Path $src "loops\*.md") | ForEach-Object {
  $t = Join-Path $ProjectPath ".claude\commands\$($_.Name)"
  if (Test-Path $t) { Remove-Item $t -Force }
}
Get-ChildItem (Join-Path $src "commands\*.md") -ErrorAction SilentlyContinue | ForEach-Object {
  $t = Join-Path $ProjectPath ".claude\commands\$($_.Name)"
  if (Test-Path $t) { Remove-Item $t -Force }
}
Get-ChildItem (Join-Path $src "agents\*.md") | ForEach-Object {
  $t = Join-Path $ProjectPath ".claude\agents\$($_.Name)"
  if (Test-Path $t) { Remove-Item $t -Force }
}
Write-Host "  removed hooks, skills, commands, agents" -ForegroundColor Green

# Strip the appended rules block from CLAUDE.md (from our marker to end)
$claudeMd = Join-Path $ProjectPath "CLAUDE.md"
$marker = "<!-- ===== real-estate-pack rules (auto-installed) ===== -->"
if (Test-Path $claudeMd) {
  $content = Get-Content $claudeMd -Raw -Encoding UTF8
  $idx = $content.IndexOf($marker)
  if ($idx -ge 0) {
    ($content.Substring(0, $idx).TrimEnd() + "`n") | Set-Content $claudeMd -Encoding utf8 -NoNewline
    Write-Host "  stripped real-estate-pack rules from CLAUDE.md" -ForegroundColor Green
  } else {
    Write-Warning "Marker not found in CLAUDE.md; remove the real-estate-pack rules manually."
  }
}

# settings.json (only remove if it is exactly ours)
$settingsDest = Join-Path $ProjectPath ".claude\settings.json"
$settingsSrc = Join-Path $src "hooks\settings.json"
if (Test-Path $settingsDest) {
  $a = (Get-Content $settingsDest -Raw).Trim()
  $b = (Get-Content $settingsSrc -Raw).Trim()
  if ($a -eq $b) {
    Remove-Item $settingsDest -Force
    Write-Host "  removed .claude\settings.json (was real-estate-pack's)" -ForegroundColor Green
  } else {
    Write-Warning ".claude\settings.json has your own changes; remove the real-estate-pack 'hooks' block manually."
  }
}

Write-Host "Done. Restart Claude Code so the changes take effect." -ForegroundColor Cyan
