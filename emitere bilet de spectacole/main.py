import tkinter as tk
from client import Client
from tkinter import messagebox
import sqlite3
from database import TicketsTabel
import pathlib
from pdf_genereator import generate_ticket_pdf
import logging

class MyGui:

#     This class represents a graphical user interface (GUI) for managing tickets in a theater.

# Attributes:
# -----------
# - ROOT : pathlib.Path
#     The root directory of the application.
# - DB_PATH : pathlib.Path
#     The path to the SQLite database file.
# - LOG_PATH : pathlib.Path
#     The path to the log file.

    ROOT = pathlib.Path(__file__).parent
    DB_PATH = ROOT / "issuing_tickets.db"
    LOG_PATH = ROOT / "log.log"
    

    def __init__(self) -> None:

        # Initializes the GUI window and sets up the main interface with buttons for various actions.
        
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.configure(bg="grey")

        self.label = tk.Label(self.root, text="Choose an option:", font=('Arial', 18), bg="grey", fg="black")
        self.label.pack(padx=10,pady=10)

        self.button1 = tk.Button(self.root, text="Reserve a ticket", command=self.buy_ticket, font=('Bold italic', 16), width=16, bg="grey")
        self.button1.pack(padx=10,pady=10)

        self.button2 = tk.Button(self.root, text="Show client info", command=self.show_client_info, font=('Bold italic', 16), width=16, bg="grey")
        self.button2.pack(padx=10,pady=10)

        self.button3 = tk.Button(self.root, text="Show me the shows", command=self.shows_view, font=('Bold italic', 16), width=16, bg="grey")
        self.button3.pack(padx=10,pady=10)

        self.button4 = tk.Button(self.root, text="Cancel a ticket", command=self.remove_ticket, font=('Bold italic', 16), width=16, bg="grey")
        self.button4.pack(padx=10,pady=10)


        self.root.mainloop()

    
    def buy_ticket(self):

        # Displays a window for reserving tickets. Handles the process of reserving a ticket, logging errors, and showing messages.

        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s >> %(levelname)-10s >> %(message)s", filename=self.LOG_PATH
        )
        
        tickets_table = TicketsTabel(self.DB_PATH)

        def reserve_ticket(email: tk.Entry, place: tk.Entry, name: tk.Entry, age: tk.Entry, show: tk.OptionMenu):

            # This function is responsible for reserving a ticket for a client based on the provided information.

# Parameters:
# -----------
# - email : tk.Entry
#     The entry field containing the client's email address.
# - place : tk.Entry
#     The entry field containing the desired seat number.
# - name : tk.Entry
#     The entry field containing the client's name.
# - age : tk.Entry
#     The entry field containing the client's age.
# - show : tk.OptionMenu
#     The dropdown menu containing the available shows.

# Returns:
# --------
# None

