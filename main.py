from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import os

chromedriver_path = "D:\chromedriver.exe"
driver = wd.Chrome(chromedriver_path)


def scroll_to_end():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)


def fetch_img_urls(search_query: str, image_count: int, target_path):
    driver.get('https://images.google.com/')
    search = driver.find_element(By.CLASS_NAME, "gLFyf.gsfi")
    search.send_keys(search_query)
    search.send_keys(Keys.RETURN)
    links = []
    img_src = []
    try:
        time.sleep(2)
        urls = driver.find_elements(By.CSS_SELECTOR, 'a.VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb')
        img_urls = driver.find_elements(By.CLASS_NAME, 'rg_i.Q4LuWd')

        while len(urls) & len(img_urls) < image_count:
            if len(urls) & len(img_urls) <= image_count:
                scroll_to_end()
                urls = driver.find_elements(By.CSS_SELECTOR, 'a.VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb')
                img_urls = driver.find_elements(By.CLASS_NAME, 'rg_i.Q4LuWd')
            else:
                pass

        print('no. of urls available on page =', len(urls))
        print('no. of img_urls available on page =', len(img_urls))

        urls = urls[:image_count]
        img_urls = img_urls[:image_count]

        for url in urls:
            links.append(url.get_attribute("href"))
        print('no. of links collected = ', len(links))

        for img_url in img_urls:
            img_url.click()

            time.sleep(2)
            actual_images = driver.find_elements(By.CSS_SELECTOR, 'img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    img_src.append(actual_image.get_attribute('src'))

        print('no. of img src collected = ', len(img_src))

        try:

            target_path = r'D:\New folder/images'
            target_folder = os.path.join(target_path, '_'.join(search_query.lower().split(' ')))

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            counter = 0
            for src in img_src:

                image_content = requests.get(src).content

                try:
                    f = open(os.path.join(target_folder, 'jpg' + "_" + str(counter) + ".jpg"), 'wb')
                    f.write(image_content)

                    f.close()
                    print(f"SUCCESS - saved {url} - as {target_folder}")
                    counter += 1
                except Exception as e:
                    print(f"ERROR - Could not save {url} - {e}")


        except Exception as e:
            print('error mf', e)

        driver.quit()

    except Exception as e:
        print(f'error{e}')
        driver.quit()


fetch_img_urls("meme",20,r'D:\New folder/images')
