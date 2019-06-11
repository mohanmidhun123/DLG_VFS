from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

element_Dir= {
    'web page' : "https://covercheck.vwfsinsuranceportal.co.uk",
    'page info' : "//IMG[@_ngcontent-c0='']",
    'ENTER REG' : "//INPUT[@id='vehicleReg']",
    'Find vehicle' : "//SPAN[@_ngcontent-c1=''][text()='Find vehicle']",
    'Please enter the vehicle registration' :"//DIV[@id='dlg-dealersearch-subtitle']",
    'start date' : "//DIV[@_ngcontent-c1=''][contains(text(),'Cover start:')]",
    'end date' : "//DIV[@_ngcontent-c1=''][contains(text(),'Cover end:')]"

}

@step('I navigate to the Home page')
def step_(context):
    context.browser.get(element_Dir['web page'])
    assert_equal(context.browser.title, "Dealer Portal")

@step('I verify page tittle as "{page_tittle}"')
def step_(context,page_tittle):
    tittle = context.browser.find_element(By.XPATH, element_Dir['page info']).get_attribute("alt")
    assert_equal(tittle, page_tittle)

@step('I verify that "{fieldname}" field is present')
def step_(context,fieldname):
    ele = context.browser.find_element(By.XPATH,element_Dir[fieldname]).text
    assert_equal(ele, fieldname)

@step('I click on "{button}"')
def step_(context,button):
    ele = context.browser.find_element(By.XPATH, element_Dir[button])
    ele.click()
    assert_equal(1, 1)

@step('I search for registration no as "{regNo}"')
def step_(context,regNo):
    ele = context.browser.find_element(By.XPATH, element_Dir['ENTER REG'])
    context.redNo = regNo
    ele.send_keys(regNo)
    assert_equal(1,1)

@step('I should get an error message as "{error}"')
def step_(context,error):
    ele = context.browser.find_element_by_xpath("//*[contains(text(), 'valid')]")
    text = ele.text
    print text
    assert_equal(error, text)

@step('I see a my registration number in search result')
def step_(context):
    xpath = "//DIV[@_ngcontent-c1=''][text()='Result for : "+ context.redNo+"']"
    ele = context.browser.find_element_by_xpath(xpath)
    text = ele.text
    if context.redNo in text:
        assert_equal(1,1)

@step('I see a cover start date as "{start_date}"')
def step_(context, start_date):
    ele = context.browser.find_element_by_xpath(element_Dir['start date'])
    text = ele.text
    text = text.strip().split('Cover start:')[1].replace(' ','')
    assert_equal(start_date, text)

@step('I see a cover end date as "{end_date}"')
def step_(context, end_date):
    ele = context.browser.find_element_by_xpath(element_Dir['end date'])
    text = ele.text
    text = text.strip().split('Cover end:')[1].replace(' ', '')
    assert_equal(end_date, text)