from entities.elements import Image, TextInput, Link, Text, Button, CheckBox
from entities.locators import XPath, Name, ClassName, ID, PartialLinkText, Css
from entities.find import All
from entities.htmlelement import HtmlElement
from rf_libs.DriverProvider import DriverProvider
from entities.mixins import Clicking
from entities.conditions import be, have
from logging import info, error
from extended_entities.ExtendedCheckBox import ExtendedCheckBox
import time


class AndersenProjectCalc(object):
    project_calc_button = Text(XPath(r"//div[@class='managed-project__accordion managed-project__accordion_mt "
                                     r"managed-project__accordion_dn']"))

    project_calc_area = Text(XPath(r"//div[@class='calc-panel box_flex']"))

    def check_open_box_area(self):
        self.project_calc_button.js_click()
        return self.project_calc_area.should(be.displayed())

    select_crit = Text(XPath(r"/html[1]/body[1]/footer[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]"
                             r"/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]"))
    select_crit_li_web = Text(XPath(r"/html[1]/body[1]/footer[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]"
                                    r"/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/div[1]"))

    def check_selected_crit(self):
        self.select_crit.js_click()
        self.select_crit_li_web.js_click()
        info(self.select_crit.text)
        return self.select_crit.text == "Web"

    integration_checkbox = Text(XPath(r"//div[@class='calc__tabs-body']//div[3]//div[1]//div[1]//div[1]//label[1]"))
    improve_checkbox = Text(XPath(r"//div[@class='calc__tabs-body']//div[3]//div[1]//div[1]//div[2]//label[1]"))
    social_serv_checkbox = Text(XPath(r"//div[@class='calc__tabs-body']//div[3]//div[1]//div[2]//div[1]//label[1]"))
    analytics_checkbox = Text(XPath(r"//div[@class='calc__tabs-body']//div[3]//div[1]//div[2]//div[2]//label[1]"))

    def check_crit_features(self):
        self.integration_checkbox.js_click()
        self.improve_checkbox.js_click()
        self.social_serv_checkbox.js_click()
        self.analytics_checkbox.js_click()
        # check whats enabled is unavailiable - check frontend with Oleh

    req_spec_switcher = Text(XPath(r"//div[@class='calc__resources-table-cell']//label"
                                   r"[@class='toggle calc__resources-toggle']"))

    ui_ux_switcher = Text(XPath(r"//div[@class='calc__resources-table-cell line line-slash']//label"
                                r"[@class='toggle calc__resources-toggle']"))

    def check_optinal_extras(self):
        self.req_spec_switcher.click()
        self.ui_ux_switcher.click()
        # check what enabled is unavailiable - check frontend with Oleh

    ur_estimation_proj_button = Text(XPath(r"//a[@class='button calc__button calc__button-estimate "
                                           r"recommend__button']"))
    popup_proj_calc_form = HtmlElement(XPath(r"//div[@id='calc-popup']//div[@class='popup__content']"))

    def check_opening_popup_form(self):
        self.ur_estimation_proj_button.js_click()
        return self.popup_proj_calc_form.should(be.displayed())

    result_criteria = Text(XPath(r"//li[@class='calc-results__list-item calc-results__list-web']"))
    result_opt_extras = All(Text, Css(r"div.calc-results__desc li.calc-results__desc-item"))

    def check_popup_form_data(self):
        exp_result_criteria = "Web"
        exp_result_opt_extras = ["Requirements specification", "UI/UX Design", "Website",
                                 "Integration with third-party services", "Website improvement", "Social services",
                                 "Analytics & report"]
        # assert self.result_criteria.text == exp_result_criteria
        # for item in self.result_opt_extras:
        #     for exp_item in exp_result_opt_extras:
        #         assert item.text == exp_item
        # need help in check
