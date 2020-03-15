# Flipkart Price Tracker
Flipkart Product Price Tracker is simple web scraper application that takes in user preferred product on Flipkart to track price and send an email notification when price has fallen down.  

* How To Run 
    * [windows] `virtualenv env` or  [linux] `python -m venv name-env` 
    * `source env/bin/activate`
    * `pip install -r requirements.txt`
    * `To Run: python scraper.py`
    
**_NOTE:_**  Mail configured for gmail only and sender's gmail id shouldn't have google Two Step Verification Enabled . You can either disable verification or create new googgle app password More info [here](https://myaccount.google.com/apppasswords)