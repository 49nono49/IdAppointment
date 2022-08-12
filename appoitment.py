from pydoc import classname
import types
from typing import Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from discordBot import *
import argparse, signal, sys, time

# init param
parser = argparse.ArgumentParser(description='Information')
parser.add_argument('-b','--browser', dest='browser', type=str,
                    help='Enable browser y/Y n/N, default yes', default='y')
parser.add_argument('-m','--mode', dest='mode', type=str,
                    help='id i/I or passport p/P appoitment', default='p')                    
args = parser.parse_args()


def signal_handler(signum: int, _p_stack_frame: Optional[types.FrameType] = None) -> None:
    """Terminate the thread.

    :param signum: The signal code value.
    :type signum: int
    :param _p_stack_frame: The frame that was interrupted by the signal, defaults to None
    :type _p_stack_frame: Optional[types.FrameType], optional
    """
    print("Wait to stop thread")
    clientDiscord.stop()
    clientDiscord.join()
    sys.exit(signum)
# Add signal handler
signal.signal(signal.SIGINT, signal_handler)  # Interrupt from keyboard (CTRL + C)
signal.signal(signal.SIGTERM, signal_handler)  # Termination signal


try:
    PATH_CHROME_DRIVER = config('PATH_CHROME_DRIVER')
except:
    print("Warning : PATH_CHROME_DRIVER is not define in .env file. The default value is use")
    PATH_CHROME_DRIVER = './usr/shares/bin'

# secondes
try:
    TIME_TO_TESTING_APPOITMENT = int(config('TIME_TO_TESTING_APPOITMENT'))
except:
    TIME_TO_TESTING_APPOITMENT = 60



clientDiscord: ThreaderBot = ThreaderBot()
chrome_options = Options()

if args.browser.upper() == 'N':
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")  # linux only
    chrome_options.add_argument("--headless")

# url passport appoitment
if args.mode.upper() == 'P':
    print("mode : Passport appoitment")
    URL_APPOITMENT  =  "https://www.clicrdv.com/mairie-de-saint-herblain?freeze=interventionsets&intervention_ids%5B%5D=2724116&interventionset_ids%5B%5D=232064&interventionset_ids%5B%5D=232066&nofooter=1&nologo=1&popin=1"
elif args.mode.upper() == 'I':
    print("mode : ID appoitment")
    URL_APPOITMENT  = "https://www.clicrdv.com/mairie-de-saint-herblain?freeze=interventionsets&intervention_ids%5B%5D=2724107&interventionset_ids%5B%5D=232064&interventionset_ids%5B%5D=232066&nofooter=1&nologo=1&popin=1"
else:
    print("Bad mode in parameter")
    exit(1)



chrome_options.executable_path = PATH_CHROME_DRIVER
driver = webdriver.Chrome(options=chrome_options)

i = 0
while True:

    driver.get(URL_APPOITMENT)
    # wait all element are load
    time.sleep(0.5)
    try:
        # click on selector
        spanA = driver.find_elements(By.CLASS_NAME, 'placeholder')
        spanA[0].click()
        time.sleep(0.2)
        element = driver.find_elements(By.CLASS_NAME, 'yui3-menuitem')
        # select a city all   element 8, 9 or 10
        element[8+i].click()
        # wait element load
        time.sleep(1)
        # get element no appoitement
        # if this element is not present a  exception is raise
        element = driver.find_element(
            By.XPATH, '//*[text()="Aucun créneau disponible à la prise de rdv par internet pour votre sélection. Merci de modifier votre sélection."]')

        i = i+1
        i = i % 3

        if i == 0:
            time.sleep(TIME_TO_TESTING_APPOITMENT)

    except Exception as e:
        msg = f"Hey un rendez-vous est dispo : "+ URL_APPOITMENT
        l = asyncio.get_event_loop()

        l.create_task(clientDiscord.sendMessage(msg))
        driver.close()
        break
