# Initialize Maturity Score to 0
maturity_score = 0


# Define the function for incrementing maturity score based on answer
def increment_maturity_score(answer):
    global maturity_score
    if answer == 'a':
        maturity_score += 1
    elif answer == 'b':
        maturity_score += 2
    elif answer == 'c':
        maturity_score += 3
    elif answer == 'd':
        maturity_score += 4
    elif answer == 'e':
        maturity_score += 5


# Define the function for asking a question and returning the user's answer
# referencing: (Gitnux, 2023)
def ask_question(question, options):
    print(f"{question}")
    for i, option in enumerate(options):
        print(f"{chr(97 + i)}. {option}")
    while True:
        answer = input("Enter your answer (a-e): ").lower()
        if answer in ['a', 'b', 'c', 'd', 'e']:
            return answer
        else:
            print("Invalid input. Please enter a letter from a to e.")


# Define final question
# referencing: (Gitnux, 2023)
def ask_final_question(question, options):
    print(f"{question}")
    for i, option in enumerate(options):
        print(f"{chr(97 + i)}. {option}")
    while True:
        answer = input("Enter your answer (a-b): ").lower()
        if answer in ['a', 'b']:
            return answer
        else:
            print("Invalid input. Please enter a valid answer")


# Define maturity level ranges - referencing: (Falessi, Shaw and Mullen, 2014) Explanation: maximum score is 5 for
# each question. There are 7 questions in total, therefore maximum score attainable is 35. Each range will carry 7
# points. See implementation below.

initial_range = range(0, 8)  # low
managed_range = range(8, 16)  # low to medium
defined_range = range(16, 23)  # medium
quantitatively_managed_range = range(23, 30)  # medium to high
optimizing_range = range(30, 36)  # high

# Ask the 7 questions and increment maturity score based on answers
print("Answer each question by choosing the corresponding letter (a)-(e)")
question1 = "Question 1: Does your organization have security controls in place to protect your assets, " \
            "data and infrastructure?"
options1 = ["No security controls in place",
            "Ad hoc security controls in place",
            "Defined security controls in place and used consistently",
            "Quantitatively managed security controls",
            "Optimized security controls that are continuously improving"]
answer1 = ask_question(question1, options1)
increment_maturity_score(answer1)
print()

question2 = "Question 2: Does your organization have a formal incident response plan in place in case of a security " \
            "breach or incident?"
options2 = ["No incident response plan in place",
            "Ad hoc incident response plan in place",
            "Defined incident response plan in place and used consistently",
            "Quantitatively managed incident response plan",
            "Optimized incident response plan that is continuously improving"]
answer2 = ask_question(question2, options2)
increment_maturity_score(answer2)

print()
question3 = "Question 3: How does your organization monitor and detect potential security threats or vulnerabilities?"
options3 = ["No monitoring or detection in place",
            "Ad hoc monitoring and detection in place",
            "Defined monitoring and detection in place and used consistently",
            "Quantitatively managed monitoring and detection",
            "Optimized monitoring and detection that is continuously improving"]
answer3 = ask_question(question3, options3)
increment_maturity_score(answer3)

print()
question4 = "Question 4: How often does your organization conduct security risk assessments?"
options4 = ["No security risk assessments were conducted",
            "Ad hoc security risk assessments conducted",
            "Defined security risk assessments conducted regularly",
            "Quantitatively managed security risk assessments",
            "Optimized security risk assessments that are continuously improving"]
answer4 = ask_question(question4, options4)
increment_maturity_score(answer4)

print()
question5 = "Question 5: Does your organization provide security awareness training to employees?"
options5 = ["No security awareness training was provided",
            "Ad hoc security awareness training provided",
            "Defined security awareness training provided regularly",
            "Quantitatively managed security awareness training",
            "Optimized security awareness training that is continuously improving"]
answer5 = ask_question(question5, options5)
increment_maturity_score(answer5)

print()
question6 = "Question 6: How often do you perform Dynamic Application Security Testing (DAST) and/or vulnerability " \
            "scanning?"
options6 = ["Less than once a year",
            "Annually",
            "Twice a year",
            "Quarterly",
            "Monthly or more frequently"]
answer6 = ask_question(question6, options6)
increment_maturity_score(answer6)

print()
question7 = "Question 7: Have you obtained any Information Security certifications, such as ISO 27001?"
options7 = ["No",
            "Yes, but they are outdated or not relevant to our current operations",
            "Yes, and they are relevant to our current operations, but they have not been updated recently",
            "Yes, and they are relevant to our current operations, and they have been updated recently",
            "Yes, and we have multiple relevant certifications"]
answer7 = ask_question(question7, options7)
increment_maturity_score(answer7)

print()
print("You're overall Maturity Score is: ", maturity_score)
print("The maximum maturity score reachable by this assessment is:", 5 * 7)
print()

question8 = "Do you wish to know your maturity scoring, according to CMMI scoring systems for organisations " \
            "within the product development domain?"
options8 = ["Yes", "No"]
answer8 = ask_final_question(question8, options8)

if answer8 == "a":
    if 0 <= maturity_score <= 7:
        maturity_level = "Initial (Low)"
    elif 8 <= maturity_score <= 15:
        maturity_level = "Managed (Low to Medium)"
    elif 16 <= maturity_score <= 22:
        maturity_level = "Defined (Medium)"
    elif 23 <= maturity_score <= 29:
        maturity_level = "Quantitatively Managed (Medium to High)"
    elif 30 <= maturity_score <= 35:
        maturity_level = "Optimizing (High)"
    else:
        maturity_level = "Invalid maturity score"

print()
print("Maturity level: ", maturity_level)
