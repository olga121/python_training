class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_new_contact_form(self, new_contact):
        wd = self.app.wd
        self.open_add_new_contact()
        # fill new contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(new_contact.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(new_contact.last_name)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(new_contact.home_number)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(new_contact.email)
        # submit the form
        wd.find_element_by_name("submit").click()

    def open_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


