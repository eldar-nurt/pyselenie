from entities.elements import Image, TextInput, Link, Text, Button
from entities.locators import XPath, Name, ClassName, ID, PartialLinkText, Css
from entities.find import All
from entities.htmlelement import HtmlElement
from rf_libs.DriverProvider import DriverProvider
from entities.conditions import be, have
from entities.wait import until_html_element_visible


class AndersenDevelopersCalc(object):
    calc_dev_link = HtmlElement(XPath("//div[@class='extended-team__accordion extended-team__accordion_mt "
                                      "extended-team__accordion_dn']"))
    calc_dev_block = HtmlElement(XPath("//div[@class='extended-team_footer']"))

    def check_calc_dev_block_displayed(self):
        self.calc_dev_link.scroll_to_element()
        # self.calc_dev_link.actions.click()
        self.calc_dev_block.actions.context_click()
        print("Tyt on uzhe clicknul")
        self.calc_dev_block.should(be.displayed)
