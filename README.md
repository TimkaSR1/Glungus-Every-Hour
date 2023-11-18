# Glungus-Every-Hour

Silly little bot that posts glungus

Requirements for Ubuntu:
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
- Add your twitter bot credentials in dump.py
- Run dump.py
- Change the twitter embed link to whatever you want
- Use crontab or task scheduler to make it run hourly, every day or whatever


Credits:
- [Artur Spirin](https://www.youtube.com/watch?v=s9m6h1bLVIo)
- [Manish Sutradhar](https://replit.com/@ManishSutradhar/Twitter-bot?v=1#main.py) (I stole most of the code from here I just modified it to work with the latest version of selenium and to work the new twitter layout)
