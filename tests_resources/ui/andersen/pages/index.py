from entities.elements import Image, TextInput, Link, Text
from entities.locators import XPath, Name, ClassName, ID, PartialLinkText, Css
from entities.find import All
from entities.htmlelement import HtmlElement
from rf_libs.DriverProvider import DriverProvider
from entities.conditions import be, have


class AndersenSite(object):
    find_devs_link = Link(PartialLinkText('Find Developers'), timeout=3)

    def hover_find_develops(self):
        self.find_devs_link.actions.hover().perform()

    def click_find_develops(self):
        self.find_devs_link.click()
        develops_url = 'https://newdsgn.andersenlab.com/find-developers.php'
        # develops_url = 'https://newdsgn.andersenlab.com/run-project.php'
        DriverProvider.should(have.url(develops_url, timeout=1))

    # query = TextInput(Name('query'), timeout=30)
    # search_frame = HtmlElement(XPath(r'//*[@id="fast-search-modal"]/div/div/iframe'))
    # description = Text(ClassName('offers-description__specs'), timeout=3)
    #
    # def do_search(self):
    #     self.query.fill('termos')
    #     logger.warn('OK')
    #     get_driver().switch_to.frame(self.search_frame._web_element)
    #     links = self.results.links
    #     parsed_result = {}
    #     item = links[1]
    #     parsed_result['link'] = item.get_href()
    #     parsed_result['name'] = item.text
    #     item._web_element.click()
    #     parsed_result['description'] = self.description.text
    #     parsed_result['images'] = []
    #     for img in self.images.items:
    #         parsed_result['images'].append(img._web_element.get_attribute('data-original'))
    #
    #
    # sleep(10)

    button_req_spec = Text(XPath(r"//div[@class='button button_theme-transparent']"), timeout=3)
    popup_req_spec = HtmlElement(XPath(r"//div[@id='popup_requestpProject']"), timeout=3)

    def check_request_specialist(self):
        self.button_req_spec.js_click()
        assert self.popup_req_spec.should(be.displayed()), 'Not displayed!'

    button_req_meet = Text(XPath(r"/html[1]/body[1]/footer[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[24]"
                                 r"/div[5]"))
    popup_req_block = HtmlElement(XPath(r"//div[@id='popup_request']//div[@class='popup__container']"))

    def check_popup_req_meet(self):
        self.button_req_meet.js_click()
        assert self.popup_req_block.should(be.displayed())

    meet_input_for_mail_and_phone = TextInput(XPath(r"/html[1]/body[1]/div[10]/div[1]/div[1]/div[1]/form[1]/div[3]"
                                                    r"/div[1]/input[1]"))
    input_error = Text(Css(r"div.popup.popup_sm.popup_active:nth-child(13) div.popup__container div.popup__content "
                           r"div.popup__section form.form div.form__row:nth-child(3) div.control.control_error > "
                           r"<pseudo:after>"))
    input_submit_button = Text(XPath(r"/html[1]/body[1]/div[10]/div[1]/div[1]/div[1]/form[1]/button[1]"))

    def check_validation_on_forms(self):
        invalid_emails = ["testAtgmail.com", "test@gmailcom", "test@gmail", "@gmail"]
        invalid_phones = ["1111111111111111111", "22222", "$100000", "bort228"]

        for email in invalid_emails:
            self.meet_input_for_mail_and_phone.send_keys(email)
            if not self.input_error.should(be.displayed()):
                return KeyError

        for phone in invalid_phones:
            self.meet_input_for_mail_and_phone.send_keys(phone)
            if not self.input_error.should(be.displayed()):
                return KeyError
