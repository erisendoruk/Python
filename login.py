from twill.commands import *


go('https://members.thirdspace.london/#/login')

fv("1", "email-email", "doruk.erisen@gmail.com")
fv("1", "password-clear", "101905gs")

submit('0')
