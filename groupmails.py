from django.core.mail import send_mass_mail
from django.contrib.auth.models import Group

# Отримуємо список користувачів групи "group1"
group1_users = Group.objects.get(name='group1').user_set.all()
group1_recipients = [user.email for user in group1_users]

# Отримуємо список користувачів групи "group2"
group2_users = Group.objects.get(name='group2').user_set.all()
group2_recipients = [user.email for user in group2_users]

# Підготовка повідомлення
subject = 'Subject line'
message = 'Here is the message.'
from_email = 'sender@example.com'
recipient_list = [(email,) for email in group1_recipients + group2_recipients]

# Відправка електронної пошти
send_mass_mail((subject, message, from_email, recipient_list), fail_silently=False)