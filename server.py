from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from dateutil import relativedelta
import csv


app = Flask(__name__)

start_date = datetime.strptime('7/11/1996', "%d/%m/%Y")
end_date = datetime.today()
lifespan = relativedelta.relativedelta(end_date, start_date)

def save_to_csv(data):
    with open('form_data.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames = ['name','email','message'])
        writer.writerow(data)

@app.route('/')
@app.route('/index')
def landing():
    return render_template('index.html', years = lifespan.years)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name+'.html', years = lifespan.years)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_to_csv(data)
        return redirect(url_for('html_page', page_name='thankyou')+'#form')
    else:
        return 'error! message not saved!'

if __name__ == "__main__":
    app.run()