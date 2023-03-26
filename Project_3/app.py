# Step 1 - To import FLASK
from flask import Flask, request, render_template
import re

# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)

# Step 3 - Create an END POINT using routes and bind them with a functionality
@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def match_regex():
    # Get the test string and regular expression from the form submission
    text_string = request.form['text_string']
    regular_expression = request.form.get('regular_expression')

    # Find all matches in the string using the regular expression
    matches = re.findall(regular_expression, text_string)

    # Render the results page with the matches
    return render_template('result.html', matches=matches)

    # Step 4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)