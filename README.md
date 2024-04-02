# Url2pdf
a REST JSON api which return pdf in base64 format from the given url

Developed in python programming language using [Flask](https://flask.palletsprojects.com/en/latest/) and [selenium](https://www.selenium.dev/documentation) packages

## Usage 
> Locally
1. Clone or download the [repo](https://github.com/botdenoms/url2pdf)

2. Create a virtual environment and activate it.

    **Not Mandatory** 


3. install the requirements 
```
# From the terminal 
pip3 install -r requirement.txt  
```
>  **Mandatory** 

Download the chrome driver or the [driver](https://chromedriver.chromium.org/downloads) of your desired browser of choice. 

modify main.py file by adding the path to the drive file


4. run the main file 
```
python3 main.py  
```

5. make a requesst to the server using the  format 

```
# using curl 
curl http://127.0.0.1:5000/v1/api/url2pdf\?url=https://site.domain.com
# or
# from a browser window with the url parameter
```

---
> Production mode/ Remote

use the [Flask production documentation ](https://flask.palletsprojects.com/en/latest/deploying/) on how export a flask app in production mode to your desired production server

make a requesst to the server using the  format similar to the local mode but substite the necessary information as shown below
```
curl http(s)://{Host ip or domain address}:{port}/v1/api/url2pdf\?url=https://site.domain.com
# or
# from a browser window with the url parameter
```
## Constrains
the url parameter should have the preceding protocol

http://
or
https://
before the domain name

the contrain in the url will be addressed in future updates

----

