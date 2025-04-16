from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_data():
    with open('collated_benchmarks.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data

@app.route('/')
def index():
    model_filter = request.args.get('model', '')
    data = load_data()
    models = sorted(set(row['Model'] for row in data))
    if model_filter:
        data = [row for row in data if row['Model'] == model_filter]
    return render_template('index.html', data=data, models=models, selected=model_filter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
