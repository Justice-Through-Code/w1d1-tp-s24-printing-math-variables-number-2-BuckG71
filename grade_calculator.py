def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    # I used the input function to prompt the user for their name
    student_name = input("What is your name? ")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    # I used the input function to prompt the user for the needed inputs and simultaneously converted the input from a string to a float using the float function
    math_score = float(input("What was your Math score? "))
    science_score = float(input("What was your Science score? "))
    english_score = float(input("What was your English score? "))

    # Calculate the average grade
    # Used simple arithmetic to calculate the average grade
    average_grade = (math_score + science_score + english_score) / 3

    # Return the student's name and their average grade
    # I've added a print f statement here to print the student's name and their average grade.
    return print(f"{student_name}'s average grade is {average_grade}.")

if __name__ == '__main__':
    # Call the calculate_average_grade function
    calculate_average_grade()

    # Print the student's name and their average grade
    # print(f"{student_name}'s average grade is {average_grade}")