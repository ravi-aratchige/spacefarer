from flask import Flask, render_template, request

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
    return render_template('form_v2.html', questions=questions)

answers = []

@app.route('/form-test', methods=['GET', 'POST'])
def form_test():
    current_question_index = int(request.form.get('question_index', 0))
    
    while current_question_index < len(questions) - 1:
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
                return render_template('form_v2.html', question=questions[next_question_index], question_index=next_question_index)
            else:
                # Display a thank you message or redirect to a different page
                return render_template('home.html')
        else:
            # Display the first question when initially accessing the page
            return render_template('form_v2.html', question=questions[0], question_index=0)

if __name__ == '__main__':
    app.run(debug=True)