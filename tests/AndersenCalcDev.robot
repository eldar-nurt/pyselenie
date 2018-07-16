*** Settings ***
Resource          tests_resources/webui.config.robot
Suite Teardown    WebUI Suite Teardown
Test Setup        Test Setup
Test Teardown     Test Teardown
Suite Setup       Suite Setup
Force Tags        common
Default Tags      smoke
Library           tests_resources.ui.andersen.pages.developers_calc.AndersenDevelopersCalc   WITH NAME   AndersenCalcDev

*** Test Cases ***

Check the open calc after click on the calc link
    [Documentation]  Проверить показ калькулятора после нажатия
    [Tags]    smoke  C4122406  andersen     andersen calc   newdsgn
    [Timeout]  10sec
    Check calc dev block displayed

*** Keywords ***
Suite Setup
    WebUI Suite Setup
    Go To   https://newdsgn.andersenlab.com/find-developers.php
    ${AndersenCalcDev}=        Get Library Instance        AndersenCalcDev
    Set Suite Variable      ${AndersenCalcDev}
    ${Browser}=             Get Library Instance        DriverProvider
    Set Suite Variable      ${Browser}