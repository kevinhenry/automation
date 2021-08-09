import re
import shutil

# def get_phone_numbers():
with open('../assets/potential-contacts.txt', 'r') as file:
# with open('../assets/existing-contact.txt', 'r') as file:
    file_data = file.readlines()
    phone_numbers = []
    re_phone = re.compile(r"(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?")
    for line in file_data:
        if re_phone.search(line):
            found_phone_number = re_phone.search(line)
            phone_number = found_phone_number.group()

            if '.' in phone_number:
                phone_number = phone_number.replace('.', '-')
            if '(' in phone_number or ')' in phone_number:
                phone_number = phone_number.strip('(')
                phone_number = phone_number.replace(')', '-')
            if '1-' in phone_number[:2] or '+1' in phone_number[:2]:
                phone_number = phone_number.strip('+1-')
                phone_number = phone_number.strip('1-')

            if len(phone_number.split('x')[0]) < 10:
                phone_number = '206-' + phone_number
            if len(phone_number) == 10:
                phone_number = phone_number[:3] + '-' + phone_number[3:6] + '-' + phone_number[6:]
            if len(phone_number) == 7:
                phone_number = phone_number[:3] + '-' + phone_number[3:6]

            phone_numbers = sorted(phone_numbers)
            phone_numbers.append(phone_number)

    for phone_number in phone_numbers:
        while phone_numbers.count(phone_number) > 1:
            phone_numbers.remove(phone_number)


with open('../assets/phone_numbers.txt', 'w+') as file:
    for phone_number in phone_numbers:
        file.write(f'{phone_number}\n')
    

# def get_email_addresses():
with open('../assets/potential-contacts.txt', 'r') as file:
# with open('../assets/existing-contact.txt', 'r') as file:
    file_data = file.readlines()
    email_addresses = []
    re_email = re.compile(r"\w+.\w+@\w+.\w+.(com|net|org|info|biz)")
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
