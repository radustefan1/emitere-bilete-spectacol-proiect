class Client():
    
#     This class represents a client with basic information such as name, age, and email.

# Attributes:
# -----------
# - name : str
#     The name of the client.
# - age : int
#     The age of the client.
# - email : str
#     The email address of the client.

    def __init__(self, name, age, email) -> None:

    #     Initializes a new `Client` object with the specified name, age, and email.

    # Parameters:
    # - name : str
    #     The name of the client.
    # - age : int
    #     The age of the client.
    # - email : str
    #     The email address of the client.

        self.name = name
        self.age = age
        self.email = email
