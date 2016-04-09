# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".

def print_hello():

    print "Hello World"


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.

def print_name(name):

    print "Hi", name


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def multiply_nums(num1, num2):

    print num1 * num2


# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def print_string_x_times(string, num):

    print string * num


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def checks_relation_to_zero(num):

    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    elif num == 0:
        print "Zero"

# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.


def is_divisible_by_three(num):

    return (num % 3 == 0)


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.


def get_spaces_num(sentence):

    spaces = 0

    for letter in sentence:
        if letter == ' ':
            spaces += 1

    return spaces

# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.


def get_price_of_meal(meal_price, tip=0.15):

    total_price = meal_price + meal_price * tip

    return total_price

# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.


def get_value_of_int(num):

    info_list = ["", ""]

    if num > 0:
        info_list[0] = "Positive"
    elif num < 0:
        info_list[0] = "Negative"
    else:
        info_list = "Zero"

    if num % 2 == 0:
        info_list[1] = "Even"
    else:
        info_list[1] = "Odd"

    return info_list

a, b = get_value_of_int(-7)

print a, b


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.
