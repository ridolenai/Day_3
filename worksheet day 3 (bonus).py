
# import statistics
# from statistics import mode
# from collections import Counter

list_of_numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
# arbitrary_number = 5
# secondlist_of_numbers = [1,1,1,4,2,2,3,3,5]
# keepy_tracky_number = 0
# first_list_names = ['Jimbob', 'Bubba', 'Jeremiah']
# second_list_names = ['Bubba', 'Johnny', 'Jimbob']


def average_numbers (list_of_numbers):
    total = sum(list_of_numbers)
    avg = total / len(list_of_numbers)
    smaller_list = []
    for x in list_of_numbers:
        if x < avg:
            smaller_list.append(x)
    return (smaller_list)



# def index_retrieval (list_of_numbers, arbitrary_number):
#     if len(list_of_numbers) < arbitrary_number:
#         reply = 'No value here!'
#         print (reply)

#     else:
#         result = (list_of_numbers[arbitrary_number])
#         return (result)
        

# def most_frequent (secondlist_of_numbers):
#     answer = (mode(secondlist_of_numbers))
#     print (answer)
#def most_frequent_value(list_name):

    
# for number in secondlist_of_numbers:
#     this_number = secondlist_of_numbers.count(number)
#     if(this_number > keepy_tracky_number):
#         keepy_tracky_number = this_number
#         print (number)

    
    



# def name_comparison (first_list_names, second_list_names):
    
    first = first_list_names
    second = second_list_names
    return (set(first) & set(second))

    
