from flask import Flask, send_from_directory , render_template, g, send_file, make_response, request, abort, redirect, flash, session , url_for, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from flask_login import LoginManager, login_user, login_required, UserMixin, logout_user, current_user
from werkzeug.utils import redirect, secure_filename
from passlib.hash import sha256_crypt
from datetime import datetime, timedelta
import os, time, base64
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')
from flask_redis import FlaskRedis
from flask_login import login_required
import matplotlib.pyplot as plt
from collections import defaultdict

from lib_database import db, User, Librarian, Section, Issue, Book

from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from mail import send_scheduled_email, send_scheduled_report_email

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

app.secret_key = "Aryan_Pratap_@_456456"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///lib_database.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False

db.init_app(app)
with app.app_context():
    db.create_all()
 

CORS(app, resources={r"/*": {'origins':"*"}})

Dict={}

@app.route('/', methods=['GET', 'POST'])
def Homepage():
    return render_template('home.html')

@app.route('/shark', methods=['GET', 'POST'])
def Shark():
    return('backend data')

@app.route('/librarianhome', methods=['GET', 'POST'])
def LibrarianHome():
    L=[]
    s_data,b_data=[],[]
    sec=Section.query.all()
    for i in sec:
        s_data.append({
            'id':i.section_id,
            'section_name':i.section_name
        })
    book=Book.query.all()
    for i in book:
        b_data.append({
            'book_id':i.book_id,
            'book_name':i.book_name,
            'authors':i.authors,
            'file_data':i.file_data,
            'section_id_r':i.section_id
        })
    L.append(s_data)
    L.append(b_data)
    print(L)
    return L

@app.route('/userhome', methods=['GET', 'POST'])
def UserHome():
    l=[]
    s_data,b_data=[],[]

    if 'cur_user' not in Dict:
            abort(401)  # Unauthorized

    sec=Section.query.all()
    for i in sec:
        s_data.append({
            'id':i.section_id,
            'section_name':i.section_name
        })
    book=Book.query.all()
    for i in book:
        b_data.append({
            'book_id':i.book_id,
            'book_name':i.book_name,
            'authors':i.authors,
            'file_data':i.file_data,
            'section_id_r':i.section_id
        })
    #print(session['user'])
    user=User.query.filter_by(user_email=Dict["cur_user"].user_email).first()
    l.append(s_data)
    l.append(b_data)
    l.append(Dict['cur_user'].user_email)
    return l

@app.route('/requestdata')
def request_data():
    L,r_data=[],[]
    issue=Issue.query.filter_by(status="pending").all()
    for i in issue:
        r_data.append({
            'book_name':i.book.book_name,
            'section_name': i.book.section.section_name,
            'user_id':i.user_id,
            'user_email': i.user.user_email, 
            'book_id':i.book_id
        })
    L.append(r_data)
    return L

@app.route('/confirmrequest/<book_id>', methods=['POST'])
def confirm_request(book_id):
    data=request.get_json()
    issue=Issue.query.filter_by(book_id=book_id).first()
    if issue:
        issue.status = data.get('status')
        issue.issue_date = datetime.now()
        db.session.commit()
        return jsonify({"message": "Request accepted or declined"})
    else:
        return jsonify({"error": "Issue not found"}), 404

@app.route('/userissuepage')
def user_issued_page():
    L,u_data=[],[]
    seven_days_ago = datetime.now() - timedelta(days=7)
    #var=Issue.query.filter_by(user_id=Dict['cur_user'].user_id, status="approved", issue_date > seven_days_ago).all()
    var = Issue.query.filter(Issue.user_id == Dict['cur_user'].user_id,
                             Issue.status == "approved",
                             Issue.issue_date >= seven_days_ago).all()
    for i in var:
        u_data.append({
            'book_name':i.book.book_name,
            'section_name': i.book.section.section_name,
            'book_id':i.book_id,
            'time': i.issue_date,
            'user_email':Dict['cur_user'].user_email
        })
    L.append(u_data)
    return L

