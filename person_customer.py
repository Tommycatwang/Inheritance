import Person as person1

def main():
    name ='john'
    address = '1234 baylor'
    telenum = "123-523-1232"
    customer_num = 1234
    onlist_flag = False

    person11=person1.person(name,address,telenum)

    customer1=person1.Customer(name,address,telenum,customer_num,onlist_flag)

    person11.print_person()

    print()
    print
