from flask import Flask, render_template, json, request
from sqlite3 import connect
from werkzeug.security import generate_password_hash

db_name = 'BucketList.sqlite'
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:
        # All Good, let's call SQLite
        # generate_password_hash defauts to SHA-1 and 1000 itterations
        _hashed_password = generate_password_hash(_password, method='pbkdf2:sha256:750000')
        error = sp_create_user(_name, _email, _hashed_password)

        if not error:
            return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error': 'User already exists'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


def sp_create_user(name, email, password):
    return_val = 1
    table_name = 'tbl_user'  # name of the table
    column_name = 'user_username'  # name of the column

    conn = connect(db_name)
    cursor = conn.cursor()

    cursor.execute('SELECT EXISTS(SELECT 1 FROM {tn} WHERE {cn}="{un}" LIMIT 1)'.
                   format(tn=table_name, cn=column_name, un=email))

    data = cursor.fetchall()[0][0]
    if not data:
        cursor.execute('INSERT INTO tbl_user ({cn1}, {cn2}, {cn3}) VALUES("{val1}", "{val2}", "{val3}")'.
                       format(cn1='user_name', cn2='user_username', cn3='user_password',
                              val1=name, val2=email, val3=password))
        conn.commit()
        return_val = 0

    conn.close()
    return return_val

if __name__ == "__main__":
    app.run()
