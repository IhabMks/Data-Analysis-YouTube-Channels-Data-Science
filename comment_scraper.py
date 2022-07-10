from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


import json
import random
import time
import re


with open(r"Data\json\video_id.json") as f:
    data = json.load(f)

try:
    with open(r"Data\json\catched_unprocessed_ids.json", "r") as file:
        catched_ids = json.load(file)
    
    if len(catched_ids) != 0:
        for key, value in data.copy().items():
            if value in catched_ids:
                del data[key]

except Exception as e:
    print(e)


def scroll_down():
    #Small step down before scroll
    html = browser.find_element(by=By.TAG_NAME, value="body")
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    last_height = browser.execute_script("return document.documentElement.scrollHeight")
    while True:
    # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        # Wait to load page
        time.sleep(3.5)
        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

base_link = "https://www.youtube.com/watch?v="
options = Options()
options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
# The Chromedriver should be compatible with the used browser.
# In case the Chromedriver isn't in the same folder, do specify the full path to it.
browser = webdriver.Chrome(options = options, service = Service("chromedriver.exe"))

com_dict = dict()
catched_ids = []
start_time = time.time()
count = 0

for id in data.values():
    try:
        browser.get(base_link + id)
        time.sleep(5)
        scroll_down()
        comment_container = browser.find_elements(By.XPATH,"""//*[@id="content-text" and @class="style-scope ytd-comment-renderer"]""")
        comment_list = []
        for comment_index in range(len(comment_container)):
            try:
                raw_comment = comment_container[comment_index].text
                if len(raw_comment) != 0:
                    comment = re.sub("[^A-Za-z0-9]+"," ",raw_comment).strip()
                    comment_list.append(comment)
            except:
                pass
        print(f"Step {count}: ==> Id: {id} ==> {len(comment_list)} comment(s) scrapped..")
        com_dict.update({id:comment_list})
        for i in reversed(range(random.randint(7,14))):
            print(f"\r{i} seconds until next page...", end="", flush=True)
            time.sleep(1)
        count+=1
    except Exception as e:
        catched_ids.append(key)
        print(f"Error -> {e}")
        print("**************************")
        print(f"video Id: {key} - has been added to the catched list.")

with open(r"Data\json\catched_unprocessed_ids.json", "w") as file:
    json.dump(catched_ids, file)

with open(r"Data\json\ytb_com.json", "w") as file:
    json.dump(com_dict, file, indent=6, separators=(",",":"))

time_elapsed = round(time.time() - start_time,2)
print(f"\nExecution time: {time_elapsed} seconds")
browser.quit()