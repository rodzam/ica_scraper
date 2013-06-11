##############################################################
# Program name: ICA Conference Site Scraper (Downloader Module)
# Version: 0.1-alpha
# By: Rodrigo Zamith
# License: MPL 2.0 (see LICENSE file in root folder)
# Additional thanks: 
##############################################################

import cookielib
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

# Variables that need setting
start_url = 'http://convention2.allacademic.com/one/ica/ica13/' # URL to start from
params = { } # Any POST parameters that need to be sent
http_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0",
            "Accept": "text/plain, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "DNT": "1",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://convention2.allacademic.com/one/ica/ica13/",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
            } # Variables from the HTTP header


##### THE SCRIPT WILL TAKE IT FROM HERE #####

### Define our functions
def create_cookie():
    # Create a cookie handler, if necessary
    cookie_jar = cookielib.LWPCookieJar()
    cookie = urllib2.HTTPCookieProcessor(cookie_jar)
    
    # Create an urllib2 opener() using our cookie jar
    opencookies = urllib2.build_opener(cookie)
    return(opencookies)

def grabber(url, params, http_header, cookiejar):
    # Create the HTTP request
    req = urllib2.Request(url, urllib.urlencode(params), http_header)
    
    # Submit the request
    res = cookiejar.open(req)
    data = res.read()
    return(data)

### Grab data
opencookies = create_cookie() # Create a cookie jar

# Start with the front page
start_url_data = grabber(start_url, params, http_header, opencookies) # Get data from main page
start_url_data_soup = BeautifulSoup(start_url_data) # Soupify it for parsing
program_url = start_url_data_soup.find(text=re.compile("Search the Online Program")).parent['href']

# Progress to the program
program_url_data = grabber(program_url, params, http_header, opencookies) # Get data from program page
program_url_data_soup = BeautifulSoup(program_url_data) # Soupify it for parsing
individual_submissions_url = program_url_data_soup.find(text=re.compile("Individual Submissions")).parent['href']

# Progress to the Individual Submissions and start saving the pages

end = 1
id_no = 1

while end > 0:
    print "Parsing page " + str(end) + " ("+ str(individual_submissions_url) + ")"
    individual_submissions_url_data = grabber(individual_submissions_url, params, http_header, opencookies) # Get data from program page
    individual_submissions_url_data_soup = BeautifulSoup(individual_submissions_url_data) # Soupify it for parsing
    try:
        individual_submissions_url = individual_submissions_url_data_soup.find(text=re.compile("Next")).parent['href']
    except KeyError:
        end = -1
    
    filename = "pages/page_" + str(id_no) + ".html"
    writepages = open(filename, "w")
    writepages.writelines(individual_submissions_url_data)
    
    id_no += 1
    end += 1
print "Finished!"
