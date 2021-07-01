import os
import sys
import log
import time
import config
import globals
from scraping_manager.automate import Web_scraping

def click_button (name, scraper, selector, close_tab=True, inside_selector=""): 
    """Click in specific button in the page with css selector

    Args:
        name (str): Name of the button (for print in therminal)
        scraper (Web_scraping): Web scraping instance (based on selenium)
        selector (str): Css selector of the button
        close_tab (bool, optional): Close the current tab after click. Defaults to True.
    """
    
    # Try to click in button
    try:
        # Open link / click in button
        scraper.click(selector)
    except: 
        text = f"{name} button not found."
    else: 
        
        # Close the new tab
        if close_tab: 
            scraper.switch_to_tab(1)
            time.sleep(3)
            
            # Wait to page load with js
            if inside_selector: 
                scraper.wait_load(inside_selector)
            
            scraper.close_tab()
            scraper.switch_to_tab(0)
            
        text = f"{name} button clicked."
    finally:
        log.info(text, print_text=True)
    

def main (url): 
    
    # proxy loop
    
    # open URL and wait to load page
    scraper = Web_scraping(url, headless=False)
    text = "Loading page..."
    log.info(text, print_text=True)
    selector_span = ".ng-trigger.ng-trigger-simpleFadeAnimation.ng-star-inserted"
    scraper.wait_load(selector_span)
    scraper.refresh_selenium()
    
    # social and platform buttons selectors
    selector_twitter = "i.fa.fa-twitter.text-light"
    selector_reddit = "i.fa.fa-reddit.text-light"
    selector_telegram = "i.fa.fa-telegram.text-light"
    selector_trade = "a.btn.btn-salmon.btn-icon-absolute.ng-star-inserted"
    selector_fav = ".btn.btn-success.btn-icon-absolute.ng-star-inserted"
    
    # Internal selector for the new page opened 
    selector_twitter_inside = '.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3'
    selector_twitter_inside += '.r-7cikom.r-1ny4l3l.r-xyw6el.r-641cr4.r-1dz5y72.r-fdjqy7.r-13qz1uu'
    
    # Open first buttons
    click_button("Twitter", scraper, selector_twitter, 
                 inside_selector=selector_twitter_inside)
    click_button("Reddit", scraper, selector_reddit)
    click_button("Telegram", scraper, selector_telegram)
    click_button("Trade", scraper, selector_trade)
    click_button("Favorite", scraper, selector_fav, close_tab=False)

    
    input ("Press Enter to end.")
        
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