import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # this is for drop down lists
from selenium.webdriver import Keys
import popcorn_locators as locators
# from faker import Faker
# fake = Faker(locale=['en_Ca', 'en_US'])


# s = Service(executable_path='C:\Automation\Python\Popcorn_project\chromedriver.exe')
# driver = webdriver.Chrome(service=s)

from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)




def setUp():
    print(f'-----Launch {locators.app} App.')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.popcorn_url)
    print(driver.title)

    if driver.current_url == locators.popcorn_url and driver.title == locators.popcorn_home_page_title:
        print(f'-----Yey! {locators.app} App website launched successfully!')
        print(f'-----{locators.app} homepage URL: {driver.current_url}, homepage title: {driver.title}')
        sleep(1)

    else:
        print(f'-----{locators.app} did not launched, check your code or application.')
        print(f'-----Current URL: {driver.current_url}, page title: {driver.title}')



def verify_service_page():
    driver.get(locators.popcorn_service_url)
    sleep(1)
    if driver.current_url == locators.popcorn_service_url and driver.title == locators.popcorn_service_title:
        print(f'----- We are in Service Page!!!!')
        print(f'-----{locators.app} Service page url: {driver.current_url}, homepage title: {driver.title}')
    else:
        print(f'----{locators.app} Service page, did not displayed.')
        sleep(1)

    assert driver.find_element(By.XPATH, '//h2[normalize-space()="STRATEGY & CONSULTING"]').is_displayed()
    strategy = driver.find_element(By.XPATH, '//h2[normalize-space()="STRATEGY & CONSULTING"]').is_displayed()
    print(f' Strategy and Consulting is displayed:{strategy}')
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(.,"LEARN MORE")]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/social-media-marketing/"]'
                                  '//span[@class="elementor-button-content-wrapper"]'
                                  '//span[@class="elementor-button-text"][normalize-space()="LEARN MORE"]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/digital-marketing/"]'
                                  '//span[@class="elementor-button-content-wrapper"]'
                                  '//span[@class="elementor-button-text"][normalize-space()="LEARN MORE"]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/influencer-marketing/"]'
                                  '//span[@class="elementor-button-content-wrapper"]'
                                  '//span[@class="elementor-button-text"][normalize-space()="LEARN MORE"]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/content-creation/"]'
                                  '//span[@class="elementor-button-content-wrapper"]'
                                  '//span[@class="elementor-button-text"][normalize-space()="LEARN MORE"]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)

    assert driver.find_element(By.XPATH, '//h2[normalize-space()="PUBLIC RELATIONS"]').is_displayed()
    pr = driver.find_element(By.XPATH, '//h2[normalize-space()="PUBLIC RELATIONS"]').is_displayed()
    print(f' PUBLIC RELATIONS is displayed:{pr}')
    sleep(1)

    driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/public-relations/"]'
                                  '//span[@class="elementor-button-content-wrapper"]'
                                  '//span[@class="elementor-button-text"][normalize-space()="LEARN MORE"]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)

    # assert is used to check Elements is displayed and its TRUE!
    assert driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xl"]').is_displayed()
    hwcwt = driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xl"]').is_displayed()
    print(f'HOW CAN WE WORK TOGETHER is displayed: {hwcwt}')
    sleep(1)
    print(f'All the service page Elements is clickable')
    sleep(1)



def jobs_page():
    driver.get(locators.popcorn_jobs_url)
    sleep(1)
    if driver.current_url == locators.popcorn_jobs_url and driver.title == locators.popcorn_jobs_title:
        print(f'----- We are in Jobs Page!!!!')
        print(f'-----{locators.app} Jobs page url: {driver.current_url}, Jobs title: {driver.title}')
    else:
        print(f'----{locators.app} Jobs page, did not displayed.')
        sleep(1)

    assert driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xxl"]').is_displayed()
    jobs = driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xxl"]').is_displayed()
    print(f' JOBS page is displayed: {jobs}')
    sleep(1)

    driver.find_element(By.XPATH, '//h3[normalize-space()="Account Executive"]').click()
    sleep(1)
    if driver.current_url == locators.popcorn_jobs_account_executive_url and driver.title == locators.popcorn_jobs_account_executive_title:
        sleep(3)
        print(f'You are in Account Executive page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Jobs"]').click()
        sleep(1)
    else:
        print(f'Something is wrong you are not is correct web page')

    driver.find_element(By.XPATH, '//h3[normalize-space()="Account Associate"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[normalize-space()="Jobs"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//strong[normalize-space()="Load more listings"]').click()
    print(f'All JOB Listing is visible')
    sleep(1)


