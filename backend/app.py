from flask import Flask, request, jsonify
import webbrowser
from tasks import open_application
from reminder import set_reminder
from web_search import search_web

app = Flask(__name__)

@app.route('/perform-task', methods=['POST'])
def perform_task():
    data = request.json
    task_type = data.get('task_type')
    task_detail = data.get('task_detail')

    if task_type == 'open_application':
        response = open_application(task_detail)
    elif task_type == 'set_reminder':
        response = set_reminder(task_detail)
    elif task_type == 'search_web':
        response = search_web(task_detail)
    else:
        response = {"status": "error", "message": "Invalid task type"}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
