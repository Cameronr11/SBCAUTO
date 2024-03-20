from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import traceback
import sqlite3
from extensions import socketio

#dependencies: selenium, pandas, sqlite3, socketio


class Gather:

    def init(self, scraped_players):
        self.scraped_players = scraped_players


    #signing into web app
    chrome_driver_path = "C:\\Program Files (x86)\\chromedriver.exe"

    chrome_binary_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    chrome_options.page_load_strategy = 'eager'  # Options: 'none', 'eager', 'normal'

    driver = webdriver.Chrome(options=chrome_options)

    def openEAFC(self):
        Gather.driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")

    def pressLogin(self):
        #trying to access login button
        xpath_expression = "//button[contains(text() , 'Login')]"
        #retryable mechanism
        max_attempts = 5
        for i in range(max_attempts):
            try:
                login_button = WebDriverWait(Gather.driver, 45).until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
                login_button.click()
                break
            except:
                print("couldn't click login button")

    def inputLogin(self,username,password):
        #trying to input login credentials
        #find fields
        try:
            findUsername = Gather.driver.find_element(By.NAME, "email")
            findPassword = Gather.driver.find_element(By.NAME, "password")
        except:
            print("couldnt find field")
        try:
            #input credentials
            findUsername.send_keys(username)
            findPassword.send_keys(password)
        except:
            print("coudlnt input credentials")

    #credentials are inputted but sign in button not being clicked
    def click_sign_in(self):
        max_attempts_sign_in = 5
        for i in range(max_attempts_sign_in):
            try:
                sign_in_button = WebDriverWait(Gather.driver, 45).until(EC.presence_of_element_located((By.ID, "logInBtn")))


                Gather.driver.execute_script("arguments[0].click();", sign_in_button)
                break
            except:
                print("Coulnd't sign in")


            
    #2FA Code: For now we will input the code 
    #manually to move on will just need to design the website to ask for their code. 
    def check_if_2FA(self):
        try:
            print("attempting to find 2FA button in check")
            send_2FA_code_button = WebDriverWait(Gather.driver, 45).until(EC.element_to_be_clickable((By.ID, "btnSendCode")))
            print("found 2FA button in check")
            send_2FA_code_button.click()
            print("clicked 2FA button in check")
            return True
        except:
            print("No 2FA to check")
            return False
    

    def handle_2FA(self, code=None):
        try:
            print("attempting to find 2FA button in handle")
            send_2FA_code_button = WebDriverWait(Gather.driver, 45).until(EC.element_to_be_clickable((By.ID, "btnSendCode")))
            print("found 2FA button in handle")
            send_2FA_code_button.click()
            print("clicked 2FA button in handle")
        except:
            print("Couldn't send 2FA code")
        #we have to check if the 2FA screen is present
        if "verificationGate" in Gather.driver.page_source:
            print("2FA Page Found. Please intput the code that was sent to your email")
            Verification_code = code
            try:
                Verification_code_input = WebDriverWait(Gather.driver, 45).until(EC.presence_of_element_located((By.ID, "twoFactorCode")))
                Verification_code_input.send_keys(Verification_code)
                sign_in_button_2FA = WebDriverWait(Gather.driver, 45).until(EC.element_to_be_clickable((By.ID, "btnSubmit")))
                sign_in_button_2FA.click()
            
            except:
                print("Couldn't finish 2FA")
        else:
            print("No 2FA to Handle")

    # We are now passed the 2FA page. We are sitting at the main
    #Web app page
    #right here we need to create a statement that says if the continue button is on the screen then click it if not just continue to club button

    def click_Club(self):
        #Club button
        max_attempts_club = 5
        club_button_clicked = False
        for i in range(max_attempts_club):
            try:
                club_button = WebDriverWait(Gather.driver, 45).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ut-tab-bar-item') and contains(@class, 'icon-club')]")))
                club_button.click()
                club_button_clicked = True
                break
            except:
                print("Club button couldn't be clicked")

    def click_Players(self):
        #Players Button
        max_attempts_players = 5
        players_button_clicked = False
        for i in range(max_attempts_players):
            try:
                players_button = WebDriverWait(Gather.driver, 45).until(EC.element_to_be_clickable((By.CLASS_NAME, "tile.col-2-3-md.players-tile")))
                print("trying to find number of players")
                num_total_players = WebDriverWait(players_button, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ut-label-view--label")))
                print("found total number of players")
                num_total_players_text = num_total_players.text
                print("turned the number of players into text")
                num_players = int(num_total_players_text.split()[0])
                print("split the number of players into just the integer value")
                print(f"Number of players to scrape: {num_players}")
                socketio.emit('num_players', {'num_players': num_players})
                players_button.click()
                players_button_clicked = True
                break
            except:
                print("Couldn't click players")

        try:
            WebDriverWait(Gather.driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME, 'listFUTItem')))
        except:
            print("Error: Player page did not render within the expected time.")


    #Above code gets us to the list of players a user owns

    def is_loan_player(self,card):
        attribute = 'class'
        classes = card.find_element(By.CLASS_NAME, 'small').get_attribute(attribute)
        return classes and 'loan' in classes.lower()


    def scraped_num_setter(self):
        self.scraped_players = 0
    def scrape_page(self,driver):

        paginated_list = WebDriverWait(driver,45).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.paginated-item-list.ut-pinned-list ul.paginated')))

        player_cards = paginated_list.find_elements(By.CSS_SELECTOR, 'li.listFUTItem')

        all_player_names_1page = []
        all_player_ratings_1page = []
        all_player_leagues_1page = []
        all_player_clubs_1page = []
        all_player_nations_1page = []
        all_player_rarities_1page = []
        all_player_pp_1page = []
        all_player_ap_1page = []
            # Assuming card is an index
        for card in player_cards:
            if not self.is_loan_player(card):
                try:
                    self.scraped_players += 1
                    socketio.emit('scraped_players', {'scraped_players': self.scraped_players})
                    time.sleep(1)
                    player_button = WebDriverWait(card, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.rowContent.has-tap-callback')))
                    player_button.click()
                    more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.more')))
                    more_button.click()
                except Exception as e:
                    print(f"Error getting to player info: {e}")
                    # You might want to handle this error case

                parent_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'pseudo-table')))
                name_element = parent_element.find_element(By.XPATH, "//li[h1='Full Name']/h2").text
                rarity_element = parent_element.find_element(By.XPATH, "//li[h1='Rarity']/h2").text
                league_element = parent_element.find_element(By.XPATH, "//li[h1='League']/h2").text
                club_element = parent_element.find_element(By.XPATH, "//li[h1='Club']/h2").text
                try:
                    parent_element_alt = parent_element.find_element(By.XPATH, "//li[h1='Alternate positions ']/h2")
                    alt_position_elements = parent_element_alt.find_element(By.XPATH, "//li[h1='Alternate positions ']/h2").text.split(', ')
                except:
                    alt_position_elements = ['N/A']

                preferred_position_element = parent_element.find_element(By.XPATH, "//li[h1='Preferred Position']/h2").text
                nation_element = parent_element.find_element(By.XPATH, "//li[h1='Nation']/h2").text

                #finding rating
                rating_element = card.find_element(By.CSS_SELECTOR, '.playerOverview .rating').text



                all_player_ratings_1page.append(rating_element)
                all_player_names_1page.append(name_element)
                all_player_pp_1page.append(preferred_position_element)
                all_player_clubs_1page.append(club_element)
                all_player_nations_1page.append(nation_element)
                all_player_ap_1page.append(alt_position_elements)
                all_player_rarities_1page.append(rarity_element)
                all_player_leagues_1page.append(league_element)



                # Locate the back button within the parent element
                parent_element_for_first_back_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.ut-navigation-bar-view.navbar-style-secondary')))
                back_button = WebDriverWait(parent_element_for_first_back_button, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.ut-navigation-button-control')))
                back_button.click()
            else:
                continue
        return all_player_names_1page, all_player_clubs_1page, all_player_ratings_1page, all_player_nations_1page, all_player_leagues_1page, all_player_pp_1page, all_player_ap_1page, all_player_rarities_1page

    def scrape_Save(self):

        all_player_names = []
        all_player_ratings = []
        all_player_leagues = []
        all_player_clubs = []
        all_player_nations = []
        all_player_rarities = []
        all_player_pp = []
        all_player_ap = []


        while True:
            try:
                time.sleep(1) #time to allow ratings to render
                all_player_names_1page, all_player_clubs_1page, all_player_ratings_1page, all_player_nations_1page, all_player_leagues_1page, all_player_pp_1page, all_player_ap_1page, all_player_rarities_1page = self.scrape_page(self.driver)

                
                all_player_ratings.extend(all_player_ratings_1page)
                all_player_names.extend(all_player_names_1page)
                all_player_pp.extend(all_player_pp_1page)
                all_player_clubs.extend(all_player_clubs_1page)
                all_player_nations.extend(all_player_nations_1page)
                all_player_ap.extend(all_player_ap_1page)
                all_player_rarities.extend(all_player_rarities_1page)
                all_player_leagues.extend(all_player_leagues_1page)




                next_button = WebDriverWait(Gather.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.flat.pagination.next')))
                next_button.click()

                #find a way to hit the next button so we can get the next page and then we are done for right now with gather.py
            except:
                print("No more Pages Exiting Loop")
                break
        
        zipped_data = list(zip(all_player_names, all_player_ratings, all_player_pp, all_player_ap, all_player_leagues, all_player_rarities, all_player_nations, all_player_clubs ))



        df = pd.DataFrame(zipped_data, columns = ['Name', 'Rating', 'PrefPosition', 'Alt_position', 'League', 'Rarity', 'Nation', 'Club' ])
        df.to_csv('Scraped_player_data.csv', index= False)

        try:
            df = pd.read_csv('Scraped_player_data.csv')
            connection = sqlite3.connect('Scraped_Player_Database.db')
            df.to_sql('players', connection, index=False, if_exists='replace')
            connection.commit()

            cursor = connection.cursor()
            cursor.execute('SELECT * FROM players')
            rows = cursor.fetchall()
            count = 0
            for row in rows:
                print(row)
                count = count +1

            print(f"player count: {count}")
            cursor.close()
            connection.close()
        except Exception as e:
            print(f"some players aren't being added: {e}")

    def scrape_user_club(self, username, password, code):
        Gather.openEAFC(self)
        Gather.pressLogin(self)
        Gather.inputLogin(self,username,password)
        Gather.click_sign_in(self)
        Gather.handle_2FA(self, code)
        Gather.click_Club(self)
        Gather.click_Players(self)
        Gather.scraped_num_setter(self)
        Gather.scrape_Save(self)
        print("Scraping Complete")
        self.driver.quit()

    def scrape_without_2FA(self, username, password):
        Gather.openEAFC(self)
        Gather.pressLogin(self)
        Gather.inputLogin(self,username,password)
        Gather.click_sign_in(self)
        Gather.click_Club(self)
        Gather.click_Players(self)
        Gather.scraped_num_setter(self)
        Gather.scrape_Save(self)
        print("Scraping Complete")
        self.driver.quit()

    def is_2FA(self, username, password):
        Gather.openEAFC(self)
        Gather.pressLogin(self)
        Gather.inputLogin(self,username,password)
        Gather.click_sign_in(self)
        return Gather.check_if_2FA(self)