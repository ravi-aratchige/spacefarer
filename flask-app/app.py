from flask import Flask, render_template, url_for, request, redirect

app = Flask('Psyche Explorer')

questions = ['Do you enjoy exploring new ideas and concepts?',
             'Are you open to thinking in different and unconventional ways?',
             'Are you comfortable with change and adapting to new situations?',
             'Do you like trying out new experiences and learning from different perspectives?']


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form-v2.html', questions=questions)

# IMPORTANT:
# the below function is the currently operational form-handling function:

@app.route('/form-v1', methods=['GET', 'POST'])
def form_v1():

    if request.method == 'POST':

        # NOTE:
        # A POST request means that the user has submitted a completed form.

        # initializing variables to store total value for each personality trait

        openness_total = 0
        conscientiousness_total = 0
        extraversion_total = 0
        agreeableness_total = 0
        neuroticism_total = 0

        # list of questions in web-form (for iteration)

        form_questions = ['q1', 'q2', 'q3', 'q4',
                          'q5', 'q6', 'q7', 'q8',
                          'q9', 'q10', 'q11', 'q12',
                          'q13', 'q14', 'q15', 'q16',
                          'q17', 'q18', 'q19', 'q20']
        
        # iterating through web-form responses to get values for each personality trait

        for question in form_questions[0:4]:
            openness_total = openness_total + int(request.form.get(question))

        for question in form_questions[4:8]:
            conscientiousness_total = conscientiousness_total + int(request.form.get(question))

        for question in form_questions[8:12]:
            extraversion_total = extraversion_total + int(request.form.get(question))

        for question in form_questions[12:16]:
            agreeableness_total = agreeableness_total + int(request.form.get(question))

        for question in form_questions[16:]:
            neuroticism_total = neuroticism_total + int(request.form.get(question))

        # print statements to test total scores for each personality trait

        print(f'openness_total is {openness_total}')
        print(f'conscientiousness_total is {conscientiousness_total}')
        print(f'extraversion_total is {extraversion_total}')
        print(f'agreeableness_total is {agreeableness_total}')
        print(f'neuroticism_total is {neuroticism_total}')

        # packing total scores into a single list

        scores = [openness_total,
                  conscientiousness_total,
                  extraversion_total,
                  agreeableness_total,
                  neuroticism_total]
        
        # calculating the final scores (to be input to the model for prediction)
        
        final_scores = []

        for score in scores:
            score = int(round(score / 2))
            final_scores.append(score)

        # final print statement to check whether everything runs smoothly

        print(f'The final scores are {final_scores}')

        return final_scores
    
    # This is the end of the if statement that handles POST requests.
    
    # Instead of a POST request, if this function receives a GET request,
    # the user is trying to access the web-form. Thus, the function must return
    # an HTML page containing the web-form.

    # NOTE:
    # This doesn't need to be written inside the else condition

    return render_template('form-v1.html')

@app.route('/form-v2', methods=['GET', 'POST'])
def form_test():
    answers = []
    if request.method == 'POST':
    # Retrieve the selected answer from the form
        answer = request.form.get('answer')
        
        print(answer)
        
        # Process the selected answer, store it, or perform any other necessary actions
        answers.append(answer)
        
        # Determine the index of the current question
        current_question_index = int(request.form.get('question_index', 0))
        
        if current_question_index < len(questions) - 1:
            # Increment the question index to display the next question
            next_question_index = current_question_index + 1
            return render_template('form-v2.html', question=questions[next_question_index], question_index=next_question_index)
        else:
            # Display a thank you message or redirect to a different page
            # return render_template('home.html')
            print(answers)            
            return redirect(url_for('home'))
    else:
        # Display the first question when initially accessing the page
        return render_template('form-v2.html', question=questions[0], question_index=0)

if __name__ == '__main__':
    app.run(debug=True)