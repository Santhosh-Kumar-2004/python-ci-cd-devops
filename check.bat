@echo off
echo Running flake8...
flake8 .
IF %ERRORLEVEL% NEQ 0 EXIT /B %ERRORLEVEL%

echo Running pytest...
pytest
IF %ERRORLEVEL% NEQ 0 EXIT /B %ERRORLEVEL%

echo All checks passed!
