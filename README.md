# Mercado Livre Web Scraping Script

This script automates the process of collecting product information from the Mercado Livre website through web scraping. It allows you to quickly gather details about various products based on your search term.

## Introduction

Web scraping is the practice of extracting information from websites. This script uses Python and libraries like `requests` and `BeautifulSoup` to fetch product data, including product names, prices, and links, from the Mercado Livre website. It also provides a graphical user interface (GUI) for user interaction.

## Getting Started

### Prerequisites

Before using this script, you need to have Python and a few Python libraries installed:

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `openpyxl` library
- `PySimpleGUI` library

You can install these libraries using the following command:

```bash
pip install requests beautifulsoup4 openpyxl PySimpleGUI
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/faellm/web-scraping-Mercado-Livre.git
```

2. Navigate to the project directory:

```bash
cd web-scraping-Mercado-Livre
```

## Usage

1. Run the script by executing:

```bash
python main.py
```

2. A GUI window will appear, prompting you to enter your search term.

3. Type the keyword for the product you want to search (e.g., "phone", "laptop").

4. Click the "Search" button.

5. The script will fetch information about the products related to your search term and display them on the console. It will also save the information in an Excel file named "data.xlsx" in the same directory.

## Features

- **GUI Interface:** The script provides a simple graphical interface using `PySimpleGUI` to input search terms easily.
- **Automated Scraping:** The script automates the process of web scraping, saving time and effort.
- **Excel Export:** Scraped data is saved in an Excel file for easy analysis and reference.
