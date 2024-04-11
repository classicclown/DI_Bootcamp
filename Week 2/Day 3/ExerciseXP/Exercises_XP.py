# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
# import random
# def get_random_temp(season):
#     if season.lower() =="winter":
#         return random.randint(-10,16)
#     elif season.lower() == "autumn":
#         return random.randint(16,23)
#     elif season.lower() == "spring":
#         return random.randint(23,32)
#     elif season.lower() == "summer":
#         return random.randint(32,40)


# def main():
#     season = input("Enter a season: Summer, Winter, Autumn or Spring")
#     temp = get_random_temp(season)
#     if 0>temp:
#         print ("Brr, it's freezing today")
#     elif 0<temp<16:
#         print("It's not freezing but definitely take a coat")
#     elif 16<temp<23:
#         print("Temps are warming up, you'll need a light sweater today")
#     elif 24<temp<32:
#         print("Buckle up, we're entering summer temps!")
#     else:
#         print("Stay in the shade today, it's cooking out there!")

# main()

#Ex.2

# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]

# def ask_question (info_list):
#     wrong_answers=[]
#     for dict in info_list:
#         print (dict["question"])
#         answer = input()
#         if answer == dict["answer"]:
#             print ("Correct!")
#         else:
#             print("Incorrect")
#             print (dict["answer"])
#             wrong_answers.append({"question":dict['question'],"Your Answer":[answer],"Right Answer":dict["answer"]})

#     if len(wrong_answers)>3:
#         play_again = input("Do you want to play again? Y/N")
#         if play_again.lower()=="Y":
#             ask_question(data)
#         else:
#             print("Thanks for playing")

#     return(wrong_answers)

# def check_score(wrong_answers):
#     total_questions = len(data)
#     correct_answers = total_questions-len(wrong_answers)
#     print (f"You got {correct_answers} correct and {len(wrong_answers)} wrong.\nThese are the questions you got wrong, the correct answer and your answer")
#     for answer in wrong_answers:
#         print(f"Question: {answer['question']}")
#         print(f"Your Answer: {answer['Your Answer']}")
#         print(f"Correct Answer: {answer['Right Answer']}")
#         print() 


# check_score(ask_question(data))

# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Let’s say retirement age is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return the age (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints

# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message informing the user whether they can retire or not.


# def get_age (year,month,day):
#     current_year=2024
#     current_month="April"
#     age=current_year-year
#     return (age)

# def can_retire(gender,date_of_birth):
#     date_of_birth = date_of_birth.split("/")
#     year=int(date_of_birth[0])
#     month=int(date_of_birth[1])
#     day=int(date_of_birth[2])
#     user_age=get_age(year,month,day)
#     if gender.lower()=='m' and 67<=user_age or gender.lower()=='f' and 62<=user_age:
#         return ("Can retire")
#     else:
#         return ("Cannot retire")
    

# gender,birthdate = map(str,input ("Enter a gender and a birthdate (yyyy/mm/dd)\n").split(" "))
# print(can_retire (gender, birthdate))

# Exercise 4:
# Instructions
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:

# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

# Hint: treating our number as a int or a str at different points in our code may be helpful

def multiply (value):
    str_value=str(value)
    str_value=(f"{str_value*1}+{str_value*2}+{str_value*3}+{str_value*4}")
    lst_value = str_value.split("+")
    int_lst = (int(num) for num in lst_value)

    return sum(int_lst)

print (multiply(3))


