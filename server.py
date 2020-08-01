from flask import Flask , render_template, url_for, request,redirect
import pprint
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:link_name>')
def html_page(link_name=None):
    return render_template(link_name)



def write_text_database(data):
    with open('database.txt' , mode="a") as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        fieldnames = ['email','subject','message']
        database.write(f'\n {email=} {subject=} {message=}')


def write_csv_database_way1(data):
    with open('database_way1.csv' , mode="a",newline='') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        fieldnames = ['email', 'subject','message']
        writer = csv.DictWriter(database2, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'email':email,'subject':subject,'message':message})


def write_csv_database_way2(data):
    with open('database_way2.csv' , mode="a" ,newline='') as database3:
        email=data['email']
        subject=data['subject']
        message=data['message']
        spamwriter = csv.writer(database3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([email,subject,message])

# POST means browser wants us to save information
# Get means browser wants us to send information
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            pprint.pprint(data)
            write_csv_database_way1(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database"
    else:
        return "This is a Get Request"



