<div><a href='https://github.com/darideveloper/dextools-clicker/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/darideveloper/dextools-clicker.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/dextools-clicker/blob/master/logo.png?raw=true' alt='Dextools Clicker' height='80px'/>

# Dextools Clicker

Web automation script, to **click on specific buttons** within the pages of the domain **www.dextools.io/app/uniswap/pair-explorer/**, implementing **proxies**.

Start date: **2021-06-30**

Last update: **2023-04-13**

Project type: **client's project**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://www.selenium.dev/' target='_blank'> <img src='https://cdn.svgporn.com/logos/selenium.svg' alt='Selenium' title='Selenium' height='50px'/> </a></div>

# Details

### Social buttons
* **Twitter**
* **Reddit**
* **Telegram**

![social buttons](https://i.imgur.com/l3p2EMt.png)

### Platform buttons
* **Favorite**
* **Trade**

![Platform buttons](https://i.imgur.com/xTfvQBG.png)

### Share buttons
* **Share on twitter**
* **Share on reddit**
* **Share on telegram**

![Share buttons](https://i.imgur.com/XFKYkbH.png)

# Install

## Third party modules

Install all modules from pip: 

``` bash
$ pip install -r requirements.txt
```

## Programs

To run the project, the following programs must be installed:

* [Google Chrome](https://www.google.com/intl/es/chrome) last version

# Settings

To successfully run the program, the following **arguments must be sent, in order**, from the terminal. 

|Argument|Description|Type|Example
|---|---|---|---|
|**url**|**Page** of www.dextools.io **to automate**.|String|https://www.dextools.io/app/|
|**search_word**|**keyword** to **search** in url page.|String|everape|
|**loop**|Number of **times** the process **will be repeated on the page**, with different proxies.|Integer|10|
|**wait_time**|**Seconds** to **wait** to load the **pages** opened in new tab.|Integer|30|
|**buttons**|One or more arguments, which indicate **which buttons are or aren't pressed** on the page.|String or Boolean|all|

Example: 

``` bash
# Run the program 10 times, using all buttons and wait 30 seconds per page
# py dextools-clicker url loops buttons
$ py dextools-clicker https://www.dextools.io/app/ everape 10 30 all
```

## Buttons

### All

With the keyword **"all"** (ignore uppercase and lowercase), the actions of **all buttons** will be performed:
* **Twitter**
* **Reddit**
* **Telegram**
* **Favorite**
* **Trade**
* **Share on twitter**
* **Share on reddit**
* **Share on telegram**

Example: 

``` bash
# Run the program 10 times, using all buttons and wait 30 seconds per page
$ py dextools-clicker https://www.dextools.io/app/ everape 10 30 all
```

### Socials

With the keyword **"social"** (ignore uppercase and lowercase), the actions of the **social buttons** will only be performed:
* **Twitter**
* **Reddit**
* **Telegram**

Example: 

``` bash
# Run the program 20 times, using only socials buttons and wait 30 seconds per page
$ py dextools-clicker https://www.dextools.io/app/ everape 20 30 socials
```

### Platform

With the keyword **"platform"** (ignore uppercase and lowercase), the actions of only the **platform's** unique **buttons** will be performed:
* **Favorite**
* **Trade**

Example: 

``` bash
# Run the program 100 times, using only platform buttons and wait 30 seconds per page
$ py dextools-clicker https://www.dextools.io/app/ everape 100 30 platform
```

### Share

With the keyword **"share"** (ignore uppercase and lowercase), the actions of only the **share buttons** will be performed:
* **Share on twitter**
* **Share on reddit**
* **Share on telegram**

Example: 

``` bash
# Run the program 100 times, using only platform buttons and wait 30 seconds per page
$ py dextools-clicker https://www.dextools.io/app/ everape 200 30 platform
```

### File

With the keyword **"file"** (ignore uppercase and lowercase), the **actions specified in the buttons.json** file will be performed.
You can edit the document with any text or code editor.

buttons.json file
``` bash
{
    "twitter": true, 
    "reddit": false,
    "telegram": true,
    "trade": true,
    "fav": false,
    "share_twitter": false, 
    "share_telegram": true,
    "share_reddit": false
}
```

Note: in the buttons.json file (unlike the "custom" section), **only true or false values are valid** (upper and lower case does matter).

Example: 

``` bash
# With the buttons.json document from the previous example, the buttons will be executed specifically: twitter, telegram, trade and share_telegram; and wait 30 seconds per page
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 file
```

### Custom

You can **specify** which **buttons to execute exactly**, from the **terminal**.

**After** the variable **"loop"**, **each** of the following **values** will **represent** whether or not to execute a **specific button**, considering the following **order**:

1. **Twitter**
2. **Reddit**
3. **Telegram**
4. **Favorite**
5. **Trade**
6. **Share on twitter**
7. **Share on reddit**
8. **Share on telegram**

If **less than 8** True and False **values** are specified, **all missing values** will be considered **False**.

Examples: 

``` bash
# Run only the Twitter button and wait 30 seconds per page
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 true
```

``` bash
# Run only the Telegram button and wait 30 seconds per page
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 false false true
```

``` bash
# Run Telegram and Favorite buttons and wait 30 seconds per page
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 false false true true
```

``` bash
# Run all buttons except twitter and telegram; and wait 30 seconds per page
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 false false true true true true true true
```

``` bash
# Run the buttons: Reddit, Favorite, Share on twitter, Share on telegram and wait 30 seconds per page
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 false true false true false true false true
```

#### True values
From terminal, **any text other than the following** (ignore case) will be considered as **true**:
* **False**
* **0** (zero),
* **None**
* **Null**
* **N/A**
* Empty String ( **""** or **''** )

Example: 
``` bash
# Run all buttons
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 true True a 1 run sample_text "my text" "run this button"
```

#### False values
**Only the following values** will be considered as **false** (ignore case):
* **False**
* **0** (zero),
* **None**
* **Null**
* **N/A**
* Empty String ( **""** or **''** )

Example: 
``` bash
# Do not run any buttons
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 false False 0 None null n/a "" ''
```

### Not found button

If the program does **not find** a specified **button** to use, the program will **not stop**.

You can **check the history** of which **buttons** were **used** on each page, as well as which **buttons** were **not found**, in the **.log** file

## config.json

The config.json file contains the proxy settings.
Its structure is as follows.

``` json
{
    "proxy_user":"your user",
    "proxy_pass": "your password",
    "proxy_server": "your proxy server or ip",
    "proxy_port": "your number of port", 
    "max_end_page": "max seconds to wait before close browser",
    "random_links": "random links / buttons to click before search keywords"
}
```

# Run

Run the **project folder** (dextools clicker) or the **__main __.py** file, with your **python 3.9** interpreter

Example: 

``` bash
$ py dextools-clicker
$ py dextools clicker__main__.py
```


