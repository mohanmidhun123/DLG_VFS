# DLG_VFS
Behave(Gherkin syntax) based automated testing using python


Pre-requisistes:
1. Install Python (Eg. Python 2.7)
2. Install Selenium
3. Install Chrome driver for selenium (download the .exe file)
4. Install Python Behave module(pip install behave)
5. Create a folder structure :
      BDD Automated Tests/
        features/
          __init__.py
          pages/
              __init__.py
          steps/
              __init__.py


Procedure to run the test:
1. Goto the BDD Automated Tests using CMD Prompt
2. Type "behave" and enter


Acceptance Test Scenario's
1. Check that the web page tittle is visible
2. Verify that "ENTER REG" field is present
3. Verify that "Find vehicle" button is present
4. Verify that "Please enter the vehicle registration" field is present
5. Check Error responses if no registration number is entered.
6. Check if expected search result(Cover Start and End date) is obtained
