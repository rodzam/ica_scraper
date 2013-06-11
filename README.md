ICA Conference Site Scraper
=============================
Author: Rodrigo Zamith  
Version: 1.0


Usage
-----
Just edit the 'start_url' variable in `downloader.py` and execute the scripts in the following order:

1. downloader.py (Downloads each page from the online conference program)
2. scraper.py (Scrapes the locally-stored pages)
3. longform.py (Converts the data into long-form (each author as a case), which facilitates certain analyses in R)


Requirements
------------
This script requires Python, as well as the urllib2 and BeautifulSoup libraries.


License
--------
This script is licensed under the Mozilla Public License Version 2.0 (see LICENSE file in root folder). TL;DR: feel free to use it commercially, modify it, and distribute it, provided you disclose both the source code and any moditations you make to it. Attribution, where appropriate, is appreciated.
