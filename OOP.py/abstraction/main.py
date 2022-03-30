from mail_services import MailService
from mail_office import MailOffice

mail_server = MailService('Google')
mail_office = MailOffice('Niavaran')
print(mail_server.get_name())
print(mail_office.get_name())