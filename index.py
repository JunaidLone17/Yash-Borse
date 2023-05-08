from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # Get the text from the text box
    text = request.form['text']

    # Get the image file
    file = request.files['file']

    # Save the image file
    file.save('tocheck.png')
    import Pankaj as pj
    res = pj.eval(text, 'tocheck.png')
    x = {
        'IsGenuine': res[0],
        'SimilarityScore': res[1],
        'SimScoreCheck': res[2]
    }

    return render_template("Result.html", result=x)


if __name__ == '__main__':
    app.run(debug=True)
