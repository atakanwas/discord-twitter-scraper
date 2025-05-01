# Discord Twitter Scraper 🐦💻

![GitHub Repo Size](https://img.shields.io/github/repo-size/atakanwas/discord-twitter-scraper)
![GitHub Issues](https://img.shields.io/github/issues/atakanwas/discord-twitter-scraper)
![GitHub License](https://img.shields.io/github/license/atakanwas/discord-twitter-scraper)

Welcome to the **Discord Twitter Scraper**! This project allows you to automatically scrape connected Twitter/X accounts from Discord member profiles using Selenium and undetected_chromedriver. If you want to dive right in, check out the [Releases](https://github.com/atakanwas/discord-twitter-scraper/releases) section for the latest version.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

## Features

- **Automated Scraping**: Effortlessly gather Twitter accounts linked to Discord profiles.
- **Selenium Integration**: Utilizes Selenium for web automation.
- **Undetected Chrome Driver**: Bypass detection mechanisms with undetected_chromedriver.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **User-Friendly**: Easy to set up and use.

## Technologies Used

- **Python**: The primary programming language.
- **Selenium**: For browser automation.
- **undetected_chromedriver**: To avoid detection by websites.
- **Discord API**: To interact with Discord member profiles.
- **Twitter API**: To fetch Twitter account details.

## Installation

To get started, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/atakanwas/discord-twitter-scraper.git
   cd discord-twitter-scraper
   ```

2. **Install Required Packages**:
   Make sure you have Python installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Latest Release**:
   Visit the [Releases](https://github.com/atakanwas/discord-twitter-scraper/releases) section, download the latest version, and execute the script.

## Usage

To run the scraper, execute the following command in your terminal:

```bash
python scraper.py
```

### Configuration

Before running the scraper, you may need to configure your Discord and Twitter API credentials. Edit the `config.py` file with your API keys and other necessary settings.

### Example Command

```bash
python scraper.py --guild_id YOUR_GUILD_ID
```

Replace `YOUR_GUILD_ID` with the ID of the Discord server you want to scrape.

## Contributing

We welcome contributions! If you want to help improve the project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, feel free to reach out:

- **Author**: Atakan Was
- **Email**: atakanwas@example.com
- **GitHub**: [atakanwas](https://github.com/atakanwas)

Thank you for checking out the **Discord Twitter Scraper**! We hope you find it useful for your automation and data extraction needs. Don't forget to visit the [Releases](https://github.com/atakanwas/discord-twitter-scraper/releases) section for updates and new features!