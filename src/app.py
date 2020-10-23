from flask import Flask 

app = Flask(__name__)

@app.route("/")
def Main():
    return "index.html"

def ReverseString(s):
    if len(s) == 0:
        return s 
    else:
        return ReverseString(s[1:]) + s[0]

if __name__ == "__main__":
    app.run(debug=True,port=5000)
