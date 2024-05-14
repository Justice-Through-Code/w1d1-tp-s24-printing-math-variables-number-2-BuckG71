def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    # I used the input function to prompt the user for their name
    student_name = input("What is your name? ")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    # I used the input function to prompt the user for the needed inputs
    math_score = input("What was your Math score? ")
    science_score = input("What was your Science score? ")
    english_score = input("What was your English score? ")

    # Calculate the average grade
    '''Since user inputs are strings, I type converted them to integers before calculating the average grade'''
    average_grade = (int(math_score) + int(science_score) + int(english_score)) / 3

    # Return the student's name and their average grade
    ''' I've added a print statement here to print the student's name and their average grade, and I type converted the average grade to an integer since school grades are usually whole numbers'''
    return print(f"{student_name}'s average grade is {int(average_grade)}.")

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"")