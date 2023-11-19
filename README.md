# Glungus Every Hour

Silly little twitter bot that posts glungus

Requirements for Ubuntu (both x64 and arm work btw):
- Desktop environment (any de will work)
- Python 3 and pip
- Chromium and Chromium web driver

Requirements for Windows:
- Python 3 and pip
- Chrome/Chromium and Chrome/Chromium web driver

Install the needed pip module:
```
pip install -r requirements
(or)
pip install selenium
```


Usage:
- Add your twitter bot credentials in dump_cookie.py
- Run dump_cookie.py
- Change the twitter embed link to whatever you want
- Use crontab or task scheduler to make glungus.py run hourly, every day or whatever

Your crontab setup should look like this:
```
DISPLAY=:  # You can find the correct display number by running env | grep DISPLAY
0 * * * * python3 # Paste the path of glungus.py here
```
Credits:
- [Artur Spirin](https://www.youtube.com/watch?v=s9m6h1bLVIo)
- [Manish Sutradhar](https://replit.com/@ManishSutradhar/Twitter-bot?v=1#main.py) (I stole most of the code from here I just modified it to work with the latest version of selenium and to work the new twitter layout)
