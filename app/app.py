"""Driver code for the Psyche Explorer Flask app"""

# Imports
from flask import Flask, render_template, redirect, url_for, request
import numpy as np
import pandas as pd
import joblib

# Instantiating the Flask app
app = Flask('Spacefarer')

# Unpickling the trained model
model = joblib.load('../model/model.pkl')

# Mapping personality types to different astronaut roles
"""
0. Navigator → 'Dependable'
1. Communicator → 'Extraverted'
2. Explorer → 'Lively'
3. Commander → 'Responsible'
4. Scientist → 'Serious'

NOTE:
The numbers given above correspond to the integer values returned
by the trained model when making predictions.
"""

# Home route
@app.route('/')
@app.route('/home')
def home():
    """Route handler for homepage

    Returns:
        str: An HTML template of the homepage
    """
    return render_template('home.html')



# Handling the web-form of the personality test
@app.route('/personality-test', methods=['GET', 'POST'])
def handle_form():
    """Route handler for personality test

    Returns:
        str: An HTML template of the form for the personality test
    """

    if request.method == 'POST':

        # NOTE:
        # A POST request means that the user has submitted a completed form.

        # Obtaining gender and age:

        gender = 0

        if request.form.get('gender') == 'male':
            gender = 1

        # NOTE:
        # Gender has a default of 0 (female) since the ML model denotes the gender
        # of female samples as 0.

        age = int(request.form.get('age'))

        print(f'Gender is {gender}')
        print(f'Gender type is {type(gender)}')
        print(f'Age is {age}')
        print(f'Age type is {type(age)}')

        # Initializing variables to store total value for each personality trait:

        openness_total = 0
        neuroticism_total = 0
        conscientiousness_total = 0
        agreeableness_total = 0
        extraversion_total = 0

        # List of questions in web-form (for iteration):

        form_questions = ['q1', 'q2', 'q3', 'q4',
                          'q5', 'q6', 'q7', 'q8',
                          'q9', 'q10', 'q11', 'q12',
                          'q13', 'q14', 'q15', 'q16',
                          'q17', 'q18', 'q19', 'q20']

        # Iterating through web-form responses to get values for each personality trait:

        for question in form_questions[0:4]:
            openness_total = openness_total + int(request.form.get(question))

        for question in form_questions[4:8]:
            neuroticism_total = neuroticism_total + int(request.form.get(question))

        for question in form_questions[8:12]:
            conscientiousness_total = conscientiousness_total + int(request.form.get(question))

        for question in form_questions[12:16]:
            agreeableness_total = agreeableness_total + int(request.form.get(question))

        for question in form_questions[16:]:
            extraversion_total = extraversion_total + int(request.form.get(question))

        # Print statements to test total scores for each personality trait:

        print(f'openness_total is {openness_total}')
        print(f'neuroticism_total is {neuroticism_total}')
        print(f'conscientiousness_total is {conscientiousness_total}')
        print(f'agreeableness_total is {agreeableness_total}')
        print(f'extraversion_total is {extraversion_total}')

        # Packing total scores into a single list:

        scores = [openness_total,
                  neuroticism_total,
                  conscientiousness_total,
                  agreeableness_total,
                  extraversion_total]

        # Calculating the final scores for the personality traits, along with
        # the age and gender (to be input to the model for prediction):

        input_values = [gender, age]

        for score in scores:
            score = int(round(score / 2))
            input_values.append(score)

        # Final print statement to check whether everything runs smoothly:

        print(f'The final scores are {input_values}')

        personality_type = predict_personality(input_values)

        print(f'Personality type: {personality_type}')
        print(f'Data type of personality type: {type(personality_type)}')   # <class 'int'>

        return redirect(url_for('display_result', personality=personality_type))

    # This is the end of the if statement that handles POST requests.

    # Instead of a POST request, if this function receives a GET request, that means that
    # the user is trying to access the web-form. Thus, the function must return an HTML page
    # containing the web-form.

    # NOTE:
    # This doesn't need to be written inside the else condition.

    return render_template('form.html')


def predict_personality(input_data):
    """Funtion to pass input data to model and get predictions

    Args:
        input_data (list): A list of integers which will make up the input vector for the model

    Returns:
        list: An HTML template of the form for the personality test
    """
    input_vector = [np.array(input_data)]
    print(input_vector)

    # The input vector by itself is only a list of integer values. Column names must be added
    # to it, as the model has trained on a DataFrame with column names. Making predictions using
    # the input vector as it is throws a UserWarning.

    # Adding column names to input vector:

    features = ['gender',
                'age',
                'openness',
                'neuroticism',
                'conscientiousness',
                'agreeableness',
                'extraversion']

    input_vector_with_columns = pd.DataFrame(input_vector, columns=features)

    # Get prediction from model:

    prediction = model.predict(input_vector_with_columns)
    print(f'Predicted personality type: {prediction}')
    print(f'Data type of prediction: {type(prediction)}')   # Output is <class 'numpy.ndarray'>

    # Convert prediction from Numpy array to integer value before returning:

    return prediction.item()



# Display personality type after prediction
@app.route('/result')
def display_result():
    """Route handler to display the results of the personality test

    Returns:
        str: An HTML template of the results page
    """
    personality = int(request.args.get('personality'))
    print(f'Personality type to be displayed: {personality}')
    print(f'Data type of personality type to be displayed: {type(personality)}')

    astronaut_types = ['Navigator', 'Communicator', 'Explorer', 'Commander', 'Scientist']
    astronaut_info = {
        'Navigator': "As a Navigator, you're the bedrock of every space mission. Your unwavering commitment to precision and attention to detail ensures that every trajectory is flawlessly calculated. You're dependable and steadfast, steering the spacecraft through the cosmos with impeccable accuracy.",
        'Communicator': "As a Communicator, you light up the spacecraft with your vibrant energy and social finesse. You foster camaraderie among crew members, build connections with other stations, and transmit messages back to Earth. Your extroverted nature makes every interaction a memorable event, bridging gaps across the vastness of space.",
        'Explorer': "As an Explorer, you possess an insatiable curiosity that fuels your ventures into the unknown. Your liveliness and zest for discovery lead you to chart uncharted territories, investigate celestial phenomena, and collect data that expands our understanding of the universe. You remind us that every star is a potential revelation.",
        'Commander': "As a Commander, you bear the weight of leadership with grace and resilience. Your responsible nature ensures that the crew operates like a well-oiled machine, making crucial decisions and maintaining the ship's integrity. With your unwavering resolve, you guide the crew through challenges, setting the course for success.",
        'Scientist': "As a Scientist, you dive deep into the intricacies of space, approaching every experiment with a serious and methodical approach. Your analytical mind unravels cosmic mysteries, deciphering the language of the cosmos and uncovering the secrets hidden within the stars. Your contributions illuminate the universe's grand design."
    }

    # NOTE
    # The above array's items have been specifically placed in the given order so that
    # their indices match the predictions that the model makes.

    return render_template('result.html',
                           astronaut=astronaut_types[personality],
                           astronaut_info=astronaut_info)



# Start up Flask app
if __name__ == '__main__':
    app.run(debug=True)
