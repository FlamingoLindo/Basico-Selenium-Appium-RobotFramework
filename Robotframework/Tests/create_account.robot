*** Settings ***
Library    SeleniumLibrary
Library    XML
Resource   ../Keywords/keywords.robot
Resource   ../Resources/variables.robot

*** Test Cases ***
Create Course
    Open the url in browser    ${page}    ${browser}
    Wait for and click in the sign-up button
    Wait for modal to load
    Fill up the form    ${name}    ${password}    ${email}

    [Teardown]    Close Browser
