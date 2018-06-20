from flask import Flask, Response, request
import json
app = Flask(__name__)

@app.route('/test', methods = ['POST'])
def log():
    errorDes = request.form['Error Description']
    lineNo = request.form['Line No']
    filename = request.form['File name']
    platform = request.form['Platform']

    ret = json.dumps({"Error Description":errorDes , "Line No" : lineNo, "File name": filename, "Platform" : platform})
    with open('errorLog.txt', 'w') as f:
        json.dump(ret, f)
    return Response(ret, mimetype = 'application/json')

if __name__ == "__main__":
    app.run(debug = True)