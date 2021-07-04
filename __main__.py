import os
import sys
import log
import time
import random
import json
import config
from scraping_manager.automate import Web_scraping

def click_button (
        name, scraper, selector, run=True, close_tab=True, 
        inside_selector="", wait_time=1): 
    """Click in specific button in the page with css selector

    Args:
        name (str): Name of the button (for print in therminal)
        scraper (Web_scraping): Web scraping instance (based on selenium)
        selector (str): CSS selector of the button
        run (bool): Run or not the acction in the current button
        close_tab (bool, optional): Close the current tab after click. Defaults to True.
        inside_selector(str): CSS selector inside the new tab, for wait to load the new page
        wait_time (int): Seconds to wait before close browser
    """
    
    if run:
        # Try to click in button
        try:
            scraper.click(selector)
        except: 
            text = f"{name} button not found."
        else: 
            
            # Close the new tab
            if close_tab: 
                scraper.switch_to_tab(1)
                
                # if wait_time:
                time.sleep(wait_time)
                
                # Wait to page load
                if inside_selector: 
                    scraper.wait_load(inside_selector)
                
                scraper.close_tab()
                scraper.switch_to_tab(0)
                
            text = f"{name} button clicked."
        finally:
            log.info(text, print_text=True)
        
        time.sleep (1)
    

def main (
        url, search_word, loops, twitter_run, reddit_run, telegram_run, 
        trade_run, fav_run, share_twitter_run, share_telegram_run, 
        share_reddit_run, wait_time=1): 
    """Run the acction in order for all butons in the page 

    Args:
        url (str): The url of the page to automate
        search_word (str): Key for search in main page
        loops (bool): Number of repetitions to do in the page
        twitter_run (bool): Run or not the twitter button
        reddit_run (bool): Run or not the reddit button
        telegram_run (bool): Run or not the telegram button
        trade_run (bool): Run or not the trade button
        fav_run (bool): Run or not the favorite button
        share_twitter_run (bool): Run or not the twitter share button
        share_telegram_run (bool): Run or not the telegram share button
        share_reddit_run (bool): Run or not the reddit share button
        wait_time (int): Seconds to wait before close browser
    """
    
    
    log.info(f"Current page: {url}", print_text=True)
        
    # Get crdentials
    config_path = os.path.join (os.path.dirname(__file__), "config.json")
    with open (config_path) as file: 
        data = json.loads(file.read())
    
    # Get proxy and user preferences
    proxy_server = data["proxy_server"]
    proxy_port = data["proxy_port"]
    proxy_user = data["proxy_user"]
    proxy_pass = data["proxy_pass"]
    proxy = f"https://{proxy_user}:{proxy_pass}@{proxy_server}:{proxy_port}"
    max_end_page = int (data["max_end_page"])
    random_links = int (data["random_links"])
    log.info (f"Proxy: {proxy}", print_text=True)
    
    for loop_counter in range(loops): 
        
        # Web scraping instance with proxy
        scraper = Web_scraping("about:blank", 
                            headless=False,  
                            proxy_server=proxy_server,
                            proxy_port=proxy_port, 
                            proxy_user=proxy_user, 
                            proxy_pass=proxy_pass)
        
        log.info(f"\tLoop {loop_counter+1} of {loops}", print_text=True) 
        
        # loop for open URL and wait to load the results page
        while True: 
            log.info("Loading base page...", print_text=True)
            selector_search = "ng-autocomplete > div > div.input-container > input"
            scraper.set_page(url)
            
            try: 
                scraper.wait_load(selector_search, time_out=30)
            except: 
                log.info ("The page took too long to load. retrying.", print_text=True)
            else: 
                scraper.refresh_selenium()        
                break
        
        # Loop por each random link to click
        for index in range (random_links):
            
            while True:
                try:
                    # Get links / buttons
                    selector_link = 'a[target="_blank"]'
                    links = scraper.get_elems(selector_link)
                    
                    # Click button
                    random_link = random.choice(links)
                    random_link.click() 
                except: 
                    continue
                else:
                    break
            
            # Go back (close new tab or return to page in browser)
            print (f"Openning random link {index+1}...")
            scraper.switch_to_tab(1)                
            time.sleep(5)
            scraper.close_tab()
            scraper.switch_to_tab(0)
            time.sleep(2)
        browser = scraper.get_browser().refresh()
        
        # Search specific word and select first element        
        scraper.send_data(selector_search, search_word)        
        selector_first_result = "ng-autocomplete > div > div > ul > li:nth-child(2)"        
        scraper.wait_load (selector_first_result, time_out=20)
        scraper.click(selector_first_result)  
        
        # loop for open URL and wait to load the results page
        while True: 
            log.info("Loading specific page...", print_text=True)
            selector_span = ".ng-trigger.ng-trigger-simpleFadeAnimation.ng-star-inserted"
            
            if loop_counter > 0: 
                scraper.reload_forced()
            
            try: 
                scraper.wait_load(selector_span, time_out=30)
            except: 
                log.info ("The page took too long to load. retrying.", print_text=True)
            else: 
                scraper.refresh_selenium()
                break
            
                
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
                        inside_selector=selector_twitter_inside, wait_time=wait_time)
            click_button("Reddit", scraper, selector_reddit, reddit_run, wait_time=wait_time)
            click_button("Telegram", scraper, selector_telegram, telegram_run, wait_time=wait_time)
        
        # Open platform buttons 
        if  trade_run or fav_run:
            
            # Get trade link
            trade_link = scraper.get_attrib (selector_trade, "href")
            
            if trade_link: 
                # Normal trade button
                click_button("Trade", scraper, selector_trade, trade_run, wait_time=wait_time)
            else: 
                # Catch trade warning
                selector_trade_warning = "body > ngb-modal-window > div > div > app-scam-modal > div > a"
                selector_trade_close = "body > ngb-modal-window > div > div > app-scam-modal > div > button"
                
                scraper.click(selector_trade)
                time.sleep(1)
                scraper.refresh_selenium()
                
                click_button("Trade", scraper, selector_trade_warning, trade_run, wait_time=wait_time)
                scraper.refresh_selenium()
                scraper.click (selector_trade_close)              
            
            
            click_button("Favorite", scraper, selector_fav, fav_run, close_tab=False, wait_time=wait_time)
            
        # Open share buttons
        if share_twitter_run or share_telegram_run or share_reddit_run:
            scraper.click(selector_share)
            time.sleep(2)
            scraper.refresh_selenium()
            time.sleep(2)
            click_button("Share twitter", scraper, selector_share_twitter, 
                        share_twitter_run, inside_selector=selector_share_twitter_iside, 
                        wait_time=wait_time)
            click_button("Share telegram", scraper, selector_share_telegram, 
                        share_telegram, wait_time=wait_time)
            click_button("Share reddit", scraper, selector_share_reddit,
                        share_reddit, wait_time=wait_time)
        
        # Wait time
        time.sleep(2)
                
        # Wait random time before end browser loop
        wait_seconds = random.randint(1,max_end_page)
        print (f"Waiting {wait_seconds}s for close browser...")
        time.sleep (wait_seconds)
        
        # End selenium
        scraper.end_browser()
    

