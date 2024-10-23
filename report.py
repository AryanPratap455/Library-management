from flask import Flask, render_template, make_response
import pdfkit
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/generate_report')
def generate_report():
    # Render your HTML template (you can pass any necessary data)
    html = render_template('report_template.html')

    # Convert HTML to PDF using pdfkit
    pdf = pdfkit.from_string(html, False, configuration=pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'))

    # Create a response containing the PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=report.pdf'
    print(response)
    return response
