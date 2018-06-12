"""
@package base
WebDriver Factory class implementation
It creates a webdriver instance based on configurations
Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver

class WebDriverFactory():

    def __init__(self,browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer envioronment based on OS
        
        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"]= chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        
        PREFERRED: Set the path on the machine where browser will be executed
    """
    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """
        baseURL = "http://automationpractice.com/index.php/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for an element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver