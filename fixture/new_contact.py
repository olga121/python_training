from model.new_contact import New_contact
import re

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
            self.open_home_page()
            self.contact_list_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
 #               print(all_phones)
                self.contact_list_cache.append(New_contact(name=firstname, last_name=lastname, id=id, address=address,
                                                           all_phones_from_home_page=all_phones,
                                                           all_emails_from_home_page=all_emails))
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
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_elements_by_class_name("left")[1].click()
        wd.switch_to_alert().accept()
        self.contact_list_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact_name(self, new_name_data):
        self.modify_some_contact_name(0, new_name_data )

    def modify_some_contact_name(self, index, new_name_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # enter new data
        self.fill_contact_form(new_name_data)
        # sumbit modification form
        wd.find_element_by_name("update").click()
        self.contact_list_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # open contact to modify
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # open contact to modify
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        secondary_number = wd.find_element_by_name("phone2").get_attribute("value")
        return New_contact(name = name, last_name = last_name, id = id, home_number = home_number, work_number = work_number,
                           mobile_number = mobile_number, secondary_number = secondary_number, address = address,
                           email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H: (.*)", text).group(1)
        mobile_number = re.search("M: (.*)", text).group(1)
        work_number = re.search("W: (.*)", text).group(1)
        secondary_number = re.search("P: (.*)", text).group(1)
        return New_contact(home_number=home_number, work_number=work_number,
                           mobile_number=mobile_number, secondary_number=secondary_number)

