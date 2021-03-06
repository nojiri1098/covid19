from selenium import webdriver
import os
import time
os.mkdir('ogp')

PATHS = {
    '/?dummy': [959,500],
    '/cards/details-of-confirmed-cases': [959,500],
    '/cards/number-of-confirmed-cases': [959,500],
    '/cards/attributes-of-confirmed-cases': [959,480],
    '/cards/number-of-tested': [959,540],
    '/cards/number-of-reports-to-covid19-consultation-desk': [959,500],
    '/cards/predicted-number-of-toei-subway-passengers': [959,750],
    '/cards/agency': [959,730],
}

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--hide-scrollbars")

driver = webdriver.Chrome(options=options)

for lang in ['ja', 'en', 'zh-cn', 'zh-tw', 'ko', 'ja-basic']:
    os.mkdir('ogp/'+lang)
    for path, size in PATHS.items():
        driver.set_window_size(size[0], size[1])
        if lang == 'ja':
            driver.get("http://localhost:8000"+path+"?ogp=true")
            time.sleep(5)
            driver.save_screenshot('ogp/'+path.replace('/cards/', '').replace('/', '_')+'.png')
        else:
            driver.get("http://localhost:8000/"+lang+path+"?ogp=true")
            time.sleep(5)
            driver.save_screenshot('ogp/'+lang+'/'+path.replace('/cards/', '').replace('/', '_')+'.png')