# Functionality:
# --------------
# 1. Retrieves the input values from the provided Tkinter entry fields and dropdown menu.
# 2. Validates the input fields to ensure they are not empty and that the seat number is within the valid range (1-30).
# 3. Attempts to convert the age entry to an integer to ensure it is a valid number.
# 4. Based on the selected show, creates the corresponding table in the database if it does not exist.
# 5. Attempts to create a ticket entry in the respective table for the provided client information.
# 6. Generates a PDF ticket for the reservation using the provided details.
# 7. Updates the database with the generated PDF file path for the reserved seat.
# 8. Displays appropriate error messages using Tkinter messagebox if any errors occur during the process.

            n_e = email.get()
            p_i = place.get()
            n_i = name.get()
            a_i = age.get()
            s_i = show.get()

            list_entries = [n_e, p_i, n_i, a_i, s_i]

            if "" not in list_entries:
                if int(p_i) <= 30 and int(p_i) > 0:

                    try:
                        a_i == int(a_i)

                        if s_i == "Romeo si Julieta":
                            tickets_table.create_table1()
                            try:
                                tickets_table.create_ticket1(p_i, s_i, Client(n_i, a_i, n_e))
                                pdf = generate_ticket_pdf(p_i, s_i, self.DB_PATH, n_i, a_i, n_e, "02.03.2024", "19.00", "30 RON")
                                tickets_table.update1(str(pdf), p_i)
                        

                            except sqlite3.IntegrityError as err:
                                messagebox.showerror("Error","This place is reserved!")

                        elif s_i == "Hamlet":
                            tickets_table.create_table2()
                            try:
                                tickets_table.create_ticket2(p_i, s_i, Client(n_i, a_i, n_e))
                                pdf = generate_ticket_pdf(p_i, s_i, self.DB_PATH, n_i, a_i, n_e, "04.03.2024", "20.00", "35 RON")
                                tickets_table.update2(str(pdf), p_i)
                            except sqlite3.IntegrityError as err:
                                messagebox.showerror("Error","This place is reserved!")

                        elif s_i == "The Lion King":
                            tickets_table.create_table3()
                            try:
                                tickets_table.create_ticket3(p_i, s_i, Client(n_i, a_i, n_e))
                                pdf = generate_ticket_pdf(p_i, s_i, self.DB_PATH, n_i, a_i, n_e, "06.03.2024", "21.00", "40 RON")
                                tickets_table.update1(str(pdf), p_i)
                            except sqlite3.IntegrityError as err:
                                messagebox.showerror("Error","This place is reserved!")
                    except ValueError as err:
                        logging.error("Put numbers in the entry with age!")
                        messagebox.showerror("Error","Put numbers in the entry with age!")

                else:
                    logging.warning("Exceed the number of seats(30)!")
                    messagebox.showinfo("Info", "Exceed the number of seats(30)!")

            else:
                logging.warning("Fill all the entries!")
                messagebox.showinfo("Error", "Fill all the entries!")    

        def show_tickets(show: tk.OptionMenu):

#             This function is responsible for displaying all tickets reserved for a specific show.

# Parameters:
# -----------
# - show : tk.OptionMenu
#     The dropdown menu containing the available shows.

# Returns:
# --------
# None

# Functionality:
# --------------
# 1. Retrieves the selected show from the provided Tkinter dropdown menu.
# 2. Depending on the selected show, creates the corresponding table in the database if it does not exist.
# 3. Retrieves all ticket information from the respective table in the database for the selected show.
# 4. Prints the retrieved ticket information to the console.

            s_i = show.get()
            if s_i == "Romeo si Julieta":
                tickets_table.create_table1()
                print(tickets_table.read_all1())

            elif s_i == "Hamlet":
                tickets_table.create_table2()
                print(tickets_table.read_all2())
            elif s_i == "The Lion King":
                tickets_table.create_table3()
                print(tickets_table.read_all3())


        def available_places(show: tk.OptionMenu, output_w: tk.Label):

#             This function calculates and displays the available places (seat numbers) for a specific show.

# Parameters:
# -----------
# - show : tk.OptionMenu
#     The dropdown menu containing the available shows.
# - output_w : tk.Label
#     The label widget where the list of available places will be displayed.

# Returns:
# --------
# None

