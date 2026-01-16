from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

def main():
    url = "https://owasp.org/Top10/2025/"
    out_dir = os.path.dirname(__file__)
    csv_path = os.path.join(out_dir, "owasp_top_10.csv")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    wait = WebDriverWait(driver, 15)

    try:
        print(f"Opening {url}")
        driver.get(url)

        wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "body")))

        anchors = driver.find_elements(
            By.XPATH,
            "//ol/li/a[starts-with(normalize-space(.), 'A0') or starts-with(normalize-space(.), 'A10')]"
        )
        print("Anchors found:", len(anchors))
        if anchors:
            print("First anchor text:", anchors[0].text)
            print("First anchor href:", anchors[0].get_attribute("href"))

        results = []
        seen = set()

        for a in anchors:
            title = a.text.strip()
            href = a.get_attribute("href")


            if not title.startswith("A0"):
                continue
            code = title.split(":")[0].strip()

            if code not in [f"A0{i}" for i in range(1, 10)]+ ["A10"]:
                continue

            key = (code, href)

            if key in seen:
                continue
            seen.add(key)

            results.append({"Vulnerability": title, "Link": href})

            results.sort(key=lambda d: int(d["Vulnerability"].split(":")[0].replace("A","")))

        print("\nExtracted OWASP Top 10:")

        print(results)

        df = pd.DataFrame(results)
        df.to_csv(csv_path, index=False, encoding="utf-8")
        print(f"\nWrote CSV: {csv_path}")

    finally:
        driver.quit()

if __name__ =="__main__":
    main()
