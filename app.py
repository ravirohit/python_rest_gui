from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api # resource, 

app = Flask(__name__)
api = Api(app)

CORS(app)

employeeData={"1":{
    "id":"1",
    "name":"rohit",
    "phone":"#1234555"
},
"2":{
    "id":"2",
    "name":"ravi",
    "phone":"#33333333"
}
}

@app.route("/")
def home():
    print("home method get called")
    return "Congratulation! you test resources get called :)"

@app.route("/hello/<id>")
def getEmplyeeInfo(id):
   # print(f"Hello Mr. {name}!... Welcome to python learning.")
    print("employee is :\n{}".format(employeeData.get(id)))
    #return jsonify(employeeData.get(id))
    messsage='Hey Rohit... Welcome to our python GUI learning'
    return render_template('info.html',name = messsage)

@app.route("/store",methods=['POST','GET'])
def storeData():
    print('store method get called')
    print('payload in the request:{}'.format(request.json))
    return jsonify({'status':'data has been stored successfully'})

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

class Employees_Name(Resource):
    def get(self, employee_id):
        print('Employee id:' + employee_id)
        result = {'data': {'id':1, 'name':'Balram'}}
        return jsonify(result)       


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
   app.run(port=5002)        #This application initializes a Flask app
   

