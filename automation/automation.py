from faker import Faker
import shutil

fake = Faker('en_US')

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

content = ''

# for i in range(100):

content += fake.paragraph()
content += fake.email()
content += fake.paragraph()
content += fake.phone_number()
content += fake.paragraph()
content += '\n'
print(content)

with open('assets/notes.txt', 'w+') as file:
    file.write(content)


shutil.copy('assets/notes.txt', '.')