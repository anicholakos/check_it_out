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

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root=os.path.join(current_dir, "static"))


@route('/')
def index():
    cur.execute('select * from users')
    try:
        if pwd_context.verify('loggedin', request.get_cookie('cookie')) == True:
            return manage_people()
    except:
        return template('templates/login.tpl') 

@post('/login')
def verify():
    form = request.forms
    uname = form.items()[0][1]
    try:
        cmd = "select password from users where username='%s'" % (uname)
        password = cur.execute(cmd).fetchone()[0]
        if pwd_context.verify(form['password'],password) == True:
            response.set_cookie('cookie', '$pbkdf2-sha256$8217$QaiV0lrLGYNQKiXkfE8pRQ$FhEjLt0armP9/6d.q2MeijH4gku5uSDKfmNzy0JQMy4')
            return manage_people()
        else:
            return index()
    except:
        return index()

@route('/persons')
def manage_people():
    try:
        if pwd_context.verify('loggedin', request.get_cookie('cookie')) == True:
            people = cur.execute('select * from persons').fetchall()
            form_ext = request.fullpath.split('/')[1]
            return template('templates/people.tpl', people=people, form_ext=form_ext)
    except:
        return index()



@route('/items')
def manage_items():
    try:
        if pwd_context.verify('loggedin', request.get_cookie('cookie')) == True:
            items = cur.execute('select * from items').fetchall()
            form_ext = request.fullpath.split('/')[1]
            return template('templates/items.tpl', items=items, form_ext=form_ext)
    except:
        return index()

@route('/add_form/<table>')
def add_form(table):
    try:
        if pwd_context.verify('loggedin', request.get_cookie('cookie')) == True:
            column_list = []
            for columns in cur.description:
                column_list.append(columns[0])
            return template('templates/addform.tpl', column_list=column_list, table=table)
    except:
        return index()

@route('/add_form/loans/<pid>')
def add_loan(pid):
    try:
        if pwd_context.verify('loggedin', request.get_cookie('cookie')) == True:
            column_list = []
            cur.execute("select * from loans")
            for columns in cur.description:
                column_list.append(columns[0])
            cmd = 'select * from persons where id=%s' % (pid)
            person_data = cur.execute(cmd).fetchone()
            person_known = dict(zip(column_list, person_data))
            tdt = datetime.date.today()
            return template('templates/addloan.tpl', column_list=column_list, table='loans', person=person_known, tdt=tdt)
    except:
        return index()

@post('/added/<table>')
def added(table):
    try:
        if pwd_context.verify('loggedin', request.get_cookie('cookie')) == True:
            ext_data = []
            import pdb; pdb.set_trace()
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

if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True)