@app.route('/downloadbook/<book_id>')
def download_book(book_id):
    file_record = Book.query.filter_by(book_id=book_id).first()
    if file_record is not None:
        response = make_response(send_file(file_record.file_data, as_attachment=True))
        response.headers["Content-Disposition"] = f"attachment; filename={file_record.book_name}"
        return response
    else:
        return "Book not found", 404

@app.route('/viewpdf/<book_id>')
def view_pdf(book_id):
    file_record = Book.query.filter_by(book_id=book_id).first()
    if file_record is not None:
        return send_file(file_record.file_data, mimetype='application/pdf')
    else:
        return "Book not found", 404


@app.route('/createsection', methods=['POST'])
def create_section():
    data=request.get_json()
    section=Section(section_name=data.get('section_name',None))
    db.session.add(section)
    db.session.commit()
    return jsonify('section successfully added')

@app.route('/createbook', methods=['POST'])
def create_book():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    book_name = request.form.get('book_name')
    authors = request.form.get('authors')
    section_id = request.form.get('section_id')

    book = Book(
        book_name=book_name,
        authors=authors,
        file_data=file_path,
        section_id=section_id
    )
    
    db.session.add(book)
    db.session.commit()
    
    return jsonify({'message': 'Book successfully added'})


@app.route('/updatesection/<int:id>', methods=['POST'])
def update_section(id):
    data=request.get_json()
    section=Section.query.filter_by(section_id=id).first()
    section.section_name=data.get("section_name")
    db.session.commit()
    return jsonify('Section successfully updated')

@app.route('/updatebook/<book_id>', methods=['POST'])
def update_book(book_id):
    data=request.get_json()
    book=Book.query.filter_by(book_id=book_id).first()
    book.book_name=data.get("book_name")
    book.authors=data.get("authors")
    db.session.commit()
    return jsonify('Book/File successfully updated')

@app.route('/deletesection/<id>')
def delete_section(id):
    secd=Section.query.filter_by(section_id=id).first()
    db.session.delete(secd)
    db.session.commit()
    return jsonify('section deleted...')

@app.route('/deletebook/<book_id>')
def delete_book(book_id):
    book=Book.query.filter_by(book_id=book_id).first()
    db.session.delete(book)
    db.session.commit()
    return jsonify('Book deleted successfully...')

@app.route('/issueRequest/<book_id>', methods=['POST'])
def issue_request(book_id):
    data=request.get_json()
    user_approved_issue_count = Issue.query.filter(and_(Issue.user_id == Dict['cur_user'].user_id, Issue.status == "approved")).count()
    print(user_approved_issue_count)
    if user_approved_issue_count >= 5:
        return jsonify('You have already made the maximum number of issue requests.'), 400

    issue=Issue(book_id=book_id,
                status="pending",
                user_id=Dict['cur_user'].user_id)
    db.session.add(issue)
    db.session.commit()
    return jsonify('Issue request successfully sent')



@app.route('/registerlibrarian', methods=['POST'])
def librarianregister():
    a_data=request.get_json()
    enc_pas=sha256_crypt.encrypt(a_data.get('password',None))
    dataa=Librarian(librarian_email=a_data.get('email',None),password=enc_pas)
    db.session.add(dataa)
    db.session.commit()
    return jsonify('Librarian registration has successfully done !')

@app.route('/registeruser', methods=['POST'])
def userregister():
    u_data=request.get_json()
    enc_pas=sha256_crypt.encrypt(u_data.get('password',None))
    dataa=User(user_email=u_data.get('email',None),password=enc_pas)
    db.session.add(dataa)
    db.session.commit()
    return jsonify('User registration has successfully done !')

@app.route('/search', methods=['POST', 'GET'])
def Search():
    s_data=request.get_json()
    section_output=Section.query.filter(
        (Section.section_name.like('%'+ s_data.get('search',None) + '%'))
        ).all()

    book_output=Book.query.filter(
        (Book.book_name.like('%' + s_data.get('search', None) + '%')) |
        (Book.authors.like('%' + s_data.get('search', None) + '%'))
    ).all()

    if request.method=='POST':
        if section_output:
            section_list = [{'section_name': section.section_name} for section in section_output]
            return jsonify({'status':'Data is present','val':section_list})
        if book_output:
            book_list = [{'book_name': book.book_name, 'author': book.authors} for book in book_output]
            return jsonify({'status':'Data is present','val':book_list})
        return jsonify({'status':'Data is not present'})
    if request.method=='GET':
        return jsonify({'val':output})

