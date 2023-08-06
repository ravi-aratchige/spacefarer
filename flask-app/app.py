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

# the below function is the currently operational form-handling function:

@app.route('/form-v1', methods=['GET', 'POST'])
def form_v1():
    openness = []

    if request.method == 'POST':

        # getting the first five answers provided in the web-form
        a1 = int(request.form.get('q1'))
        a2 = int(request.form.get('q2'))
        a3 = int(request.form.get('q3'))
        a4 = int(request.form.get('q4'))

        # grouping the answers into a single list
        for item in [a1, a2, a3, a4]:
            openness.append(item)

        # get final score for trait
        openness_total = sum(openness)
        openness_score = openness_total / 2

        # EXPLANATION:
        # There are 4 questions for each personality trait. Each question has
        # 5 MCQ answers, scored from 1 to 5. Thus, the total obtained for a
        # single trait is taken out of 20 (5 x 4). To scale this down to be
        # taken out of 10 (as the machine learning model uses values between
        # 1 and 10 for each trait), we divide the collective total obtained for
        # each trait by 2.
        
        print(f'Responses for openness: {openness}')
        print(f'Final openness score: {openness_score}')
        print(f'Data type of openness score: {type(openness_score)}')
        return openness
    
    # page to be rendered when the above if-statement is passed, i.e. form page:
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