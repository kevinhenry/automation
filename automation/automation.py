import re
import shutil

# def get_phone_numbers():

# re_phone = re.compile(r"/\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/")

re_phone = re.compile(r"(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?")

phone_numbers = []

with open('../assets/potential-contacts.txt', 'r') as file:
# with open('../assets/existing-contact.txt', 'r') as file:
    file_data = file.readlines()
    
    for line in file_data:
        if re_phone.search(line):
            found_phone_number = re_phone.search(line)
            found_phone_number = found_phone_number.group()
            phone_numbers = sorted(phone_numbers)
            phone_numbers.append(found_phone_number)
    
    for found_phone_number in phone_numbers:
        while phone_numbers.count(found_phone_number) > 1:
            phone_numbers.remove(found_phone_number)

with open('../assets/phone_numbers.txt', 'w+') as file:
    for phone_number in phone_numbers:
        file.write(f'{phone_number}\n')

# def get_email_addresses():

re_email = re.compile(r"\w+.\w+@\w+.\w+.(com|net|org|info|biz)")

email_addresses = []


with open('../assets/potential-contacts.txt', 'r') as file:
# with open('../assets/existing-contact.txt', 'r') as file:
    file_data = file.readlines()
    
    for line in file_data:
        if re_email.search(line):
            found_email = re_email.search(line)
            found_email = found_email.group()
            email_addresses = sorted(email_addresses)
            email_addresses.append(found_email)
    
    for found_email in email_addresses:
        while email_addresses.count(found_email) > 1:
            email_addresses.remove(found_email)


with open('../assets/email_addresses.txt', 'w+') as file:
    for email_address in email_addresses:
        file.write(f'{email_address}\n')

# print(fake)

# print(fake)

# print(dir(fake))
# print(fake.wor())
# print(fake.words())
# print(fake.sentence())
# print(fake.sentences())
# print(fake.paragraph())
# print(fake.paragraph(20))
# print(fake.name())
# print(fake.credit_card())
# print(fake.email(100))
# for i in range(100):
#     print(fake.email())
# print(fake.phone_number())

# content = ''

# for i in range(100):

# content += fake.paragraph()
# content += fake.email()
# content += fake.paragraph()
# content += fake.phone_number()
# content += fake.paragraph()
# content += '\n'
# print(content)

# with open('assets/notes.txt', 'w+') as file:
#     file.write(content)


# shutil.copy('assets/notes.txt', '.')