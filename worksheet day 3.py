


# many_colors = ['blue', 'red', 'white', 'green', 'yellow']
list_of_numbers=[1,2,3,4,5,6,7,8,9,10]
arbitrary_number = 3

# def colors(many_colors):
#     for color in many_colors:
#         print(many_colors[0])
#     return (many_colors[0])


# def color_list(more_colors):
#     guess = input("Enter a color: ")


guess = input('Enter a color: ')
color_selections = ['blue', 'red', 'white', 'green', 'yellow']
while (guess) not in color_selections:
    guess = input("Enter a color: ")
    if guess in color_selections:
        print('You found my chosen color!')

# def numbers(list_of_numbers):
#     total = sum(list_of_numbers)
#     if total % 2 == 0:
#         print('Even')
#     else:
#         print ('Odd')

def check_it(list_of_numbers, arbitrary_number):
    for number in list_of_numbers:
        if number > arbitrary_number:
            print(number)


# https://www.online.devcodecamp.com/courses/take/mercury-full-stack-software-development/texts/28350424-day-4-overview-using-functions