*** Settings ***
Resource          tests_resources/webui.config.robot
Suite Teardown    WebUI Suite Teardown
Test Setup        Test Setup
Test Teardown     Test Teardown
Suite Setup       Suite Setup
Force Tags        common
Default Tags      smoke
Library           tests_resources.ui.andersen.pages.index.AndersenSite  WITH NAME  AndersenSite


*** Test Cases ***
Check for static headers on page scrolls
    [Documentation]  Проверить появления статического хедера при скролле страницы
    [Tags]    smoke  C4121844  andersen  no_run
    [Timeout]  10min
    Do Search


Check the hover efect link "Staff Augmentation"
    [Documentation]  Проверить ховер эффект ссылки "Staff Augmentation"
    [Tags]    smoke  C4121849  andersen  main page
    [Timeout]  10min
    Hover Find Develops

Check request specialist form open
    [Documentation]  Проверить появления формы "Request specialist" после нажатия на кнопку(также называется)
    [Tags]    smoke  C4126443  andersen     main page
    [Timeout]  1min
    check_request_specialist

Check validation request form
    [Documentation]  Проверить отображение ошибки для "Meet request".
    [Tags]    smoke  C4126443  andersen     main page
    [Timeout]  1min
    check_validation_on_forms


Check the clickability of the link "Project Development"
    [Documentation]  Проверить кликабельность ссылки "Project Development"
    [Tags]    smoke  C4121860  andersen     main page
    [Timeout]  10min
    Call method             ${AndersenSite.find_devs_link}      click
    Check Browser Url       https://newdsgn.andersenlab.com/find-developers.php

*** Keywords ***
Suite Setup
    WebUI Suite Setup
    Go To   https://newdsgn.andersenlab.com
    ${AndersenSite}=        Get Library Instance        AndersenSite
    Set Suite Variable      ${AndersenSite}
    ${Browser}=             Get Library Instance        DriverProvider
    Set Suite Variable      ${Browser}
