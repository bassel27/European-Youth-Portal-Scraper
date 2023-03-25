# -*- coding: utf-8 -*-
from scrapper import Scraper
from constants import *
from opp import Opp
import csv


def write_header_to_csv():
    with open("opportunities.csv", "w", newline="", encoding='utf-8') as file:
        header = [
            "Opportunity",
            "topics",
            "description",
            "profile",
            "accommodation",
            "training",
            "dates",
            "deadline",
            "location",
            "url",
        ]
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)


def append_to_csv(data):
    with open("opportunities.csv", "a", newline="", encoding='utf-8') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(data)


scraper = Scraper()
scraper.fetch_url(PORTAL_URL)
scraper.accept_cookies()
data = []
write_header_to_csv()
i = 0
while True:
    for i in range(i,i + 8):
        scraper.open_opp_in_new_tab(i)
        if scraper.is_my_country_included():
            data.append(
                [
                    scraper.get_opp_title(),
                    scraper.get_topics(),
                    scraper.get_description(),
                    scraper.get_profile(),
                    scraper.get_accommodation(),
                    scraper.get_training(),
                    scraper.get_dates(),
                    scraper.get_deadline(),
                    scraper.get_location(),
                    scraper.get_current_url(),
                ]
            )
            append_to_csv(data)
            data = []
        scraper.close_current_tab()
        scraper.switch_to_main_window()
        i += 1
    scraper.load_more()