# Functionality:
# --------------
# 1. Retrieves the selected show from the provided Tkinter dropdown menu.
# 2. Initializes an empty string to store the list of available places.
# 3. Creates a list of all possible place numbers (1 to 30).
# 4. Retrieves the list of occupied places from the corresponding table in the database for the selected show.
# 5. Iterates through all possible place numbers and checks if each place is not in the list of occupied places.
# 6. Concatenates the available place numbers to the `loc_dis` string.
# 7. Updates the text of the provided output label widget with the concatenated list of available places.


            s_i = show.get()
            loc_dis = ""
            all_places = list(range(1,31))
            occp_places = []
            
            if s_i == "Romeo si Julieta":
                tickets_table.create_table1()

                for tickets in tickets_table.read_all1():
                    occp_places.append(tickets[0])

                for loc in all_places:
                    if loc not in occp_places:
                        loc_dis = loc_dis + str(loc) + " | "
                    
                output_w["text"] = f"{loc_dis}"

            elif s_i == "Hamlet":
                tickets_table.create_table2()

                for tickets in tickets_table.read_all2():
                    occp_places.append(tickets[0])

                for loc in all_places:
                    if loc not in occp_places:
                        loc_dis = loc_dis + str(loc) + " | "
                    
                output_w["text"] = f"{loc_dis}"
            elif s_i == "The Lion King":
                tickets_table.create_table3()

                for tickets in tickets_table.read_all3():
                    occp_places.append(tickets[0])

                for loc in all_places:
                    if loc not in occp_places:
                        loc_dis = loc_dis + str(loc) + " | "
                    
                output_w["text"] = f"{loc_dis}"


        root = tk.Tk()
        root.title("Buy Ticket")
        root.geometry("450x450")
        root.configure(bg="grey")

        frm1 = tk.Frame(root, bg="grey")
        frm1.grid()
        frm1.columnconfigure(0, weight=1)
        frm1.columnconfigure(1, weight=1)

        label1 = tk.Label(frm1, text="Write your email:", font=('Arial', 18), bg="grey", fg="black")
        label1.grid(row=0, column=0)

        name_email = tk.Entry(frm1, font=('Arial', 18), bg="grey", fg="black", width=19)
        name_email.grid(row=0, column=1)


        label2 = tk.Label(frm1, text="Write your name:", font=('Arial', 18), bg="grey", fg="black")
        label2.grid(row=1, column=0)

        name_client = tk.Entry(frm1, font=('Arial', 18), bg="grey", fg="black", width=19)
        name_client.grid(row=1, column=1)


        label3 = tk.Label(frm1, text="Write your age:", font=('Arial', 18), bg="grey", fg="black")
        label3.grid(row=2, column=0)

        number_age = tk.Entry(frm1, font=('Arial', 18), bg="grey", fg="black", width=18)
        number_age.grid(row=2, column=1)


        label4 = tk.Label(frm1, text="Choose the place:", font=('Arial', 18), bg="grey", fg="black")
        label4.grid(row=3, column=0)

        number_place = tk.Entry(frm1, font=('Arial', 18), bg="grey", fg="black", width=19)
        number_place.grid(row=3, column=1)


        frm1.pack(fill='x')




        selected_option = tk.StringVar(root)
        selected_option.set("Romeo si Julieta")

        options = ["Romeo si Julieta", "Hamlet", "The Lion King"]

        option_menu = tk.OptionMenu(root, selected_option, *options)
        option_menu.pack(padx=10,pady=10)

        option_menu.config(bg="grey",fg="black", width=50)
        option_menu["menu"].config(bg="grey")






        button_append = tk.Button(root, text="Reserve ticket", command=lambda: reserve_ticket(name_email, number_place, name_client, number_age, selected_option),width=48 , bg="grey")
        button_append.pack(padx=10,pady=10)
        button_show = tk.Button(root, text="Show all tickets", command=lambda: show_tickets(selected_option) ,width=48 , bg="grey")
        button_show.pack(padx=10,pady=10)

        button_show_available_tickets = tk.Button(root, text="Show available tickets", command=lambda: available_places(selected_option, label4), width=48 , bg="grey")
        button_show_available_tickets.pack(padx=10,pady=10)
        label4 = tk.Label(root, text="Press previous button for available tickets", font=('Arial', 18), bg="grey", fg="black", wraplength=400)
        label4.pack(padx=10, pady=10)





    def show_client_info(self):

        #  Displays a window for showing client information. Handles the process of retrieving client details, logging errors, and showing messages.

        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s >> %(levelname)-10s >> %(message)s", filename=self.LOG_PATH
        )

        tickets_table = TicketsTabel(self.DB_PATH)

        def show_client_details(email: tk.Entry, show: tk.OptionMenu, output_w: tk.Label):

