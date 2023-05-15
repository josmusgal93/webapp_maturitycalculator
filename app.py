from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    # Fetch the Python code from GitHub
    url = 'https://raw.githubusercontent.com/josmusgal93/webapp_maturitycalculator/main/maturity_calculator.py'

    response = request.get(url)
    python_code = response.text

    # Render the Python code in the HTML template
    return '''
        <html>
        <body>
            <pre><code>{}</code></pre>
        </body>
        </html>
    '''.format(python_code)


if __name__ == '__main__':
    app.run()
