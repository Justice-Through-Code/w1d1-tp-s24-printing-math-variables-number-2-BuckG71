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
    # I used a return statement to return the student name input and the calculated average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"('{student_name}', {int(average_grade)})")