if __name__ == "__main__":
    """Run main function with terminal arguments

    Raises:
        AttributeError: Very few arguments. The program does not accept less than 3 arguments
        AttributeError: Too many arguments. The program does not accept more than 10 arguments
        AttributeError: Invalid url. The program only accepts urls from the domain www.dextools.io
        TypeError: The second argument must be an integer
    """
    
    help_message = "\n\tRead README file in github for more info \n\t(https://github.com/DariHernandez/dextools-clicker)"
        
    if len(sys.argv) < 6:
        raise AttributeError(f"Very few arguments. {help_message}")
    elif len (sys.argv) > 13: 
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
        
        # Get seach word 
        search_word = sys.argv[2]
        
        # Try to get loops
        try:
            loops = int(sys.argv[3])
        except: 
            raise TypeError(f"The second argument must be an integer.{help_message}")
            sys.exit()
        
        # Try to get loops
        try:
            wait_time = int(sys.argv[4])
        except: 
            raise TypeError(f"The second argument must be an integer.{help_message}")
            sys.exit()
        
        # Get third argument
        third_argv = str(sys.argv[5]).lower()
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
            
        elif third_argv == "file": 
            
            # Open json setting file
            json_path = os.path.join (os.path.dirname(__file__), "buttons.json")
            with open (json_path) as file: 
                data = json.loads(file.read())
                
            twitter = data["twitter"] 
            reddit = data["reddit"] 
            telegram = data["telegram"] 
            trade = data["trade"] 
            fav = data["fav"] 
            share_twitter = data["share_twitter"]  
            share_telegram = data["share_telegram"] 
            share_reddit = data["share_reddit"] 
            
        else:
            
            # Convert all other arguments to boolean
            specific_buttons = []
            for argv in sys.argv[5:]:
                
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
        scraper = main(url, search_word, loops, twitter, reddit, telegram, trade, fav, 
                       share_twitter, share_telegram, share_reddit, wait_time)