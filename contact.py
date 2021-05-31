import pyperclip

class Contact: 
    contact_list= [] #empty

    def __init__(self,first_name,last_name,phone_number,email): 


        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email


#self is a special keyword in python, 
    # self is a variable that represents the instance of the object itself. Like "this" in Js.
    # _init_ creates new instances of a class
    def save_contact(self): #append objects to contact list

        """
        save_contact method saves contact objects into contact_list
        """

        Contact.contact_list.append(self)

    def delete_contact(self):

        """delete_contact method deletes a saved contact from the contact_list
        """

        Contact.contact_list.remove(self)

@classmethod #decorator. Allows make simple modifications to functions,methods or classes. Eg Shows that the method belongs to the entire class
def find_by_number(cls,number): #cls refers to entire class. 
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

@classmethod
def contact_exist(cls,number):
    """Method that checks if a contact exists from the contact list

    Args:
    number: Phone number to search if it exists

    returns: True or false depending if the contact exists
    """

    for contact in cls.contact_list:
        print(contact.phone_number, "This is my comtact")
        if contact.phone_number==number:
            return True

    return False

@classmethod
def display_contact(cls):

    """
    method that returns the contact list
    """
    return cls.contact_list

@classmethod
def copy_email(cls,number):
    contact_found = Contact.find_by_number(number)
    pyperclip.copy(contact_found.email)