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

### Social buttons\r
* **Twitter**\r
* **Reddit**\r
* **Telegram**\r
\r
![social buttons](https://i.imgur.com/l3p2EMt.png)\r
\r
### Platform buttons\r
* **Favorite**\r
* **Trade**\r
\r
![Platform buttons](https://i.imgur.com/xTfvQBG.png)\r
\r
### Share buttons\r
* **Share on twitter**\r
* **Share on reddit**\r
* **Share on telegram**\r
\r
![Share buttons](https://i.imgur.com/XFKYkbH.png)

# Install

## Third party modules\r
\r
Install all modules from pip: \r
\r
\\`\\`\\` bash\r
$ pip install -r requirements.txt\r
\\`\\`\\`\r
\r
## Programs\r
\r
To run the project, the following programs must be installed:\r
\r
* [Google Chrome](https://www.google.com/intl/es/chrome) last version

# Settings

To successfully run the program, the following **arguments must be sent, in order**, from the terminal. \r
\r
|Argument|Description|Type|Example\r
|---|---|---|---|\r
|**url**|**Page** of www.dextools.io **to automate**.|String|https://www.dextools.io/app/|\r
|**search_word**|**keyword** to **search** in url page.|String|everape|\r
|**loop**|Number of **times** the process **will be repeated on the page**, with different proxies.|Integer|10|\r
|**wait_time**|**Seconds** to **wait** to load the **pages** opened in new tab.|Integer|30|\r
|**buttons**|One or more arguments, which indicate **which buttons are or aren't pressed** on the page.|String or Boolean|all|\r
\r
Example: \r
\r
\\`\\`\\` bash\r
# Run the program 10 times, using all buttons and wait 30 seconds per page\r
# py dextools-clicker url loops buttons\r
$ py dextools-clicker https://www.dextools.io/app/ everape 10 30 all\r
\\`\\`\\`\r
\r
## Buttons\r
\r
### All\r
\r
With the keyword **\\\"all\\\"** (ignore uppercase and lowercase), the actions of **all buttons** will be performed:\r
* **Twitter**\r
* **Reddit**\r
* **Telegram**\r
* **Favorite**\r
* **Trade**\r
* **Share on twitter**\r
* **Share on reddit**\r
* **Share on telegram**\r
\r
Example: \r
\r
\\`\\`\\` bash\r
# Run the program 10 times, using all buttons and wait 30 seconds per page\r
$ py dextools-clicker https://www.dextools.io/app/ everape 10 30 all\r
\\`\\`\\`\r
\r
### Socials\r
\r
With the keyword **\\\"social\\\"** (ignore uppercase and lowercase), the actions of the **social buttons** will only be performed:\r
* **Twitter**\r
* **Reddit**\r
* **Telegram**\r
\r
Example: \r
\r
\\`\\`\\` bash\r
# Run the program 20 times, using only socials buttons and wait 30 seconds per page\r
$ py dextools-clicker https://www.dextools.io/app/ everape 20 30 socials\r
\\`\\`\\`\r
\r
### Platform\r
\r
With the keyword **\\\"platform\\\"** (ignore uppercase and lowercase), the actions of only the **platform's** unique **buttons** will be performed:\r
* **Favorite**\r
* **Trade**\r
\r
Example: \r
\r
\\`\\`\\` bash\r
# Run the program 100 times, using only platform buttons and wait 30 seconds per page\r
$ py dextools-clicker https://www.dextools.io/app/ everape 100 30 platform\r
\\`\\`\\`\r
\r
### Share\r
\r
With the keyword **\\\"share\\\"** (ignore uppercase and lowercase), the actions of only the **share buttons** will be performed:\r
* **Share on twitter**\r
* **Share on reddit**\r
* **Share on telegram**\r
\r
Example: \r
\r
\\`\\`\\` bash\r
# Run the program 100 times, using only platform buttons and wait 30 seconds per page\r
$ py dextools-clicker https://www.dextools.io/app/ everape 200 30 platform\r
\\`\\`\\`\r
\r
### File\r
\r
With the keyword **\\\"file\\\"** (ignore uppercase and lowercase), the **actions specified in the buttons.json** file will be performed.\r
You can edit the document with any text or code editor.\r
\r
buttons.json file\r
\\`\\`\\` bash\r
{\r
    \\\"twitter\\\": true, \r
    \\\"reddit\\\": false,\r
    \\\"telegram\\\": true,\r
    \\\"trade\\\": true,\r
    \\\"fav\\\": false,\r
    \\\"share_twitter\\\": false, \r
    \\\"share_telegram\\\": true,\r
    \\\"share_reddit\\\": false\r
}\r
\\`\\`\\`\r
\r
Note: in the buttons.json file (unlike the \\\"custom\\\" section), **only true or false values are valid** (upper and lower case does matter).\r
\r
Example: \r
\r
\\`\\`\\` bash\r
# With the buttons.json document from the previous example, the buttons will be executed specifically: twitter, telegram, trade and share_telegram; and wait 30 seconds per page\r
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 file\r
\\`\\`\\`\r
\r
### Custom\r
\r
You can **specify** which **buttons to execute exactly**, from the **terminal**.\r
\r
**After** the variable **\\\"loop\\\"**, **each** of the following **values** will **represent** whether or not to execute a **specific button**, considering the following **order**:\r
\r
1. **Twitter**\r
2. **Reddit**\r
3. **Telegram**\r
4. **Favorite**\r
5. **Trade**\r
6. **Share on twitter**\r
7. **Share on reddit**\r
8. **Share on telegram**\r
\r
If **less than 8** True and False **values** are specified, **all missing values** will be considered **False**.\r
\r
Examples: \r
\r
\\`\\`\\` bash\r
# Run only the Twitter button and wait 30 seconds per page\r
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 true\r
\\`\\`\\`\r
\r
\\`\\`\\` bash\r
# Run only the Telegram button and wait 30 seconds per page\r
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 false false true\r
\\`\\`\\`\r
\r
\\`\\`\\` bash\r
# Run Telegram and Favorite buttons and wait 30 seconds per page\r
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 false false true true\r
\\`\\`\\`\r
\r
\\`\\`\\` bash\r
# Run all buttons except twitter and telegram; and wait 30 seconds per page\r
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 false false true true true true true true\r
\\`\\`\\`\r
\r
\\`\\`\\` bash\r
# Run the buttons: Reddit, Favorite, Share on twitter, Share on telegram and wait 30 seconds per page\r
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 false true false true false true false true\r
\\`\\`\\`\r
\r
#### True values\r
From terminal, **any text other than the following** (ignore case) will be considered as **true**:\r
* **False**\r
* **0** (zero),\r
* **None**\r
* **Null**\r
* **N/A**\r
* Empty String ( **\\\"\\\"** or **''** )\r
\r
Example: \r
\\`\\`\\` bash\r
# Run all buttons\r
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 true True a 1 run sample_text \\\"my text\\\" \\\"run this button\\\"\r
\\`\\`\\`\r
\r
#### False values\r
**Only the following values** will be considered as **false** (ignore case):\r
* **False**\r
* **0** (zero),\r
* **None**\r
* **Null**\r
* **N/A**\r
* Empty String ( **\\\"\\\"** or **''** )\r
\r
Example: \r
\\`\\`\\` bash\r
# Do not run any buttons\r
$ py dextools-clicker https://www.dextools.io/app/ everape 50 30 false False 0 None null n/a \\\"\\\" ''\r
\\`\\`\\`\r
\r
### Not found button\r
\r
If the program does **not find** a specified **button** to use, the program will **not stop**.\r
\r
You can **check the history** of which **buttons** were **used** on each page, as well as which **buttons** were **not found**, in the **.log** file\r
\r
## config.json\r
\r
The config.json file contains the proxy settings.\r
Its structure is as follows.\r
\r
\\`\\`\\` json\r
{\r
    \\\"proxy_user\\\":\\\"your user\\\",\r
    \\\"proxy_pass\\\": \\\"your password\\\",\r
    \\\"proxy_server\\\": \\\"your proxy server or ip\\\",\r
    \\\"proxy_port\\\": \\\"your number of port\\\", \r
    \\\"max_end_page\\\": \\\"max seconds to wait before close browser\\\",\r
    \\\"random_links\\\": \\\"random links / buttons to click before search keywords\\\"\r
}\r
\\`\\`\\`

# Run

Run the **project folder** (dextools clicker) or the **__main __.py** file, with your **python 3.9** interpreter\r
\r
Example: \r
\r
\\`\\`\\` bash\r
$ py dextools-clicker\r
$ py dextools clicker\\__main__.py\r
\\`\\`\\`


