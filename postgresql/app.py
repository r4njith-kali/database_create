from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname = 'employee_db',
        user = 'ranjith',
        password = 'ranjith',
        host = 'localhost'
    )
    return conn

@app.route('/employees', methods = ['GET'])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return jsonify(employees)

@app.route('/employees', methods = ['POST'])
def add_employee():
    new_employee = request.get_json()
    name = new_employee['name']
    age = new_employee['age']
    position = new_employee['position']
    department = new_employee['department']
    salary = new_employee['salary']
    hire_date = new_employee['hire_date']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (name, age, position, department, salary, hire_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (name, age, position, department, salary, hire_date))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'status': 'Employee added'}), 201

@app.route('/employees/<int:id>', methods = ['DELETE'])
def delete_employee(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'status': 'Employee deleted'})

@app.route('/employees/<int:id>', methods = ['PUT'])
def update_employee(id):
    updated_employee = request.get_json()
    name = updated_employee['name']
    age = updated_employee['age']
    position = updated_employee['position']
    department = updated_employee['department']
    salary = updated_employee['salary']
    hire_date = updated_employee['hire_date']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        UPDATE employees
        SET name = %s, age = %s, position = %s, department = %s, salary = %s, hire_date = %s
        WHERE id = %s
        ''', (name, age, position, department, salary, hire_date, id)
    )

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'status': 'Employee updated'})

@app.route('/')
def home():
    return '✅ Employee Management API is running!'


if __name__ == '__main__':
    app.run(debug = True)



