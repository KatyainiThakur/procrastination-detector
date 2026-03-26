from flask import Flask, render_template, request, redirect, url_for
from analyzer import BehaviorAnalyzer, Task
from storage import Storage

app = Flask(__name__)

@app.route('/')
def index():
    raw_data = Storage.load_tasks()
    tasks = [Task(**d) for d in raw_data]
    score, status, insights = BehaviorAnalyzer.calculate_score(tasks)
    return render_template('index.html', tasks=tasks, score=score, status=status, insights=insights)

@app.route('/add', methods=['POST'])
def add_task():
    name = request.form.get('name')
    priority = request.form.get('priority')
    Storage.add_single_task(name, priority)
    return redirect(url_for('index'))

@app.route('/complete/<name>')
def complete_task(name):
    Storage.mark_completed(name)
    return redirect(url_for('index'))

@app.route('/delete/<name>')
def delete_task(name):
    Storage.delete_task(name)
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    Storage.save_tasks([])
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Setting host to '0.0.0.0' allows the custom name mapping to work
    app.run(debug=True, host='0.0.0.0', port=5001)