def case_studies():
    driver.get(locators.popcorn_case_studies_url)
    if driver.current_url == locators.popcorn_case_studies_url and driver.title == locators.popcorn_case_studies_title:
        sleep(3)
        print(f'CASE STUDIES page is displayed')
        print(f'{locators.app} Case Studies url {locators.popcorn_case_studies_url}, Case studies {locators.popcorn_case_studies_title}')
    else:
        print(f'Something went wrong')
        sleep(1)

    assert driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xxl"]').is_displayed()
    CS = driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xxl"]').is_displayed()
    print(f'Case Studies page is displayed: {CS}')
    sleep(1)

    assert driver.find_element(By.XPATH, '//h2[normalize-space()="Here are a few examples of our work:"]').is_displayed()
    workexamples = driver.find_element(By.XPATH, '//h2[normalize-space()="Here are a few examples of our work:"]').is_displayed()
    print(f'Here are a few examples of our work title is displayed: {workexamples}')
    sleep(1)

    # Skype footware
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                     '//h3[@class="elementor-portfolio-item__title"][normalize-space()="SKYE Footwear"]').click()
    if driver.current_url == locators.popcorn_portfolio_skye_footware_url and driver.title == locators.popcorn_portfolio_skye_footware_title:
        print(f'You are in Skype Footware Page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # NETGEAR
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Netgear"]').click()
    if driver.current_url == locators.popcorn_portfolio_netgear_url and driver.title == locators.popcorn_portfolio_netgear_title:
        print(f'You are in Netgear page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # SAMSUNG
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Samsung"]').click()
    if driver.current_url == locators.popcorn_portfolio_samsung_url and driver.title == locators.popcorn_portfolio_samsung_title:
        print(f'Your are in SAMSUNG page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # NEST DESIGNS
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Nest Designs"]').click()
    if driver.current_url == locators.popcorn_portfolio_nest_design_url and driver.title == locators.popcorn_portfolio_nest_design_title:
        print(f'Your are in NEST DESIGN page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # Michael Hill Jewellery
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                      '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Michael Hill Jeweller"]').click()
    if driver.current_url == locators.popcorn_portfolio_michaelhilljewel_url and driver.title == locators.popcorn_portfolio_michaelhilljewel_title:
        print(f'Your are in MICHAEL HILL JEWELLERY page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # JUST EAT
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Just Eat (Skip The Dishes)"]').click()
    if driver.current_url == locators.popcorn_portfolio_justeat_url and driver.title == locators.popcorn_portfolio_justeat_title:
        print(f'Your are in JUST EAT (SKIP THE DISH) page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # PURDY CHOCOLATIER
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Purdys Chocolatier"]').click()
    if driver.current_url == locators.popcorn_portfolio_purdy_url and driver.title == locators.popcorn_portfolio_purdy_title:
        print(f'Your are in PURDY CHOCOLATIER page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # TOURISUM VANCOUVER
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Tourism Vancouver"]').click()
    if driver.current_url == locators.popcorn_portfolio_tourisum_vancouver_url and driver.title == locators.popcorn_portfolio_tourisum_vancouver_title:
        print(f'Your are in TOURISUM VANCOUVER page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # BETTER THAN BOUILLON
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Better Than Bouillon"]').click()
    if driver.current_url == locators.popcorn_portfolio_better_than_bouillon_url and driver.title == locators.popcorn_portfolio_better_than_bouillon_title:
        print(f'Your are in BETTER THAN BOUILLON page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # SHANGRI-LA HOTEL
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Shangri-La Hotel"]').click()
    if driver.current_url == locators.popcorn_portfolio_shangri_la_hotel_url and driver.title == locators.popcorn_portfolio_shangri_la_hotel_title:
        print(f'Your are in SHANGRI-LA HOTEL page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # VIRTUOUS PIE
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Virtuous Pie"]').click()
    if driver.current_url == locators.popcorn_portfolio_virtuous_pie_url and driver.title == locators.popcorn_portfolio_virtuous_pie_title:
        print(f'Your are in VIRTUOUS PIE page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # Canadian Federation of Independent Grocers - Popcorn
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Canadian Federation of Independent Grocers"]').click()
    if driver.current_url == locators.popcorn_portfolio_CFOIG_url and driver.title == locators.popcorn_portfolio_CFOIG_title:
        print(f'Your are in Canadian Federation of Independent Grocers - Popcorn page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    driver.find_element(By.XPATH, '//span[@class="elementor-button-text"]').click()
    sleep(1)


def tearDown():
    if driver is not None:
        print('------------------------------------~*~------------------------------------------------')
        print(f'-----The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


setUp()
# verify_service_page()
case_studies()
# jobs_page()
# tearDown()