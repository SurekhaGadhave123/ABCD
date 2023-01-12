import time
from library.wrapper import Wrapper
from selenium.webdriver.common.by import By


class General(Wrapper):
    def __init__(self, driver):
        super().__init__(driver)
        # super().__init__(driver)

    def click_keypad(self):
        keypad = (By.ID, "com.google.android.dialer:id/dialpad_fab")
        self.click_element(keypad)
        time.sleep(3)

    def click_numbers(self, no):
        number = (By.ID, f"com.google.android.dialer:id/{no}")
        self.click_element(number)
        time.sleep(2)

    def click_callbtn(self):
        call = (By.ID, "com.google.android.dialer:id/dialpad_voice_call_button")
        self.click_element(call)
        time.sleep(2)

    def click_seven(self):
        seven = (By.ID, "com.google.android.calculator:id/digit_7")
        self.click_element(seven)
        time.sleep(2)

    def click_three(self):
        three = (By.ID, "com.google.android.calculator:id/digit_3")
        self.click_element(three)
        time.sleep(2)

    def click_add(self):
        add = (By.ID, "com.google.android.calculator:id/op_add")
        self.click_element(add)
        time.sleep(2)

    def click_equal(self):
        equal = (By.ID, "com.google.android.calculator:id/eq")
        self.click_element(equal)
        time.sleep(2)

    def get_finalresult(self):
        time.sleep(3)
        result = (By.ID, "com.google.android.calculator:id/result_final")
        return self.get_text_from_element(result)

    def click_messegesicon(self):
        msg = (By.XPATH, "//android.widget.TextView[@content-desc='Messages']")
        self.click_element(msg)
        time.sleep(2)

    def click_startchatbtn(self):
        startchat = (By.XPATH, "//android.widget.Button[@content-desc='Start chat']")
        self.click_element(startchat)
        time.sleep(2)

    def enter_phoneno(self, no):
        phoneno = (By.ID, "com.google.android.apps.messaging:id/recipient_text_view")
        self.enter_text(phoneno, no)
        time.sleep(2)

    def click_creategroup(self):
        create = (By.ID, "com.google.android.apps.messaging:id/contact_picker_create_group")
        self.click_element(create)
        time.sleep(2)

    def click_next(self):
        next = (By.ID, "com.google.android.apps.messaging:id/container_action_button")
        self.click_element(next)
        time.sleep(2)

    def enter_msg(self, text):
        msg = (By.ID, "com.google.android.apps.messaging:id/compose_message_text")
        self.enter_text(msg, text)
        time.sleep(2)

    def click_sendbtn(self):
        send = (By.XPATH, "//android.widget.ImageView[@content-desc='Send SMS']")
        self.click_element(send)
        time.sleep(2)

    def get_sended_msgtext(self):
        time.sleep(2)
        text = (By.ID, "com.google.android.apps.messaging:id/message_text")
        return self.get_text_from_element(text)

    def click_morefield(self):
        more = (By.ID, "com.google.android.contacts:id/more_fields")
        self.click_element(more)
        time.sleep(2)

    def click_contacts(self):
        contact = (By.XPATH,
                   "//android.widget.FrameLayout[@content-desc='Contacts']/android.view.ViewGroup/android.widget.TextView")
        self.click_element(contact)
        time.sleep(2)

    def enter_firstname(self, name):
        firstname = (By.ID, "//android.widget.EditText[@text='First name']")
        self.enter_text(firstname, name)
        time.sleep(2)

    def click_endcall(self):
        end = (By.ID, "com.google.android.dialer:id/incall_end_call")
        self.click_element(end)
        time.sleep(2)

    def get_endcalltext(self):
        time.sleep(2)
        text = (By.ID, "com.google.android.dialer:id/incall_end_call")
        return self.get_text_from_element(text)
