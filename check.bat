@echo off
echo Starting checks...
echo Running flake8...
flake8 .
@REM IF %ERRORLEVEL% NEQ 0 EXIT /B %ERRORLEVEL%

echo Running pytest...
pytest
IF %ERRORLEVEL% NEQ 0 EXIT /B %ERRORLEVEL%

echo All checks passed!
echo You can now proceed with your commit.
