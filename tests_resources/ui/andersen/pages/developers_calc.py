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


class AndersenDevelopersCalc(object):
    calc_dev_link = HtmlElement(XPath("//div[@class='extended-team__accordion extended-team__accordion_mt "
                                      "extended-team__accordion_dn']"), timeout=10)
    calc_dev_block = Text(XPath(r"/html/body/footer/div[1]/div[1]/div[1]"), timeout=10)

    def check_calc_dev_block(self):
        self.calc_dev_block.actions.move_to_element().perform()
        self.calc_dev_block.click()
        self.calc_dev_block.should(be.displayed())

    dev_minus = Text(XPath(r"//div[@class='calculator__column calculator__column_flex']//div[1]//div[1]//span[1]"))
    dev_plus = Text(XPath(r"/html[1]/body[1]/footer[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]"
                          r"/div[1]/span[2]"))
    dev_number = TextInput(XPath(r"//div[@class='calculator__column calculator__column_flex']"
                                 r"//div[1]//div[1]//input[1]"))

    qa_minus = Text(XPath(r"/html[1]/body[1]/footer[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]"
                          r"/div[1]/span[1]"))
    qa_plus = Text(XPath(r"/html[1]/body[1]/footer[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]"
                         r"/div[1]/span[2]"))
    qa_number = TextInput(XPath(r"//div[@class='calculator__column calculator__column_flex']//div[3]//div[1]"
                                r"//input[1]"))

    pm_plus = Text(XPath(r"//div[@class='calculator__column calculator__column_flex']//div[2]//div[1]//span[2]"))
    pm_number = Text(XPath(r"//div[@class='calculator__column calculator__column_flex']//div[2]//div[1]//input[1]"))

    ba_plus = Text(XPath(r"//div[@class='calculator__column calculator__column_flex']//div[4]//div[1]//span[2]"))
    ba_number = Text(XPath(r"//div[@class='calculator__column calculator__column_flex']//div[4]//div[1]//input[1]"))

    zero_button = Text(XPath(r"//div[@class='calculator-button calculator__team-button line line_button']"))

    def check_zero_button(self):
        self.dev_minus.js_click()
        self.dev_minus.js_click()
        self.qa_plus.js_click()
        self.dev_plus.js_click()
        self.pm_plus.js_click()
        self.ba_plus.js_click()
        self.zero_button.js_click()
        return self.qa_number.text!='0' or self.dev_number.text!='0' or self.dev_number.text!='0' or self.ba_number!='0'

    def check_devs_number(self):
        self.dev_plus.click()
        dev_number_exp_result = 1
        dev_number_fact_result = self.dev_number.text
        return dev_number_exp_result == dev_number_fact_result

    def check_qa_number(self):
        self.qa_plus.click()
        qa_number_exp_result = 1
        qa_number_fact_result = self.qa_number.text
        return qa_number_exp_result == qa_number_fact_result

    more_techs_button = Text(XPath(r"//div[@class='calculator-button calculator__tech-button line line_button']"))
    block_with_moretech_nodejs = Text(XPath(r"//div[@class='calculator__table-cell-body']//div[5]//label[1]"))

    def check_moretech_is_displayed(self):
        self.more_techs_button.click()
        self.block_with_moretech_nodejs.should(be.displayed())

    check_titles = All(Text, ClassName(r"calculator__toggle_checkbox"))
    checks = All(ExtendedCheckBox, ClassName(r"calculator__input"))

    def check_enabled_check_buttons(self):
        result_click = ["Java", ".NET", "Scala", "HTML/CSS", "Javascript", "ReactJS", "iOS", "Android", "React Native",
                        "DevOps", "BigData", "MySQL"]
        # for check in self.checks:
        #     for result in result_click:
        #         if check.text == result:
        #             check.js_click()
        # for check in self.checks:
        #     for result in result_click:
        #         if check.text == result:
        #             """ispravit\' tyt"""
        #             check_input = check
        #             info(check_input)
        #             if not check.is_checked():
        #                 error(check.text + " not checked!")
        #             else:
        #                 info(check.text + "is checked!")
        # result_checks = []
        for title_index, check_title in enumerate(self.check_titles):
            for result in result_click:
                if check_title.text == result:
                    check_title.click()
                    # result_checks.append(title_index)
        # I will work on it.
        # for result_check in result_checks:
        #     for checkbox_index, checkbox in enumerate(self.checks):
        #         if int(checkbox_index) == int(result_check):
        #             if checkbox.is_checked():
        #                 info(str(result_check) + " is checked!")
        # info("Lenght: " + str(len(result_checks)))

    start_position_the_slider = Text(XPath(r"//div[@class='ui-slider-grid']//div[1]//div[1]"))
    finish_position_the_slider = Text(XPath(r"//div[@class='ui-slider-grid']//div[1]//div[5]"))
    quantity_months = Text(XPath(r"//span[@id='ui-slider-duration']"))

    def check_move_slider(self):
        self.start_position_the_slider.actions.drag_and_drop(target=self.finish_position_the_slider).perform()
        fact_result_quantity_months = "5"
        return fact_result_quantity_months == self.quantity_months.text

    get_calc_button = Link(PartialLinkText(r"Get calculation"))
    month_count = Text(XPath(r"//span[@id='project-days']"))
    dev_count_fact = Text(XPath(r"//span[@id='dev']"))
    qa_count_fact = Text(XPath(r"//span[@id='qa']"))
    backend_techs_fact = All(Text, XPath(r"//ul[@id='backend']//li"))
    frontend_techs_fact = All(Text, XPath(r"//ul[@id='frontend']//li"))
    mobile_techs_fact = All(Text, XPath(r"//ul[@id='mobile']//li"))
    other_techs_fact = All(Text, XPath(r"//ul[@id='other']//li"))

    def get_calc_check(self):
        result_exp = ["Java", ".NET", "Scala", "HTML/CSS", "Javascript", "ReactJS", "iOS", "Android", "React Native",
                      "DevOps", "BigData", "MySQL"]
        self.get_calc_button.click()
        if self.month_count.text != "5":
            error("Incorrect month count!")
        if self.dev_count_fact.text != "1":
            error("Incorrect developer count!")
        if self.qa_count_fact.text != "1":
            error("Incorrect qa count!")
        result_fct = self.backend_techs_fact + self.frontend_techs_fact + self.mobile_techs_fact + self.other_techs_fact
        info(len(result_fct))
        if len(result_fct) != len(result_exp):
            error("Not enought elements in techs!")
        for exp_elem in result_exp:
            for fct_elem in result_fct:
                if fct_elem.text == exp_elem:
                    info("Find equals!")
                    info(exp_elem)
