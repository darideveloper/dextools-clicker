import os
import sys
import log
import time
import config
import globals
from scraping_manager.automate import Web_scraping

def click_button (name, scraper, selector, run=True, close_tab=True, inside_selector=""): 
    """Click in specific button in the page with css selector

    Args:
        name (str): Name of the button (for print in therminal)
        scraper (Web_scraping): Web scraping instance (based on selenium)
        selector (str): Css selector of the button
        close_tab (bool, optional): Close the current tab after click. Defaults to True.
    """
    
    if run:
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
                time.sleep(5)
                
                # Wait to page load with js
                if inside_selector: 
                    scraper.wait_load(inside_selector)
                
                scraper.close_tab()
                scraper.switch_to_tab(0)
                
            text = f"{name} button clicked."
        finally:
            log.info(text, print_text=True)
    

def main (
        url, loops, twitter_run, reddit_run, telegram_run, trade_run, fav_run, 
        share_twitter_run, share_telegram_run, share_reddit_run): 
    
    print (twitter_run, reddit_run, telegram_run, trade_run, fav_run, 
        share_twitter_run, share_telegram_run, share_reddit_run)
    
    # proxy loop
    
    # open URL and wait to load page
    scraper = Web_scraping(url, headless=False)
    text = "Loading page..."
    log.info(text, print_text=True)
    selector_span = ".ng-trigger.ng-trigger-simpleFadeAnimation.ng-star-inserted"
    scraper.wait_load(selector_span)
    scraper.refresh_selenium()
    
    # Social, platforms, share an internal selectores
    selector_twitter = "i.fa.fa-twitter.text-light"
    selector_reddit = "i.fa.fa-reddit.text-light"
    selector_telegram = "i.fa.fa-telegram.text-light"
    selector_trade = "a.btn.btn-salmon.btn-icon-absolute.ng-star-inserted"
    selector_fav = ".btn.btn-success.btn-icon-absolute.ng-star-inserted"
    selector_twitter_inside = '.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf'
    selector_twitter_inside += '.r-7cikom.r-1ny4l3l.r-xyw6el.r-641cr4.r-1dz5y72'
    selector_share = ".fa.fa-share-alt"
    selector_share_twitter = ".btn-twitter.btn-outline-info"
    selector_share_telegram = ".btn-telegram.btn-outline-info"
    selector_share_reddit = ".btn-reddit.btn-outline-salmon"
    selector_share_twitter_iside = ".r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64"
    selector_share_twitter_iside += ".r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72"
    
    # Open social buttons
    if twitter_run or reddit_run or telegram_run:
        click_button("Twitter", scraper, selector_twitter, twitter_run,  
                    inside_selector=selector_twitter_inside)
        click_button("Reddit", scraper, selector_reddit, reddit_run)
        click_button("Telegram", scraper, selector_telegram, telegram_run)
    
    # Open platform buttons 
    if  trade_run or fav_run:
        click_button("Trade", scraper, selector_trade, trade_run)
        click_button("Favorite", scraper, selector_fav, fav_run, close_tab=False)
        
    # Open share buttons
    if share_twitter_run or share_telegram_run or share_reddit_run:
        click_button("Share", scraper, selector_share, close_tab=False)
        scraper.refresh_selenium()
        time.sleep(3)
        click_button("Share twitter", scraper, selector_share_twitter, 
                     share_twitter_run, inside_selector=selector_share_twitter_iside)
        click_button("Share telegram", scraper, selector_share_telegram, 
                     share_telegram)
        click_button("Share reddit", scraper, selector_share_reddit,
                     share_reddit)
    
    # Wait time
    time.sleep(2)
            
    # Close all tabs in browser
    scraper.end_browser()
    

if __name__ == "__main__":
    
    help_message = "\n\tRun --help for more info"
    
    if len(sys.argv) < 4:
        raise AttributeError(f"Very few arguments. {help_message}")
    elif len (sys.argv) > 11: 
        raise AttributeError(f"Too many arguments. {help_message}")
    else: 
        
        # Activate or deactivate actions 
        twitter = False 
        reddit = False
        telegram = False
        trade = False
        fav = False
        share_twitter = False 
        share_telegram = False
        share_reddit = False
        
        # Get and validate url
        url = sys.argv[1]
        if not "www.dextools.io" in url: 
            raise AttributeError(f"'{url}' is an invalid url")
            sys.exit()
        
        # Try to get loops
        try:
            loops = int(sys.argv[2])
        except: 
            raise TypeError(f"The second argument must be an integer.{help_message}")
            sys.exit()
        
        # Get third argument
        third_argv = str(sys.argv[3]).lower()
        if third_argv == "all": 
            
            # Run all options
            twitter = True 
            reddit = True
            telegram = True
            trade = True
            fav = True
            share_twitter = True 
            share_telegram = True
            share_reddit = True
            
        elif third_argv == "socials": 
            
            # Run social buttons
            twitter = True 
            reddit = True
            telegram = True
            
        elif third_argv == "platform": 
            
            # Run the platform buttons
            trade = True
            fav = True
            
        elif third_argv == "share": 
            
            # Run share buttons
            share_twitter = True 
            share_telegram = True
            share_reddit = True
            
        else:
            
            # Convert all other arguments to boolean
            specific_buttons = []
            for argv in sys.argv[3:]:
                
                # Convert to title string
                argv_str = str(argv).title()
                
                # Validate3 with list of false vales
                false_values = ["False", "0", "None", "Null", "N/A", "''", '""']
                if argv_str in false_values: 
                    argv_bool = False
                else: 
                    argv_bool = True
                specific_buttons.append(argv_bool)
            
            # fill in the missing fields
            missing_fields = 8 - len (specific_buttons)
            for _ in range(missing_fields): 
                specific_buttons.append(False)
                
            # Set values for control variables
            twitter = specific_buttons[0] 
            reddit = specific_buttons[1] 
            telegram = specific_buttons[2] 
            trade = specific_buttons[3] 
            fav = specific_buttons[4] 
            share_twitter = specific_buttons[5]  
            share_telegram = specific_buttons[6]
            share_reddit = specific_buttons[7]                 
            
        
        # call main function
        scraper = main(url, loops, twitter, reddit, telegram, trade, fav, 
                       share_twitter, share_telegram, share_reddit)