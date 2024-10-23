from flask import Flask, render_template
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import pdfkit
from lib_database import db, User, Librarian, Section, Issue, Book

def create_app():
    app = Flask(__name__)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'bobymaurya455@gmail.com'
    app.config['MAIL_PASSWORD'] = 'kwydetxwzgqofqru'
    app.config['MAIL_DEFAULT_SENDER'] = 'bobymaurya455@gmail.com'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lib_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    mail = Mail(app)
    
    return app, mail

app, mail = create_app()

def send_scheduled_email():
    try:
        with app.app_context():
            
            current_time = datetime.now()
            time_threshold = current_time - timedelta(hours=24)
            users = User.query.filter(User.last_login < time_threshold).all()
            
            for user in users:
                msg = Message('Scheduled Email', recipients=[user.user_email])
                msg.body = "Hey !! " + user.user_email + ", \nYou have not visited the app today.\n Please visit the app.\n Thanking You " + str(datetime.now())
                mail.send(msg)
                print("Email has sent")
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False


def send_scheduled_report_email():
    try:
        with app.app_context():
            users = User.query.all()
            for user in users:
                # Get approved and pending issues for the user
                approved_issues_count = Issue.query.filter_by(user_id=user.user_id, status='Approved').count()
                pending_issues_count = Issue.query.filter_by(user_id=user.user_id, status='Pending').count()

                # Generate HTML content for the report
                html = render_template('report_template.html', user=user, approved_count=approved_issues_count, pending_count=pending_issues_count)

                # Convert HTML content to PDF
                pdf_content = pdfkit.from_string(html, False, configuration=pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'))

                # Create email message
                msg = Message('Monthly Report', recipients=[user.user_email])
                msg.body = "This is a monthly report sent at " + str(datetime.now())

                # Attach PDF content to email
                msg.attach("monthly_report.pdf", "application/pdf", pdf_content)

                # Send email
                mail.send(msg)
                print("Monthly report email has been sent to", user.user_email)

        return True
    except Exception as e:
        print("Error sending email:", e)
        return False

'''
scheduler = BackgroundScheduler()
scheduler.add_job(send_scheduled_email, 'date', run_date=datetime.now())
scheduler.start()
scheduler.shutdown(wait=False)
'''