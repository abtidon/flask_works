from flask import Flask, render_template
import cx_Oracle

app = Flask(__name__)

# Oracle database connection details
oracle_connection_details = {
    'user': 'your_username',
    'password': 'your_password',
    'dsn': 'your_oracle_dsn',
}

# Route for the report page
@app.route('/')
def show_report():
    try:
        # Establish a connection to the Oracle database
        connection = cx_Oracle.connect(**oracle_connection_details)
        cursor = connection.cursor()

        # Execute a query to fetch data from the 'monlog' table
        query = 'SELECT * FROM monlog'
        cursor.execute(query)

        # Fetch all rows from the result set
        result_set = cursor.fetchall()

        # Column names
        column_names = [description[0] for description in cursor.description]

        return render_template('report.html', column_names=column_names, result_set=result_set)

    except cx_Oracle.DatabaseError as e:
        return f"Database Error: {e}"
    finally:
        # Close the database connection
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
