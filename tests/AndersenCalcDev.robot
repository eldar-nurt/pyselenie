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
Check the open calc
    [Documentation]  Проверить показ калькулятора после нажатия.
    [Tags]     smoke  C4122406  andersen     andersen calc   newdsgn
    [Timeout]  10min
    check_calc_dev_block

Check the devs number
    [Documentation]  Проверить плюс/минус разработчика.
    [Tags]      smoke  C4122406  andersen     andersen calc   newdsgn
    [Timeout]   10min
    check_devs_number

Check the qa number
    [Documentation]  Проверить плюс/минус QA инженера.
    [Tags]      smoke  C4122406  andersen     andersen calc   newdsgn
    [Timeout]   10min
    check_qa_number

Check the open moretech
    [Documentation]  Проверить показ всех технологий после нажатия.
    [Tags]     smoke  C4122406  andersen     andersen calc   newdsgn
    [Timeout]  10min
    check_moretech_is_displayed

Enable checkboxes
    [Documentation]  Проверить активированные тайтлы в чекбоксе.
    [Tags]     smoke  C4122406  andersen     andersen calc   newdsgn
    [Timeout]  10min
    check_enabled_check_buttons

Slider func
    [Documentation]  Проверить ползунок в количестве месяцев.
    [Tags]     smoke  C4122406  andersen     andersen calc   newdsgn
    [Timeout]  10min
    ${result}=          check_move_slider
    Should Be True      ${result}

Get calc check
    [Documentation]  Проверить входящие в popup окно изменения.
    [Tags]     smoke  C4122406  andersen     andersen calc   newdsgn
    [Timeout]  10min
    get_calc_check

*** Keywords ***
Suite Setup
    WebUI Suite Setup
    Go To   https://newdsgn.andersenlab.com/find-developers.php
    ${AndersenCalcDev}=        Get Library Instance        AndersenCalcDev
    Set Suite Variable      ${AndersenCalcDev}
    ${Browser}=             Get Library Instance        DriverProvider
    Set Suite Variable      ${Browser}