# Write a program to check if a number is a multiple of 50

# num = int(input("Input a Number "))
#
# multiple = 50%num
# print(multiple)
# if multiple == 0:
#     print(num, " is a multiple of 50")
# else:
#     print(num, " is not a multiple of 50")


# Write a program to lock a safe ,before
# opening the safe require three or two  personnel  to open .namely The president,vice and the speaker
# when the president is prensent and any other ,the safe should open,when vice and speaker is present the
# safe should open


personnel_one = str(input('President  Password'))
personnel_two = str(input('Vice  Password'))
personnel_third = str(input('Speaker Password'))


if personnel_one == 'p' and personnel_two == 'vp' or personnel_third == 's':
    print('safe open')
elif personnel_two == 'vp' and personnel_third == 's':
    print('safe open')
else:
    print('safe lock')
print('safe open')


