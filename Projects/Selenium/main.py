from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from urllib.parse import urljoin, urlparse

# Setup options for headless crawling
options = Options()
options.headless = True  # Optional: run browser in background

# Create WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Crawl the homepage
    url = "https://ircsl.gov.lk"
    driver.get(url)

    # Delay to wait for page to load
    time.sleep(2)

    # Print page title
    print("Page Title:", driver.title)

    # Extract all <a> tags
    links = driver.find_elements("tag name", "a")
    print("\nFound Links:")
    visited = set()
    for link in links:
        href = link.get_attribute("href")
        if href:
            href = urljoin(url, href)  # resolve relative URLs
            parsed = urlparse(href)
            if parsed.path.startswith("/wp-admin/"):
                continue  # Respect robots.txt
            if href not in visited:
                print(href)
                visited.add(href)

finally:
    driver.quit()
