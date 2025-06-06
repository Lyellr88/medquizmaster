import os
import random
from flask import Flask, render_template, request, session, redirect, url_for
from questions import QUESTIONS

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "medical-quiz-secret-key")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    specialty = request.form.get('specialty', 'mixed')
    difficulty = request.form.get('difficulty', 'easy')
    session['difficulty'] = difficulty

    timer_enabled = 'enable_timer' in request.form
    time_limit = request.form.get('time_limit', '').strip()
    if timer_enabled and (not time_limit.isdigit() or int(time_limit) <= 0):
        time_limit = 'N/A'

    session['timer_enabled'] = timer_enabled
    session['time_limit'] = time_limit

    if specialty == 'mixed':
        questions = QUESTIONS.copy()
    else:
        questions = [q for q in QUESTIONS if q['specialty'] == specialty]

    random.shuffle(questions)

    session['questions'] = questions
    session['current_index'] = 0
    session['score'] = 0
    session['answers'] = []
    session['specialty'] = specialty
    session['total_questions'] = len(questions)

    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    if 'questions' not in session:
        return redirect(url_for('index'))

    current_index = session.get('current_index', 0)
    questions = session.get('questions', [])

    if current_index >= len(questions):
        return redirect(url_for('results'))

    current_question = questions[current_index]
    progress = ((current_index + 1) / len(questions)) * 100

    return render_template('quiz.html',
                           question=current_question,
                           question_num=current_index + 1,
                           total_questions=len(questions),
                           progress=progress)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    if 'questions' not in session:
        return redirect(url_for('index'))

    selected_answer = request.form.get('answer')
    current_index = session.get('current_index', 0)
    questions = session.get('questions', [])

    if current_index >= len(questions):
        return redirect(url_for('results'))

    current_question = questions[current_index]
    correct_answer = current_question['answer']
    is_correct = selected_answer == correct_answer

    answer_record = {
        'question': current_question['question'],
        'selected': selected_answer,
        'correct': correct_answer,
        'is_correct': is_correct,
        'specialty': current_question['specialty'],
        'explanation': current_question.get('explanation', '')
    }

    session['answers'].append(answer_record)

    if is_correct:
        session['score'] = session.get('score', 0) + 1

    session['current_index'] = current_index + 1

    return redirect(url_for('quiz'))

@app.route('/results')
def results():
    if 'answers' not in session or not session['answers']:
        return redirect(url_for('index'))

    answers = session.get('answers', [])
    score = session.get('score', 0)
    specialty = session.get('specialty', 'mixed')
    difficulty = session.get('difficulty', 'easy')
    timer_enabled = session.get('timer_enabled', False)
    time_limit = session.get('time_limit', 'N/A')

    specialty_stats = {}
    for answer in answers:
        spec = answer.get('specialty', 'unknown')
        if spec not in specialty_stats:
            specialty_stats[spec] = {'correct': 0, 'total': 0}
        specialty_stats[spec]['total'] += 1
        if answer.get('is_correct'):
            specialty_stats[spec]['correct'] += 1

    percentage = (score / len(answers) * 100) if answers else 0

    return render_template('results.html',
                           answers=answers,
                           score=score,
                           total_questions=len(answers),
                           percentage=percentage,
                           specialty=specialty,
                           specialty_stats=specialty_stats,
                           difficulty=difficulty,
                           timer_enabled=timer_enabled,
                           time_limit=time_limit)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
