from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)
# flask --app server --debug run


@app.route("/")
def hello_world():
    return render_template('./index.html')


@app.route("/<string:page>")
def pag(page="index.html"):
    return render_template(f'./{page}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        try:
            to_csv(data)
        except:
            return 'wrung'
        return redirect('thankyou.html')
    else:
        return 'dog'


def to_txt(dat):
    with open('./info.txt', mode='a') as file:
        file.write(str(dat))


def to_csv(dat):
    with open('./info.csv', mode='a') as file:
        email = dat['email']
        sub = dat['subject']
        mes = dat['message']
        csv_wr = csv.writer(file, delimiter=',',
                            quotechar='\\', quoting=csv.QUOTE_MINIMAL)
        csv_wr.writerow([email, sub, mes])
