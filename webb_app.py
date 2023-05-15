from flask import Flask, render_template, request

app = Flask(maturity_calculator)

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

# Define the routes and corresponding view functions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    global maturity_score
    maturity_score = 0

    question1 = request.form['question1']
    increment_maturity_score(question1)

    question2 = request.form['question2']
    increment_maturity_score(question2)

    # Continue with the remaining questions...

    return render_template('result.html', maturity_score=maturity_score)

if maturity_calculator == '__main__':
    app.run(debug=True)
