# European-Youth-Portal-Scraper
This Python program scrapes the [European Youth Portal](https://youth.europa.eu/go-abroad/volunteering/opportunities_en) Opportunities to gather 
information on volunteering opportunities available for your country. The program saves
this information in a CSV file called "opportunities.csv". The purpose of the program 
is to allow users to easily filter through the volunteering opportunities available on 
the website by their country, as the website currently does not offer this functionality.

## Technologies/Libraries Used
1. Selenium
2. CSV

## Setup
1. Clone the repository:
git clone https://github.com/your_username/volunteering-opportunities-scraper.git
2. Navigate to the project directory:
`cd volunteering-opportunities-scraper`
3. Install the required dependencies:
`pip install -r requirements.txt`
3. In the constants.py file, assign your country code to the MY_COUNTRY variable. For example, if you're in Italy, you would assign 'Italy' to the variable:
`MY_COUNTRY = 'Italy'`
4. Run the program:
`python main.py`
The program will open a Chrome window and start scraping the opportunities for your country. The results will be saved in a file named opportunities.csv. 

## License
This project is licensed under the MIT License. See the LICENSE.md file for details.

## Notes
Please be respectful when scraping websites and do not overload their servers with requests. This program is intended for personal use only.
