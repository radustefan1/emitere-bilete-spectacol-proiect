from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
import string
import pathlib

ROOT = pathlib.Path(__file__).parent
DB_PATH = ROOT / "ticket.pdf"

def generate_ticket_pdf(place, show, db_path, name, age, email, date, time, price):
    # Generate a random 8-digit ticket number
    ticket_number = ''.join(random.choices(string.digits, k=8))

    # Create PDF
    c = canvas.Canvas(str(DB_PATH), pagesize=letter)

    # Set up the content
    content = [
        f"Email: {email}",
        f"Name: {name}",
        f"Age: {age}",
        f"Show: {show}",
        f"Date: {date}",
        f"Time: {time}",
        f"Price: {price}",
        f"Place: {place}",
        f"Ticket Number: {ticket_number}"
    ]


    y_position = 750
    for line in content:
        c.drawString(100, y_position, line)
        y_position -= 20

    
    c.save()

    print(f"Ticket PDF generated: {DB_PATH}")
    return ticket_number

