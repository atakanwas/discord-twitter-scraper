# Discord Twitter/X Scraper 🕵️‍♂️
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  ![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
  ![Maintained](https://img.shields.io/badge/Maintained-yes-green.svg)

Scrape connected Twitter (X) accounts from Discord members quickly and easily.

## Features
- ✅ Scrolls through online members automatically
- ✅ Opens their profiles and extracts Twitter/X usernames
- ✅ Handles "View Full Bio" popups
- ✅ De-duplicates and saves clean profile links
- ✅ Built with undetected_chromedriver to avoid detection

## Demo
![2025-04-25 21-14-04](https://github.com/user-attachments/assets/105d4d68-4a75-4757-8b0a-587ccaa648f1)

## Requirements
- Python 3.10+
- Google Chrome (latest)
- ChromeDriver (auto-handled by undetected_chromedriver)

Install the Python libraries:

```bash
pip install selenium undetected-chromedriver

```
Setup:
```bash
git clone https://github.com/YOURUSERNAME/discord-twitter-scraper.git
```
```bash
cd discord-twitter-scraper
```
1. Edit the DISCORD_URL in discscraper.py to the channel you want to scrape.

2. Update CHROME_PROFILE_PATH and PROFILE_NAME to match your Chrome user settings (needed to stay logged in).

3. Run the script:
  ```bash
python discscraper.py
``` 

4. Press ENTER once Discord is loaded and members are visible.

5. Let it work. Links will be saved into twitter_links.txt when done.

Important Notes
Your Discord must already be logged in.

Only works in servers where you have access to the full member list.

For educational and research purposes only. I am not responsible for misuse.

Made with ❤️ by Bytebl33d3r

