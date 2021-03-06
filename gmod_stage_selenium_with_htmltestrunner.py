import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pyunitreport import HTMLTestRunner

#Chrome version 73.0.3683.86, ChromeDriver 73.0.3683.68
#Firefox version:58, Driver version:geckodriver24.0 
#IE version:11, IEDriverServer_x64_3.14.0
#Driver should put in the path of python36

class ContactTestCase(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get('https://gmod-stage.nal.usda.gov/register/project-dataset/account')

    #namespace must be test....
    def test_contact(self):
        driver=self.driver
        name_element = driver.find_element_by_name("name")
        name_element.send_keys("Test_Robot")
        print ('name_done')

        mail_element = driver.find_element_by_xpath("//*[@id='edit-email']")
        mail_element.send_keys("monica.poelchau@ars.usda.gov")
        print ('email_done')

        subject_element = driver.find_element_by_name("affiliation")
        subject_element.send_keys("Test_Robot")
        print ('Affiliation_done')

        message_element = driver.find_element_by_name("content")
        message_element.send_keys("Automated Testing")
        print ('Contact_done')

        #Math question
        text=driver.find_element_by_xpath("//*[@id='project-dataset-submission-account']/div/div[6]/div").text
        question=str(text)
        number=[]

        for n in question.split():
            if n.isdigit():
                number.append(n)

        answer=int(number[0])+int(number[1])
        #print (answer)

        answer_field = driver.find_element_by_name("captcha_response")
        answer_field.send_keys(answer)
        
        print ('Math_done')
        #click button
        submit_button = driver.find_element_by_xpath("//*[@id='edit-submit']")
        submit_button.click()

        #success message contact:"/html/body/div[2]/div/section/div[2]"
        success_message=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]").text
        print (success_message)
        print ("All_Done")

        # navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        # responseStart = driver.execute_script("return window.performance.timing.responseStart")
        # domComplete = driver.execute_script("return window.performance.timing.domComplete")

        # backendPerformance = responseStart - navigationStart
        # frontendPerformance = domComplete - responseStart
    
        # print (time.process_time())
        # print ("Back End: %s" % backendPerformance)
        # print ("Front End: %s" % frontendPerformance)
        #time.sleep(10) # Let the user actually see something!
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='example_dir'))


# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('-b', '--browser', type=str, help='specify the testing browser', default='Chrome')
# #parser.add_argument('-u', '--url', type=str, help='specify the testing url')
# args = parser.parse_args()


# if args.browser=='Chrome':
#     #driver = webdriver.Chrome()
#     specify_browser()
#     #Check_mail()

# if args.browser=='Firefox':
#     driver = webdriver.Firefox()
#     driver.get('https://gmod-stage.nal.usda.gov/register/project-dataset/account')
#     specify_browser()

# #if args.url:
#     #driver.get(args.url)