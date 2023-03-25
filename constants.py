PORTAL_URL = "https://youth.europa.eu/go-abroad/volunteering/opportunities_en"
WAIT_TIME = 10
OPP_XPATH = '//a[@class="waves-effect waves-light btn"]'
ACCEPT_COOKIES_XPATH = (
    '//a[@class="wt-link wt-ecl-button wt-ecl-button--primary cck-actions-button"]'
)
CLOSE_COOKIES_XPATH = '//span[@class="wt-ecl-button__container"]'
MY_COUNTRY = "Egypt"
COUNTRIES_XPATH = '((//div[@class="box"])/p)[3]'
TITLE_XPATH = '//section[@class="col-sm-12"]/h1'
DATES_XPATH = '((//div[@class="box"])/p)[1]'
LOCATION_XPATH = '((//div[@class="box"])/p)[2]'
DEADLINE_XPATH = '//div[@class="box"]/p[contains(text(), "deadline")]'
TOPICS_XPATH = '(//div[@class="box"])[2]/p[i[@class="fa fa-check"]]'

GENERAL_XPATH = '//div[@class="box"]/text()[position()='
DESCRIPTION_XPATH = GENERAL_XPATH + "2]"
ACCOMMODATION_XPATH = GENERAL_XPATH + "3]"
TRAINING_XPATH = GENERAL_XPATH + "4]"
PROFILE_XPATH = GENERAL_XPATH + "5]"
LOAD_MORE_BUTTON_XPATH = '//*[@id="eyp-volunteering-opportunities-list"]/div/div[4]/div/button'