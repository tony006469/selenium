*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Open browser and run 
    Open Browser  https://gmod-stage.nal.usda.gov/register/project-dataset/account  headlesschrome
    Wait and Input  name=name  Test_Robot
    Wait and Input  xpath=//*[@id='edit-email']  monica.poelchau@ars.usda.gov
    Wait and Input  name=affiliation  Test_Robot
    Wait and Input  name=content  Automated Testing
    [Teardown]    Close All Browsers

*** Keywords ***
Wait and Input 
    [Arguments]  ${locator}  ${text}
    Wait Until Element is Visible  ${locator}
    Input Text  ${locator}  ${text}

