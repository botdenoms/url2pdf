from flask import Flask, jsonify, request
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


app = Flask(__name__)

chrome_driver = './chromedriver'
service = Service(chrome_driver)
options = Options()
options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=service, options=options)

@app.route('/')
def home():
    data = {
        'Status': 200,
        'url': '',
        'at': '/v1/api/url2pdf',
        'version': 'v1'
    }
    return jsonify(data)

@app.route('/v1/api/url2pdf')
def url2pdf(): 
    url = request.args.get('url')
    data = {
        'Status': 200,
        'url': url,
    }

    if valid_url(url) == False:
        data['message'] = 'Invalid url'
    else:
        data['message'] = 'Valid url'
        #  get the url
        try:
            # new_window
            driver.execute_script('window.open("about:blank", "_blank");')
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)
            time.sleep(5)
            data['data'] = site_printer(url)
            data['error'] = False
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print('Error: ', e)
            data['data'] = None
            data['error'] = True
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            return jsonify(data)
    return jsonify(data)

def valid_url(url):
    # use urlparse to check validity... 
    if url == None:
        return False
    parsed_url = urlparse(url)
    if parsed_url.scheme == '':
        if parsed_url.netloc == '':
            if parsed_url.path != '':
                return True
            else:
                return False
        else:
            return False
    else:
        if parsed_url.netloc == '':
            if parsed_url.path != '':
                return True
            else:
                return False
        else:
            return True

def site_printer(url):
    try:
        # wait for page to load
        loaded = False
        while loaded == False:
                # check if page is loaded
                state = driver.execute_script('return document.readyState;')
                if state == 'complete':
                    loaded = True
                print('loading url:', url)
                time.sleep(2)
        results = driver.get_screenshot_as_base64()
        return results
    except:
        print('Error processing results of url:', url)
    finally:
        print('site printer end...')

if __name__ == '__main__':
    app.run()