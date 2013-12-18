#!/usr/bin/env python3
import os
import sys
import sqlite3
import datetime
from crypt import pwd_context
from bottle import route, run, template, static_file, request, post, response

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
sys.path.append(current_dir)
conn = sqlite3.connect("database.db")
cur = conn.cursor()

def check_login():
    key = "loggedin"
    try:
        if pwd_context.verify(key, request.get_cookie('cookie')) == True:
            return True
        else:
            return False
    except:
        return False

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root=os.path.join(current_dir, "static"))


@route('/')
def index():
    cur.execute('select * from users')
    if check_login() == True:
        return manage_people()
    else:
        return template('templates/login.tpl')

@post('/login')
def verify():
    form = request.forms
    uname = form.items()[0][1]
    try:
        cmd = "select password from users where username='%s'" % (uname)
        password = cur.execute(cmd).fetchone()[0]
        if pwd_context.verify(form['password'],password) == True:
            response.set_cookie('cookie', "$pbkdf2-sha256$7376$u/c.JwQAQKiVcq71ntM6Rw$zQlWEpB6WMpS8oEKUrVs1oSDDdYMiwjRet5XISbYcm8")
            return manage_people()
        else:
            return index()
    except:
        return index()

@route('/persons')
def manage_people():
    people = cur.execute('select * from persons').fetchall()
    if check_login() == True:
        form_ext = 'persons'
        return template('templates/people.tpl', people=people, form_ext=form_ext)
    else:
        return index()

@route('/loans')
def manage_loans():
    loaned = cur.execute('select * from loans').fetchall()
    if check_login() == True:
        form_ext = request.fullpath.split('/')[1]
        return template('templates/loans.tpl', loaned=loaned, form_ext=form_ext)
    else:
        return index()

@route('/remove-loan')
def remove_loans():
    loaned = cur.execute('select * from loans').fetchall()
    names = []
    items = []
    if check_login() == True:
        for name in loaned:
            if name[2].strip() not in names:
                names.append(name[2].strip())
        for item in loaned:
            if item[4].strip() not in items:
                items.append(item[4].strip())
        return template('templates/rmloan.tpl', loaned=names, items=items)
    else:
        return index()

@post('/removing')
def removeing_loans():
    if check_login() == True:
        try:
            form_data = request.forms
            cmd = ("delete from loans where person_lname='%s ' and itemnum='%s ';") %(form_data['person_lname'], form_data['item_name'])
            cur.execute(cmd)
            conn.commit()
            cur.close
            return index()
        except:
            print("error")
            return index()
    else:
        return index()


@route('/items')
def manage_items():
    items = cur.execute('select * from items').fetchall()
    if check_login() == True:
        form_ext = request.fullpath.split('/')[1]
        return template('templates/items.tpl', items=items, form_ext=form_ext)
    else:
        return index()

@route('/add_form/<table>')
def add_form(table):
    if check_login() == True:
        column_list = []
        for columns in cur.description:
            column_list.append(columns[0])
        return template('templates/addform.tpl', column_list=column_list, table=table)
    else:
        return index()

@route('/add_form/loans/<pid>')
def add_loan(pid):
    if check_login() == True:
        column_list = []
        items = []
        cur.execute("select * from loans")
        for columns in cur.description:
            column_list.append(columns[0])
        cmd = 'select * from persons where id=%s' % (pid)
        person_data = cur.execute(cmd).fetchone()
        person_known = dict(zip(column_list, person_data))
        person_known.pop('item_id')
        person_known.pop('itemnum')
        uni_items = cur.execute("select id_num from items").fetchall()
        for item in uni_items:
            items.append(item[0].encode())
        return template('templates/addloan.tpl', column_list=column_list, table='loans', person=person_known, items=items)
    else:
        return index()
 
@post('/added/<table>')
def added(table):
    if check_login() == True:
        try:
            ext_data = []
            ext_data.append(table)
            if table == "loans":
                cur.execute("select * from loans")
            column_data = request.forms
            for key in cur.description:
                ext_data.append(column_data[key[0]])
            col_placeholder = "'%s '," * len(column_data.keys())
            cmd = ("insert into %s values (" + col_placeholder[:-1] + ')') % tuple(ext_data)
            cur.execute(cmd)
            conn.commit()
            cur.close
            return index()
        except:
            print("error")
            return index()
    else:
        return index()

@post('/added/loans')
def added_loan():
    if check_login() == True:
        try:
            column_data = request.forms
            cmd = "select pk from items where id_num=%s" % (column_data['itemnum'])
            column_data['item_id'] = cur.execute(cmd).fetchone()[0]
            column_data['checked_out'] = datetime.date.today()
            ext_data = []
            ext_data.append('loans')
            cur.execute("select * from loans")
            for key in cur.description:
                ext_data.append(column_data[key[0]])
            col_placeholder = "'%s '," * len(column_data.keys())
            cmd = ("insert into %s values (" + col_placeholder[:-1] + ')') % tuple(ext_data)
            cur.execute(cmd)
            conn.commit()
            cur.close
            return index()
        except:
            print("error")
            return index()
    else:
        return index()

if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True)
