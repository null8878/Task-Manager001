from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = [] # Consider using a list of dictionaries for more complex tasks later

@app.route('/')
def index():
    # Pass tasks with their indices
    return render_template('index.html', tasks=enumerate(tasks))

@app.route('/add', methods=['POST'])
def add():
    task_content = request.form.get('task')
    if task_content:
        tasks.append(task_content)
    return redirect(url_for('index')) # Use url_for for better routing

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)