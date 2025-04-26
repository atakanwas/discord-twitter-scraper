import time
import os
import random
import re
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === CONFIG ===
DISCORD_URL = "https://discord.com/channels/1083381867664904212/1083381868176625766"
OUTPUT_FILE = "twitter_links.txt"
CHROME_PROFILE_PATH = "C:/Users/admin1/AppData/Local/Google/Chrome/User Data"
PROFILE_NAME = "Default"

# === SETUP CHROME ===
options = uc.ChromeOptions()
options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
options.add_argument(f"--profile-directory={PROFILE_NAME}")
driver = uc.Chrome(options=options)

driver.get(DISCORD_URL)

banner = r"""

    ____  _                          __   _____                                
   / __ \(_______________  _________/ /  / ___/______________ _____  ___  _____
  / / / / / ___/ ___/ __ \/ ___/ __  /   \__ \/ ___/ ___/ __ `/ __ \/ _ \/ ___/
 / /_/ / (__  / /__/ /_/ / /  / /_/ /   ___/ / /__/ /  / /_/ / /_/ /  __/ /    
/_____/_/____/\___/\____/_/   \__,_/   /____/\___/_/   \__,_/ .___/\___/_/     
                                                           /_/                 
                          Made by https://t.me/Bytebl33d3r
"""

print(banner)
input("🟢 Press ENTER when ready to begin scraping...")

twitter_links = set()

# (Your scraping functions go here...)
# === rest of your script continues from here ===


def normalize_link(link):
    link = link.replace("www.", "").replace("mobile.", "").rstrip("/")
    match = re.match(r"https?://(?:x|twitter)\.com/([^/]+)", link)
    if match:
        username = match.group(1)
        return f"https://x.com/{username}"
    return link

def try_open_full_bio():
    try:
        view_bio_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "viewFullBio_f5f93a")]'))
        )
        driver.execute_script("arguments[0].click();", view_bio_button)
        time.sleep(random.uniform(0.2, 0.4))
        print("📖 Clicked 'View Full Bio'.")
        return True
    except:
        print("ℹ️ No 'View Full Bio' button, scraping mini-profile.")
        return False

def extract_twitter():
    expanded = try_open_full_bio()

    try:
        connections = driver.find_elements(By.XPATH, '//div[contains(@class, "connectedAccountNameText_e6abe8")]')
        for conn in connections:
            username = conn.get_attribute("aria-label")
            if username:
                link = normalize_link(f"https://x.com/{username}")
                if link not in twitter_links:
                    twitter_links.add(link)
                    print(f"✅ Found (Connection): {link}")

        bio_links = driver.find_elements(By.XPATH, '//a[contains(@class, "anchor_edefb8") and (contains(@href, "twitter.com") or contains(@href, "x.com"))]')
        for link in bio_links:
            href = link.get_attribute("href")
            if href:
                clean_href = normalize_link(href)
                if clean_href not in twitter_links:
                    twitter_links.add(clean_href)
                    print(f"✅ Found (Bio Link): {clean_href}")

    except Exception as e:
        print(f"❌ Error scraping profile: {e}")

def close_modal():
    try:
        body = driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.ESCAPE)
        time.sleep(random.uniform(0.1, 0.2))
    except:
        pass

def scrape_members_scroll_locked():
    print("📜 Starting scroll-locked scrape...")
    scroll_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "members_c8ffbb")]'))
    )

    seen_ids = set()
    stuck_count = 0
    max_stuck_scrolls = 5

    while stuck_count < max_stuck_scrolls:
        members = driver.find_elements(By.XPATH, '//div[contains(@class, "member__5d473") and contains(@class, "clickable__91a9d")]')
        new_found = False

        for member in members:
            try:
                member_id = member.get_attribute("data-list-item-id")
                if member_id in seen_ids:
                    continue

                seen_ids.add(member_id)
                new_found = True

                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", member)
                time.sleep(random.uniform(0.4, 0.6))
                member.click()
                time.sleep(random.uniform(0.4, 0.8))

                WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]'))
                )
                extract_twitter()
                close_modal()

            except Exception as e:
                print(f"❌ Error on member: {e}")
                close_modal()

        if not new_found:
            stuck_count += 1
        else:
            stuck_count = 0

        driver.execute_script("arguments[0].scrollBy(0, 800);", scroll_box)
        time.sleep(random.uniform(0.3, 0.6))

    print(f"🏁 Finished. Scraped {len(seen_ids)} unique members.")

# === MAIN EXECUTION ===
try:
    scrape_members_scroll_locked()
except KeyboardInterrupt:
    print("\n🛑 CTRL+C detected. Saving progress...")

# === SAVE RESULTS CLEANLY ===
deduped_links = sorted(twitter_links)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for link in deduped_links:
        f.write(link + "\n")

print(f"✅ Done. Saved {len(deduped_links)} links to {OUTPUT_FILE}")
driver.quit()
