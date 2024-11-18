*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open the url in browser
    [Arguments]    ${page}    ${browser}
    Open browser    ${page}    ${browser}

Wait for and click in the sign-up button
    Wait Until Element Is Visible    css=.gPDjGr
    Click Element    css=.gPDjGr

Wait for modal to load
    Wait Until Element Is Visible    css=.jAEPQo

Fill up the form
    [Arguments]    ${name}    ${password}    ${email}
    Sleep    2s
    Input Text    id=signup-username    ${name}
