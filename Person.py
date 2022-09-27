class person:
    def __init__(self,name,address, telenum):
        self._name = name
        self._address=address
        self._telenum=telenum

    def get_name(self):
        return self._name
    def get_address(self):
        return self._address

    def get_telenum(self):
        return self._telenum

    
    
    def print_person(self):
        print('person name is: ', self._name)
        print('person address is', self._address)
        print("person's telephone number is", self._telenum)



class Customer(person):
    def __init__(self,name,address,telenum,customer_number,wishes):
        person.__init__(self,customer_number,wishes)

        self.customer_number=customer_number
        self.wishes=wishes

    
    #def set_wish(self,wishes):
       ##     print("this person want to be on the wish list")
        #else:
       #     print("this person does not want to be on wish list")
    def print_person(self):
        person.print_person(self)

        print('customer number: ', self.customer_number)

        if self.wishes:##equal if self.___onlist ==true
            print("on the mailing list: yes")
        else:
            print('he is not on the list')