#             This function retrieves and displays client details based on the provided email and selected show.

# Parameters:
# -----------
# - email : tk.Entry
#     The entry widget containing the client's email.
# - show : tk.OptionMenu
#     The dropdown menu containing the available shows.
# - output_w : tk.Label
#     The label widget where the client details will be displayed.

# Returns:
# --------
# None

# Functionality:
# --------------
# 1. Retrieves the client's email and the selected show from the provided Tkinter entry and dropdown menu widgets, respectively.
# 2. Checks the selected show to determine which database table to query for client details.
# 3. Queries the corresponding table in the database to retrieve client details based on the provided email.
# 4. If client details are found, formats and displays the client's name and age on the output label widget.
# 5. If no client details are found (empty result set), displays an error message indicating that the client doesn't exist.
# 6. Handles potential exceptions such as database errors or cases where the user needs to reserve a ticket before viewing client details.


            n_e = email.get()
            s_i = show.get()

            if s_i == "Romeo si Julieta":
                tickets_table.create_table1()
                try:
                    a = tickets_table.read_by_email1(n_e)
                    for i in a:
                        output_w["text"] = f"Name: {i[3]} | Age: {i[2]}"
                    if a == []:
                        messagebox.showinfo("Error", "The client doesn't exist!") 
                        logging.error("The client doesn't exist!")
                except sqlite3.ProgrammingError as err:
                    messagebox.showinfo("Error", "You need to reserve a ticket!") 
                    logging.error("You need to reserve a ticket!")
                    
            elif s_i == "Hamlet":
                tickets_table.create_table2()
                try:
                    a = tickets_table.read_by_email2(n_e)
                    for i in a:
                        output_w["text"] = f"Name: {i[3]} | Age: {i[2]}"
                    if a == []:
                        messagebox.showinfo("Error", "The client doesn't exist!") 
                        logging.error("The client doesn't exist!")
                except sqlite3.ProgrammingError as err:
                    messagebox.showinfo("Error", "You need to reserve a ticket!")
                    logging.error("You need to reserve a ticket!") 

            elif s_i == "The Lion King":
                tickets_table.create_table3()
                try:
                    a = tickets_table.read_by_email3(n_e)
                    for i in a:
                        output_w["text"] = f"Name: {i[3]} | Age: {i[2]}"
                    if a == []:
                        messagebox.showinfo("Error", "The client doesn't exist!") 
                        logging.error("The client doesn't exist!")
                except sqlite3.ProgrammingError as err:
                    messagebox.showinfo("Error", "You need to reserve a ticket!") 
                    logging.error("You need to reserve a ticket!")

        root = tk.Tk()
        root.geometry("400x400")
        root.title("Showing tikets")
        root.configure(bg="grey")


        frm = tk.Frame(root, bg="grey")
        frm.grid()
        
        label1 = tk.Label(frm, text="Write your email:", font=('Arial', 18), bg="grey", fg="black")
        label1.grid(row=0, column=0)

        name_email = tk.Entry(frm, font=('Arial', 18), bg="grey", fg="black", width=19)
        name_email.grid(row=0, column=1)

        frm.pack(fill='x')



        selected_option = tk.StringVar(root)
        selected_option.set("Romeo si Julieta")

        options = ["Romeo si Julieta", "Hamlet", "The Lion King"]

        option_menu = tk.OptionMenu(root, selected_option, *options)
        option_menu.pack(padx=10,pady=10)

        option_menu.config(bg="grey",fg="black", width=50)
        option_menu["menu"].config(bg="grey")

        button = tk.Button(root, text="Show client info", command=lambda: show_client_details(name_email, selected_option, label2), font=('Bold italic', 16), width=16, bg="grey")
        button.pack(padx=10, pady=10)

        label2 = tk.Label(root, text="", font=('Arial', 18), bg="grey", fg="black")
        label2.pack(padx=10, pady=10)
        

    

    def shows_view(self):

        # Displays a window for showing details about available shows, including show name, date, time, price, and available places.

        tickets_table = TicketsTabel(self.DB_PATH)

        def available_places(show: tk.OptionMenu, output_w: tk.Label):

