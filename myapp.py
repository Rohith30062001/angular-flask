import mysql.connector as mysql
from flask import jsonify,Flask,render_template,redirect,request
from flask_cors import CORS, cross_origin



db=mysql.connect(host="localhost",user="admin",password="password",database='employee')
print(db)
cursor=db.cursor()

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/',methods = ['POST', 'GET'])
@cross_origin(supports_credentials=True)
def insert():
    #return 'Welcome To Employee DB'
    json = request.json
    print('hitted')
    if json.get('userid') is None or json.get('userid')=='':
        print('entered normal')
        query="INSERT INTO EMPLOYEEDATA (FIRSTNAME,LASTNAME,MOBILENUMBER,DOB,GENDER,ADRESS,EMAIL,DESIGNATION,CHECKBOX) VALUES (%s, %s , %s, 			%s, %s, %s, %s, %s, %s)"
        values=(json.get('username'),json.get('surname'),json.get('mobile'),json.get('dob'),json.get('gender'),json.get('adress'),json.get('email'),json.get('type'),json.get('remeber'))
        cursor.execute(query,values)
        db.commit()
        return {'message': 'done!!!'}
    else:
        print('entered edit')
        query='''UPDATE EMPLOYEEDATA
                SET FIRSTNAME = %s, LASTNAME = %s, MOBILENUMBER = %s, DOB = %s, GENDER = %s, ADRESS = %s, EMAIL = %s, DESIGNATION = %s, CHECKBOX = %s
                WHERE ID = %s;
                '''
        values=(json.get('username'),json.get('surname'),json.get('mobile'),json.get('dob'),json.get('gender'),json.get('adress'),json.get('email'),json.get('type'),json.get('remeber'),json.get('userid'))
        cursor.execute(query,values)
        db.commit()
        return {'message': 'done!!!'}


@app.route('/employees',methods = ['POST', 'GET'])
@cross_origin(supports_credentials=True)
def getusers():
    print("hitted users")
    query="SELECT * FROM EMPLOYEEDATA;"
    cursor.execute(query)
    data = cursor.fetchall()
    print("data",data)

    return data

if __name__ == '__main__':
    app.run(debug=True)
