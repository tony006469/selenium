*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Open browser and run 
    Open Browser https://gmod-stage.nal.usda.gov/register/project-dataset/account headlesschrome
    Input Text name=name Test_Robot
    Input Text xpath=//*[@id='edit-email'] monica.poelchau@ars.usda.gov
    Input Text name=affiliation Test_Robot
    Input Text name=content Automated Testing
    [Teardown]    Close All Browsers

*** Keywords ***
Wait and Input 
    [Arguments]  ${locator}  ${text}
    Wait Until Element is Visible ${locator}
    Input Text  ${locator}  ${text}

