from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
import string
import pathlib

ROOT = pathlib.Path(__file__).parent
DB_PATH = ROOT / "ticket.pdf"

def generate_ticket_pdf(place, show, db_path, name, age, email, date, time, price):

    #     This function generates a PDF ticket for a show reservation based on the provided details.

# Parameters:
# -----------
# - place : int
#     The place of the ticket holder.

# - show : str
#     The name of the show for which the ticket is being generated.

# - db_path : str
#     The path to the database .

# - name : str
#     The name of the ticket holder.

# - age : int
#     The age of the ticket holder.

# - email : str
#     The email address of the ticket holder.

# - date : str
#     The date of the show.

# - time : str
#     The time of the show.

# - price : str
#     The price of the ticket.

# Returns:
# --------
# - ticket_number : str
#     A unique ticket number generated for the ticket.

# Functionality:
# --------------
# 1. Generates a unique ticket number consisting of 8 random digits.
# 2. Initializes a canvas for PDF generation using the `canvas.Canvas` function from the `reportlab` library.
# 3. Constructs the content of the ticket, including details such as email, name, age, show, date, time, price, place, and the generated ticket number.
# 4. Draws each line of content on the PDF canvas with appropriate positioning.
# 5. Saves the generated PDF with a filename specified by `DB_PATH`, although `DB_PATH` is not used in the function.
# 6. Prints a message indicating that the ticket PDF has been generated along with the path where it's saved.
# 7. Returns the generated ticket number.

    
    ticket_number = ''.join(random.choices(string.digits, k=8))

    
    c = canvas.Canvas(str(DB_PATH), pagesize=letter)

    
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

