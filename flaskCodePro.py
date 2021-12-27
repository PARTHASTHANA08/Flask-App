from flask import Falsk,jsonify,request

app = Flask(__name__)
tasks = [
    {
        "ID": 1,
      "Name" : "Nikhil Saxena",
      "contact No." : "98523*****",
      "Work Done" : "True"
    },
    {
        "ID": 2,
        "Name" : "Anjali Mishra",
        "contact No." : "96326*****",
        "Work Done" : "False"
    }
]
@app.route("/get-data")
def given_data():
    return jsonify({
        "data" : tasks
    })
@app.route("/add-data",methods = ["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status" : "Error",
            "message" : "Please provide the data"
        })
    task = {
        "ID" : tasks[-1]["id"] + 1,
        "Work Done" : request.json["Work Done"]
    }    
    tasks.append(task)
    return jsonify({
        "status" : "success",
        "message" : "task added successfully"
    })
@app.route("/")
def home():
    return "this is home page"
if(__name__ == "__main__"):
    app.run(debug = True)
