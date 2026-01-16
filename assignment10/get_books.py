from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import json
import os

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 15)

    try:
        print("Opening", url)
        driver.get(url)

        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"li.cp-search-result-item")))
        print("LI results found", len(results))

        print("\n---First LI Preview-----")
        print(results[0].text[:400])
        print("---- end preview ----\n")

        extracted = []
        for li in results:
            try:
                title = li.find_element(By.CSS_SELECTOR, "h3 a").text.strip()
            except:
                title=""

            
            authors = []
            try:
                author_links = li.find_elements(By.CSS_SELECTOR,"a")
                for a in author_links:
                    t = a.text.strip()
                    if t and t !=title:
                        authors.append(t)
            except:
                pass

            author_text = "; ".join(dict.fromkeys(authors))

            try:
                format_year = li.find_element(By.CSS_SELECTOR,"span.display-info-primary").text.strip()
            except:
                format_year = ""

            extracted.append({
                "Title": title,
                "Author": author_text,
                "Format-Year": format_year
            })

        df = pd.DataFrame(extracted)

        print(df.head(10))

        out_dir = os.path.dirname(__file__)
        csv_path = os.path.join(out_dir, "get_books.csv")
        json_path = os.path.join(out_dir,"get_books.json")

        df.to_csv(csv_path, index=False, encoding="utf-8")

        with open("get_books.json", "w", encoding="utf-8") as f:
                json.dump(extracted, f, indent=2, ensure_ascii=False)

    finally:
        driver.quit()

if __name__ =="__main__":
    main()
