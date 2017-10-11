from flask import Flask, render_template, send_from_directory, send_file
from taichi.misc.settings import get_output_directory
import os
from taichi import get_output_directory
from flask_cors import CORS

app = Flask(__name__)
#CORS(app)


@app.route('/viewer/<path:path>')
def send_front_end_file(path):
  return send_from_directory('viewer', path)

@app.route('/data/<path:path>')
def send_data_file(path):
  path = os.path.join(get_output_directory(), path)
  print(path)
  return send_file(path)


@app.route('/')
def browse_outputs():
  output_dir = get_output_directory()
  dirs = os.listdir(output_dir)
  dirs = sorted(dirs)
  entries = []
  for d in dirs:
    entries.append({
        'title': d,
        'text': '',
    })
  return render_template('browser.html', entries=entries)


@app.route('/view/<folder>')
def view(folder):
  output_dir = get_output_directory()
  return render_template('view.html', folder=folder)


def get_pakua_server():
  return app
