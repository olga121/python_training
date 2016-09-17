from model.new_contact import New_contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_new_contact_form(self, new_contact):
        wd = self.app.wd
        self.open_add_new_contact()
        self.fill_contact_form(new_contact)
        # submit the form
        wd.find_element_by_name("submit").click()
        self.contact_list_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("home", contact.home_number)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    contact_list_cache = None

    def get_contact_list(self):
        if self.contact_list_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            self.contact_list_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_list_cache.append(New_contact(name=firstname, last_name=lastname, id=id))
        return list(self.contact_list_cache)

    def open_home_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def del_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_list_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact_name(self, new_name_data):
        wd = self.app.wd
        self.open_home_page()
        # open first contact to modify
        wd.find_element_by_xpath("//div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        # enter new data
        self.fill_contact_form(new_name_data)
        # sumbit mifification form
        wd.find_element_by_name("update").click()
        self.contact_list_cache = None
