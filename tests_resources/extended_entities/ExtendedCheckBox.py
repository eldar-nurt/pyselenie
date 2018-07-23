from entities.elements import CheckBox


class ExtendedCheckBox(CheckBox):

    def get_value(self):
        return self._web_element.get_attribute("value")
