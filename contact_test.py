import pyperclip
import unittest #importing the unittest module
from contact import Contact #import contact class

class TestContact(unittest.TestCase):

    """
    Test class that defines test cases for the contact class behaviors.

    Args:
    unittest.TestCase.TestCase class that helps in creating test cases

    """
    #Test 1

    def setUp(self): # setUp defines instructions that will be executed before each test method. 

            """
           Set up method to run before each test cases
            """
            self.new_contact=Contact("James", "Muriuki", "0746373622", "james@moringaschool.com")#create contact object
    def tearDown(self):
        """tearDown method does clean up after each test case has run.
        """

        Contact.contact_list=[]

    def test_init(self):
            """
            test_init test case to test if the object is intialized properly
            """

            self.assertEqual(self.new_contact.first_name,"James") #assertEqual checks for the expected result
            self.assertEqual(self.new_contact.last_name,"Muriuki")
            self.assertEqual(self.new_contact.phone_number,"0746373622")
            self.assertEqual(self.new_contact.email,"james@moringaschool.com")



#Test 2-  save contacts

    def test_save_contact(self):

            """
            test_save_contact test case to test if the contact object is saved into the contact list
            """
            self.new_contact.save_contact() #saving new contact

            self.assertEqual(len(Contact.contact_list),1)

            #Test 3-save multiple contacts

    def test_save_multiple_contact(self):

            """test_save_multiple contact to check if we can save mulitple
            contact objects to our contact_list
            """

            self.new_contact.save_contact()
            test_contact=Contact("Test", "User", "0712345678", "test@user.com") #new contact
            test_contact.save_contact()
            self.assertEqual(len(Contact.contact_list),2)

            #Test 4-delete contacts

    def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
            test_contact.save_contact()

            self.new_contact.delete_contact()# Deleting a contact object
            self.assertEqual(len(Contact.contact_list),1)


            #Test 5-find a contact object
    def test_find_contact_by_number(self):
            '''
            test to check if we can find a contact by phone number and display information
            '''

            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
            test_contact.save_contact()

            found_contact = Contact.find_by_number("0711223344")

            self.assertEqual(found_contact.email,test_contact.email)

    def test_contact_exists(self):

        """
        test to check if we can return Boolean if we cannot find the contact
        """

        self.new_contact.save_contact()
     #   test_contact=Contact("Test", "user", "0711223344", "test@user,com") #new contact
      #  test_contact.save_contact()

        contact_exists=Contact.contact_exists("0711223344")

        self.assertTrue(contact_exists)

    def test_display_all_contact(self):
        """
        method that returns the contact list
        """

        return cls.contact_list

def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_contact.save_contact()
        Contact.copy_email("0712345678")

        self.assertEqual(self.new_contact.email,pyperclip.paste())

if __name__=='__main__': #confirming that anything inside the if block should run only if the file is currently being run
    unittest.main() #collects all tests and methods and executes them