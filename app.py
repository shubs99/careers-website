from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'kolkata,India',
  'salary': '1,00,000'
}, {
  'id': 2,
  'title': 'Front end engineer',
  'location': 'Delhi,India',
}, {
  'id': 3,
  'title': 'Data Scientist',
  'location': 'Mumbai,India',
  'salary': '15,00,000'
}, {
  'id': 4,
  'title': 'Data engineer',
  'location': 'banagalore,India',
  'salary': '11,00,000'
}]


@app.route("/")
def hello_World():
  return render_template('home.html', jobs=JOBS, company_name='jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