@app.route('/loginlibrarian',methods=['POST'])
def librarianlogin():
    AL_data=request.get_json()
    email=AL_data.get("email")
    password=AL_data.get("password") 
    librarian=Librarian.query.filter_by(librarian_email=email).first()
    #session['admin_email']=email
    if librarian is None:
        return jsonify('User does not exist !!')
    if librarian and sha256_crypt.verify(password,librarian.password):
        return jsonify({'status':'success','message':'successfully logged in'})
    return jsonify('Invalid password')

@app.route('/logoutlibrarian')
def librarianlogout():
    librarian_emails = session.get('librarian_email')
    if librarian_emails is not None:
        #print(session['admin_email'])
        #session.pop('admin_email', None)
        return jsonify("librarian is logged out")
    else:
        return jsonify("No active session. Librarian is not logged in.")

@app.route('/loginuser', methods=['POST'])
def userlogin():
    UL_data = request.get_json()
    email = UL_data.get("email")
    password = UL_data.get("password") 
    cur_user = User.query.filter_by(user_email=email).first() 
    cur_user.last_login=datetime.now()
    db.session.commit() 
    if cur_user is None:
        return jsonify('User does not exist !!')
    if cur_user and sha256_crypt.verify(password,cur_user.password):
        Dict['cur_user']=cur_user
        print(Dict['cur_user'])
        return jsonify({'status': 'success', 'message': 'successfully logged in'})
    return jsonify('Invalid password')

@app.route('/logoutuser')
def userlogout():
    if 'cur_user' in Dict:
        #print(Dict['cur_user'])
        Dict.pop('cur_user', None)
    #session.pop('cur_user',None)
    return jsonify({'message': 'logged out successfully'})

@app.route('/stats', methods=['GET'])
def stats():
    if request.method == 'GET':
        # Visualization - 1
        sections = Section.query.all()
        section_names = [section.section_name for section in sections]
        num_books = [section.books.count() for section in sections]

        plt.figure(figsize=(5, 8))  # Create a new figure

        plt.subplot(2, 1, 1)  # Create the first subplot for visualization 1
        plt.bar(section_names, num_books)
        plt.xlabel('Section')
        plt.ylabel('Number of Books')
        plt.title('Number of Books in Each Section')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        plt.savefig('static/books_per_section.png')

        # Visualization - 2
        plt.figure(figsize=(5, 8))  # Create another new figure

        books = Book.query.all()
        book_names = [book.book_name for book in books]
        num_issues = [book.issues.filter_by(status='approved').count() for book in books]

        plt.subplot(2, 1, 2)  # Create the second subplot for visualization 2
        plt.bar(book_names, num_issues)
        plt.xlabel('Book')
        plt.ylabel('Number of Issues')
        plt.title('Number of Issues for Each Book')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        plt.savefig('static/issues_per_book.png')
        plt.close()

        # Construct URLs for the images
        books_per_section_url = url_for('static', filename='books_per_section.png')
        issues_per_book_url = url_for('static', filename='issues_per_book.png')

        # Return the URLs as JSON response
        return jsonify({
            'books_per_section_url': books_per_section_url,
            'issues_per_book_url': issues_per_book_url
        })


'''
scheduler = BackgroundScheduler()
try:
    #scheduler.add_job(send_scheduled_email, 'date', run_date=datetime.now())
    scheduler.add_job(send_scheduled_report_email, 'date', run_date=datetime.now())

    scheduler.start()
except Exception as e:
    print("An error occurred:", e)
finally:
    scheduler.shutdown(wait=False)
'''


if __name__ =="__main__":
    app.run(debug=True)     