#             This function calculates and displays the number of available places for a selected show.

# Parameters:
# -----------
# - show : tk.OptionMenu
#     The dropdown menu containing the available shows.
# - output_w : tk.Label
#     The label widget where the available places information will be displayed.

# Returns:
# --------
# None

# Functionality:
# --------------
# 1. Retrieves the selected show from the provided Tkinter dropdown menu widget.
# 2. Initializes variables to store information about all available places, occupied places, and the count of available places.
# 3. Depending on the selected show, queries the corresponding table in the database to retrieve information about occupied places.
# 4. Calculates the number of available places by subtracting the count of occupied places from the total number of places.
# 5. Formats and displays the show details along with the calculated number of available places on the output label widget.


            s_i = show.get()
            loc_dis = ""
            all_places = list(range(1,31))
            occp_places = []
            k = 0
            
            if s_i == "Romeo si Julieta":
                tickets_table.create_table1()

                for tickets in tickets_table.read_all1():
                    occp_places.append(tickets[0])

                for loc in all_places:
                    if loc not in occp_places:
                        k = k + 1
                    
                output_w["text"] = f"Show: {s_i}| Date: 02.03.2024 | Time: 19.00 | Price: 30 RON | Available places: {k}"

            elif s_i == "Hamlet":
                tickets_table.create_table2()

                for tickets in tickets_table.read_all2():
                    occp_places.append(tickets[0])

                for loc in all_places:
                    if loc not in occp_places:
                        k = k + 1
                    
                output_w["text"] = f"Show: {s_i}| Date: 04.03.2024 | Time: 20.00 | Price: 35 RON | Available places: {k}"

            elif s_i == "The Lion King":
                tickets_table.create_table3()

                for tickets in tickets_table.read_all3():
                    occp_places.append(tickets[0])

                for loc in all_places:
                    if loc not in occp_places:
                        k = k + 1
                    
                output_w["text"] = f"Show: {s_i}| Date: 06.03.2024 | Time: 21.00 | Price: 40 RON | Available places: {k}"

        root = tk.Tk()
        root.geometry("1100x300")
        root.configure(bg="grey")

        selected_option = tk.StringVar(root)
        selected_option.set("Romeo si Julieta")

        options = ["Romeo si Julieta", "Hamlet", "The Lion King"]

        option_menu = tk.OptionMenu(root, selected_option, *options)
        option_menu.pack(padx=10,pady=10)

        option_menu.config(bg="grey",fg="black", width=50)
        option_menu["menu"].config(bg="grey")



        button = tk.Button(root, text="Show details about the selected show", command=lambda: available_places(selected_option, label_show), bg="grey")
        button.pack(padx=10,pady=10)

        label_show = tk.Label(root, text="", font=('Arial', 18), bg="grey", fg="black")
        label_show.pack(padx=10, pady=10)


    def remove_ticket(self):

        # Displays a window for canceling a ticket reservation. Handles the process of canceling a ticket, logging errors, and showing messages.

        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s >> %(levelname)-10s >> %(message)s", filename=self.LOG_PATH
        )

        def rem_tick(email: tk.Entry, show: tk.OptionMenu):

#             This function handles the cancellation process for a ticket reservation based on the provided email and selected show.

# Parameters:
# -----------
# - email : tk.Entry
#     An entry widget where the user inputs their email address.

# - show : tk.OptionMenu
#     An option menu widget allowing the user to select the show for which they want to cancel the ticket reservation.

