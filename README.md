# DEXTOOLS CLICKER
**python version: 3.9**

Web automation script, to **click on specific buttons** within the pages of the domain **www.dextools.io/app/uniswap/pair-explorer/**, implementing **proxies**.

## Supported buttons

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
## Tird party modules

Install all modules from pip: 

``` bash
$ pip install -r requirements.txt
```

## Programs

To run the project, the following programs must be installed:: 

* [Google Chrome](https://www.google.com/intl/es/chrome) last version

# Run the program

Run the **project folder** (dextools clicker) or the **__main __.py** file, with your **python 3.9** interpreter

Example: 

``` bash
$ py dextools-clicker
$ py dextools clicker\__main__.py
```

# Setting

To successfully run the program, the following **arguments must be sent, in order**, from the terminal. 

|Argument|Description|Type|Example
|---|---|---|---|
|**url**|**Page** of www.dextools.io **to automate**.|String|https://www.dextools.io/app/|
|**search_word**|**keyword** to **search** in url page.|String|everape|
|**loop**|Number of **times** the process **will be repeated on the page**, with different proxies.|Integer|10|
|**buttons**|One or more arguments, which indicate **which buttons are or aren't pressed** on the page.|String or Boolean|all|

Example: 

``` bash
# Run the program 10 times, using all buttons
# py dextools-clicker url loops buttons
$ py dextools-clicker https://www.dextools.io/app/ everape 10 all
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
# Run the program 10 times, using all buttons
$ py dextools-clicker https://www.dextools.io/app/ everape 10 all
```

### Socials

With the keyword **"social"** (ignore uppercase and lowercase), the actions of the **social buttons** will only be performed:
* **Twitter**
* **Reddit**
* **Telegram**

Example: 

``` bash
# Run the program 20 times, using only socials buttons
$ py dextools-clicker https://www.dextools.io/app/ everape 20 socials
```

### Platform

With the keyword **"platform"** (ignore uppercase and lowercase), the actions of only the **platform's** unique **buttons** will be performed:
* **Favorite**
* **Trade**

Example: 

``` bash
# Run the program 100 times, using only platform buttons
$ py dextools-clicker https://www.dextools.io/app/ everape 100 platform
```

### Share

With the keyword **"share"** (ignore uppercase and lowercase), the actions of only the **share buttons** will be performed:
* **Share on twitter**
* **Share on reddit**
* **Share on telegram**

Example: 

``` bash
# Run the program 100 times, using only platform buttons
$ py dextools-clicker https://www.dextools.io/app/ everape 200 platform
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
# With the buttons.json document from the previous example, the buttons will be executed specifically: twitter, telegram, trade and share_telegram
$ py dextools-clicker https://www.dextools.io/app/ everape 50 file
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
# Run only the Twitter button.
$ py dextools-clicker https://www.dextools.io/app/ everape 50 true
```

``` bash
# Run only the Telegram button.
$ py dextools-clicker https://www.dextools.io/app/ everape 50 false false true
```

``` bash
# Run Telegram and Favorite buttons.
$ py dextools-clicker https://www.dextools.io/app/ everape 50 false false true true
```

``` bash
# Run all buttons except twitter and telegram
$ py dextools-clicker https://www.dextools.io/app/ everape 50 false false true true true true true true
```

``` bash
# Run the buttons: Reddit, Favorite, Share on twitter, Share on telegram
$ py dextools-clicker https://www.dextools.io/app/ everape 50 false true false true false true false true
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
$ py dextools-clicker https://www.dextools.io/app/ everape 50 true True a 1 run sample_text "my text" "run this button"
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
$ py dextools-clicker https://www.dextools.io/app/ everape 50 false False 0 None null n/a "" ''
```

### Not found button

If the program does **not find** a specified **button** to use, the program will **not stop**.

You can **check the history** of which **buttons** were **used** on each page, as well as which **buttons** were **not found**, in the **.log** file

## Proxy (config.json)

The config.json file contains the proxy settings.
Its structure is as follows.

``` json
{
    "proxy_user":"your user",
    "proxy_pass": "your password",
    "proxy_server": "your proxy server or ip",
    "proxy_port": "your number of port"
}
```