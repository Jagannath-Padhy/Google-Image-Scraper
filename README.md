# Google Image Scraper
  Searches for the query on Google images and downloads the requested amount of images and stores it
  on local drive

## To run
  * Download the Chromedriver of the same version of chrome installed in your system and update the       path in chromedriver_path.
  * To Begin the download, Run fetch_img_urls with Query(str) ,No. of images(int) required and 
    folder directory; eg:- fetch_img_urls('bmw',20,r'D:\New folder/images')
  * Incase you have a slow internet connection try increasing the time.sleep().