# Returns:
# --------
# None

# Functionality:
# --------------
# 1. Retrieves the email address and selected show from the respective Tkinter entry and option menu widgets.
# 2. Based on the selected show, creates the corresponding table in the database and attempts to read the ticket reservation associated with the provided email.
# 3. If no ticket reservation is found for the given email and show, displays an informational message stating that the ticket is not reserved.
# 4. If a ticket reservation is found, deletes the reservation from the database and displays a message confirming that the ticket has been successfully canceled.
# 5. Logs relevant information using the logging module, such as successful ticket deletion or errors encountered during the cancellation process.


            n_e = email.get()
            s_i= show.get()

            if s_i == "Romeo si Julieta":
                tickets_table.create_table1()
                try:
                    a = tickets_table.read_by_email1(n_e)
                    if a == []:
                        messagebox.showinfo("Info", "The ticket is not reserved!")
                        logging.info("The ticket is not reserved!")   
                    else:
                        tickets_table.delete1(n_e)
                        messagebox.showinfo("Info", "The ticket is deleted!")
                        logging.info("The ticket is deleted!") 
                       
                except sqlite3.ProgrammingError as err:
                    messagebox.showinfo("Error", "You need to reserve a ticket!") 
                    logging.info("You need to reserve a ticket!") 

            elif s_i == "Hamlet":
                tickets_table.create_table2()
                try:
                    a = tickets_table.read_by_email2(n_e)
                    if a == []:
                        messagebox.showinfo("Info", "The ticket is not reserved!") 
                        logging.info("The ticket is not reserved!")  
                    else:
                        tickets_table.delete2(n_e)
                        messagebox.showinfo("Info", "The ticket is deleted!") 
                        logging.info("The ticket is deleted!") 
                       
                except sqlite3.ProgrammingError as err:
                    messagebox.showinfo("Error", "You need to reserve a ticket!")
                    logging.info("You need to reserve a ticket!")  

            elif s_i == "The Lion King":
                tickets_table.create_table3()
                try:
                    a = tickets_table.read_by_email3(n_e)
                    if a == []:
                        messagebox.showinfo("Info", "The ticket is not reserved!")  
                        logging.info("The ticket is not reserved!") 
                    else:
                        tickets_table.delete3(n_e)
                        messagebox.showinfo("Info", "The ticket is deleted!") 
                        logging.info("The ticket is deleted!") 
                       
                except sqlite3.ProgrammingError as err:
                    messagebox.showinfo("Error", "You need to reserve a ticket!")
                    logging.info("You need to reserve a ticket!")  
        
        root = tk.Tk()
        root.geometry("500x500")
        root.configure(bg="grey")

        tickets_table = TicketsTabel(self.DB_PATH)
            

        frm1 = tk.Frame(root, bg="grey")
        frm1.grid()
        frm1.columnconfigure(0, weight=1)
        frm1.columnconfigure(1, weight=1)

        label1 = tk.Label(frm1, text="Enter your email:", font=('Arial', 18), bg="grey", fg="black")
        label1.grid(row=0, column=0)


        nume_email = tk.Entry(frm1, font=('Arial', 18), bg="grey", fg="black", width=19)
        nume_email.grid(row=0, column=1)

        frm1.pack(fill='x')



        selected_option = tk.StringVar(root)
        selected_option.set("Romeo si Julieta")

        options = ["Romeo si Julieta", "Hamlet", "The Lion King"]

        option_menu = tk.OptionMenu(root, selected_option, *options)
        option_menu.pack(padx=10,pady=10)

        option_menu.config(bg="grey",fg="black", width=50)
        option_menu["menu"].config(bg="grey")



        button1 = tk.Button(root, text="Press to delete", command=lambda: rem_tick(nume_email, selected_option), font=('Arial', 18), bg="grey", fg="black", width=30)
        button1.pack(padx=10, pady=10)



        


        



MyGui()