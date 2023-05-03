def checker_strong_pass(password):
    uppercase = False
    have_digit = False
    length_pass = False
    if len(password) > 8:
        length_pass = True
    for i in password:
        if i.isdigit():
            have_digit = True
        if i.isupper():
            uppercase = True
    if uppercase and have_digit and length_pass:
        print('Strong pass')
    else:
        print('Week Pass')


checker_strong_pass(input())

