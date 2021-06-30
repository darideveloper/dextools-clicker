import os
import sys
import log
import config
import globals
from scraping_manager.automate import Web_scraping

def main (url): 
    
    # proxy loop
    
    # open URL and wait to load page
    scraper = Web_scraping(url, headless=False)
    text = "Loading page..."
    log.info(text, print_text=True)
    selector_span = ".ng-trigger.ng-trigger-simpleFadeAnimation.ng-star-inserted"
    scraper.wait_load(selector_span)
    scraper.refresh_selenium()
    
    # List of all links in the page
    links_found = [] 
    
    # Get all social buttons
    selector_buttons = ".d-inline-block.align-bottom > a.ng-star-inserted"
    elems = scraper.get_elems(selector_buttons)
    socials = ["Twitter", "Reddit", "Telegram"]
    for index in range(1, len(elems)+1):
    
        link_selector = selector_buttons + f":nth-child({index})"        
        link = scraper.get_attrib(link_selector, "href")
        
        icon_selector = link_selector + " > i.text-light"
        icon_classes = scraper.get_attrib(icon_selector, "class")
        
        # Save social links
        if icon_classes:
            for social in socials: 
                if str(social).lower() in icon_classes: 
                    links_found.append(link)
                    messsage = f"{social} button found"
                    log.info(messsage, print_text=True)
                    socials.remove(social)                
                
                
    
    # Click trade 
    selector_trade = "a.btn.btn-salmon.btn-icon-absolute.ng-star-inserted"
    link_trade = scraper.get_attrib(selector_trade, "href")
    links_found.append(link_trade)
    text = "Trade button found."
    log.info(text, print_text=True)
    
    # Click favorite button
    selector_fav = ".btn.btn-success.btn-icon-absolute.ng-star-inserted"
    scraper.click(selector_fav)    
    text = "Favorite button found"
    log.info(text, print_text=True)
    
    # Open al links
    print ("Openning all links...")
    for link in links_found: 
        scraper.set_page_js(link, new_tab=False)
    
    # input ("Press Enter to end.")
        
    # Close all tabs in browser
    scraper.end_browser()
    
    
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ("Arguments error: ") 
        print ("\tTry to run: py __main__.py  ") 
    else: 
        
        # Get terminal arguments
        url = sys.argv[1]
        
        #  call main function
        scraper = main(url)