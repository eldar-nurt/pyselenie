*** Settings ***
Resource          tests_resources/webui.config.robot
Suite Teardown    WebUI Suite Teardown
Test Setup        Test Setup
Test Teardown     Test Teardown
Suite Setup       Suite Setup
Force Tags        common
Default Tags      smoke
Library           tests_resources.ui.andersen.pages.project_calc.AndersenProjectCalc   WITH NAME   AndersenProjDev

*** Test Cases ***
Check open calc
    [Documentation]  Проверить показ калькулятора проекта.
    [Tags]    smoke  C4122541  andersen     proj_calc
    [Timeout]  10min
    ${result}=      check_open_box_area
    Should Be True  ${result}

Check criteria
    [Documentation]  Проверить выбор критерия проекта.
    [Tags]    smoke  C4122541  andersen     proj_calc
    [Timeout]  10min
    ${result}=      check_selected_crit
    Should Be True  ${result}

Check features of criteria
    [Documentation]  Проверить всё ли выбрано в разделе "Criteria".
    [Tags]    smoke  C4122541  andersen     proj_calc
    [Timeout]  10min
    check_crit_features

Check optional extras
    [Documentation]  Проверить всё ли выбрано в разделе "Optional extras" и оформление switches изменилось.
    [Tags]    smoke  C4122541  andersen     proj_calc
    [Timeout]  10min
    check_optinal_extras

Сheck opening popup form
    [Documentation]  Проверить открытие формы для заключительного этапа.
    [Tags]    smoke  C4122541  andersen     proj_calc
    [Timeout]  10min
    ${result}=      check_opening_popup_form
    Should Be True  ${result}

Check all data which chosen
    [Documentation]  Проверить правильность тех данных, что были введены при отображении на форме заказа.
    [Tags]    smoke  C4122541  andersen     proj_calc
    [Timeout]  10min
    check_popup_form_data

*** Keywords ***
Suite Setup
    WebUI Suite Setup
    Go To   https://newdsgn.andersenlab.com/run-project.php
    ${AndersenCalcDev}=        Get Library Instance        AndersenProjDev
    Set Suite Variable      ${AndersenCalcDev}
    ${Browser}=             Get Library Instance        DriverProvider
    Set Suite Variable      ${Browser}