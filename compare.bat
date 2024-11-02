cd C:\Users\Annhi\Desktop\CodeLibrary\songs-python
set /p exercise=Which exercise to compare(type 0 to compare all of them):
call .venv\Scripts\activate
python ./run.py True %exercise%
PAUSE
deactivate