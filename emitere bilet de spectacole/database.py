import sqlite3
import pathlib
from client import Client

class TicketsTabel:

# This class represents a database table for storing ticket information related to different shows.

# Attributes:
# -----------
# - con : sqlite3.Connection
#     A connection object representing the connection to the SQLite database.

    def __init__(self, db) -> None:
        # Initializes the `TicketsTable` object with a connection to the specified SQLite database.

        # Parameters:
        # - db : str
        #     The path to the SQLite database file.
        self.con = sqlite3.connect(db)

    def create_table1(self):
        # Creates the table "show__1" in the database if it doesn't already exist.
        cursor = self.con.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS show__1 (
            "nr_loc"	INTEGER NOT NULL PRIMARY KEY UNIQUE,
            "show"  TEXT NOT NULL,
            "name"	TEXT NOT NULL,
            "age"   INTEGER NOT NULL,
            "email"	TEXT NOT NULL,
            "ticket_number" TEXT
            )"""
        )
    
    def create_table2(self):
        # Creates the table "show__2" in the database if it doesn't already exist.
        cursor = self.con.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS show__2 (
            "nr_loc"	INTEGER NOT NULL PRIMARY KEY UNIQUE,
            "show"  TEXT NOT NULL,
            "name"	TEXT NOT NULL,
            "age"   INTEGER NOT NULL,
            "email"	TEXT NOT NULL,
            "ticket_number" TEXT
            )"""
        )

    def create_table3(self):
        # Creates the table "show__3" in the database if it doesn't already exist.
        cursor = self.con.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS show__3 (
            "nr_loc"	INTEGER NOT NULL PRIMARY KEY UNIQUE,
            "show"  TEXT NOT NULL,
            "name"	TEXT NOT NULL,
            "age"   INTEGER NOT NULL,
            "email"	TEXT NOT NULL,
            "ticket_number" TEXT
            )"""
        )


# *************************************************************************


    def create_ticket1(self, loc, show_name, client: Client):

        # Creates a ticket entry in "show__1" table.

    # Parameters:
    # - loc : int
    #     The location number of the ticket.
    # - show_name : str
    #     The name of the show.
    # - client : Client
    #     An object representing the client information.


        cursor = self.con.cursor()
        cursor.execute(
            """INSERT INTO show__1 (nr_loc, show, name, age, email)
            VALUES(?, ? ,?, ?, ?);""",
            (loc, show_name, client.name, client.age, client.email)
        )
        self.con.commit()

    def create_ticket2(self, loc, show_name, client: Client):

    #     Creates a ticket entry in "show__2" table.

    # Parameters:
    # - loc : int
    #     The location number of the ticket.
    # - show_name : str
    #     The name of the show.
    # - client : Client
    #     An object representing the client information.

        cursor = self.con.cursor()
        cursor.execute(
            """INSERT INTO show__2 (nr_loc, show, name, age, email)
            VALUES(?, ? ,?, ?, ?);""",
            (loc, show_name, client.name, client.age, client.email)
        )
        self.con.commit()

    def create_ticket3(self, loc, show_name, client: Client):

    #     Creates a ticket entry in "show__3" table.

    # Parameters:
    # - loc : int
    #     The location number of the ticket.
    # - show_name : str
    #     The name of the show.
    # - client : Client
    #     An object representing the client information.

        cursor = self.con.cursor()
        cursor.execute(
            """INSERT INTO show__3 (nr_loc, show, name, age, email)
            VALUES(?, ? ,?, ?, ?);""",
            (loc, show_name, client.name, client.age, client.email)
        )
        self.con.commit()


# *************************************************************************


    def read_all1(self):

    #     Reads all ticket entries from "show__1" table.

    # Returns:
    # - list
    #     A list of tuples representing the ticket entries.

        cursor = self.con.cursor()
        cursor.execute("""SELECT * FROM show__1;""")
        return cursor.fetchall()
    
    def read_all2(self):

    #     Reads all ticket entries from "show__2" table.

    # Returns:
    # - list
    #     A list of tuples representing the ticket entries.

        cursor = self.con.cursor()
        cursor.execute("""SELECT * FROM show__2;""")
        return cursor.fetchall()
    
    def read_all3(self):

    #     Reads all ticket entries from "show__3" table.

    # Returns:
    # - list
    #     A list of tuples representing the ticket entries.

        cursor = self.con.cursor()
        cursor.execute("""SELECT * FROM show__3;""")
        return cursor.fetchall()
    

# *************************************************************************


    def read_by_email1(self, email):

    #     Reads ticket entries from "show__1" table based on email.

    # Parameters:
    # - email : str
    #     The email address to search for.

    # Returns:
    # - list
    #     A list of tuples representing the ticket entries matching the email.

        cursor = self.con.cursor()
        cursor.execute("""SELECT * FROM show__1 WHERE email LIKE ?""", (email,))
        return cursor.fetchall()
    
    def read_by_email2(self, email):

# Reads ticket entries from "show__2" table based on email.

#     Parameters:
#     - email : str
#         The email address to search for.

#     Returns:
#     - list
#         A list of tuples representing the ticket entries matching the email.

        cursor = self.con.cursor()
        cursor.execute("""SELECT * FROM show__2 WHERE email LIKE ?""", (email,))
        return cursor.fetchall()
    
    def read_by_email3(self, email):

    #     Reads ticket entries from "show__3" table based on email.

    # Parameters:
    # - email : str
    #     The email address to search for.

    # Returns:
    # - list
    #     A list of tuples representing the ticket entries matching the email.

        cursor = self.con.cursor()
        cursor.execute("""SELECT * FROM show__3 WHERE email LIKE ?""", (email,))
        return cursor.fetchall()


# *************************************************************************


    def update1(self, ticket_number, place):

    #     Updates the ticket number in "show__1" table.

    # Parameters:
    # - ticket_number : str
    #     The ticket number to update.
    # - place : int
    #     The location number of the ticket to update.

        cursor = self.con.cursor()
        cursor.execute(
            """UPDATE show__1
                SET ticket_number = ?
                WHERE
                nr_loc == ?""",
                (ticket_number, place)
        )
        self.con.commit()


    def update2(self, ticket_number, place):

    #     Updates the ticket number in "show__2" table.

    # Parameters:
    # - ticket_number : str
    #     The ticket number to update.
    # - place : int
    #     The location number of the ticket to update.

        cursor = self.con.cursor()
        cursor.execute(
            """UPDATE show__2
                SET ticket_number = ?
                WHERE
                nr_loc == ?""",
                (ticket_number, place)
        )
        self.con.commit()


    def update3(self, ticket_number, place):

    #     Updates the ticket number in "show__3
    #     " table.

    # Parameters:
    # - ticket_number : str
    #     The ticket number to update.
    # - place : int
    #     The location number of the ticket to update.

        cursor = self.con.cursor()
        cursor.execute(
            """UPDATE show__3
                SET ticket_number = ?
                WHERE
                nr_loc == ?""",
                (ticket_number, place)
        )
        self.con.commit()


# *************************************************************************


    def delete1(self, email):

    #     Deletes ticket entries from "show__1" table based on email.

    # Parameters:
    # - email : str
    #     The email address to delete.

        cursor = self.con.cursor()
        cursor.execute("DELETE FROM show__1 WHERE email == ?", (email,))
        self.con.commit()

    def delete2(self, email):

    #     Deletes ticket entries from "show__2" table based on email.

    # Parameters:
    # - email : str
    #     The email address to delete.

        cursor = self.con.cursor()
        cursor.execute("DELETE FROM show__2 WHERE email == ?", (email,))
        self.con.commit()

    def delete3(self, email):

    #     Deletes ticket entries from "show__3" table based on email.

    # Parameters:
    # - email : str
    #     The email address to delete.
        
        cursor = self.con.cursor()
        cursor.execute("DELETE FROM show__3 WHERE email == ?", (email,))
        self.con.commit()



