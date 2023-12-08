import tkinter
from csvFunctions import *


class voteGUI:
    
    def __init__(self, window):
        """
        Initializes the GUI by creating the main window.
        User should have the choice to either vote or view current results.
        """
        
        
        self.window = window
    
        self.header_label = tkinter.Label(window, text = "What would you like to do?")
        self.header_label.pack()

        self.Vote_Button = tkinter.Button(window, text = "Vote", command = self.vb_clicked, width = 10, height = 5, bg = "white")
        self.Vote_Button.pack()
        self.Results_Button = tkinter.Button(window, text = "View Results", command = self.rb_clicked, width = 10, height = 5, bg = "white")
        self.Results_Button.pack()
        
    def vb_clicked(self):
        """
        This function should be called when Vote_Button is pressed.
        
        The window should change and create an entry box for the user to enter their name.
        A submit button is created beneath this entry box.
        """
        self.header_label.config(text = "Please Enter Your First and Last Name")
        self.Vote_Button.pack_forget()
        self.Results_Button.pack_forget()
        
        self.Name_Entry = tkinter.Entry(self.window, width = 30)
        self.Name_Entry.pack()
        self.Submit_Name_Button = tkinter.Button(self.window, text = "Submit", command = self.submit_clicked, width = 10, height = 1,)
        self.Submit_Name_Button.pack()
        
        
    
    def submit_clicked(self):
        """
        This function should be called when Submit_Name_Button is pressed.
        
        Upon being called, the entry in the box should be stored.
        If this value is empty, the message "Please Enter Name"
        
        If the name is among those who can vote and have not already voted, they will be taken to the vote screen
        If they cannot vote, an error message is displayed.
        """
        name = self.Name_Entry.get()
        if name == "":
            try:
                self.error_label.config(text = "Please Enter Name.")
            except AttributeError:
                self.error_label = tkinter.Label(self.window, text = "Please Enter Name.")
                self.error_label.pack()
        elif allowed_to_vote(name) == True:
            just_voted(self.Name_Entry.get())
            self.header_label.config(text = "Who would you like to vote for?")
            self.Name_Entry.pack_forget()
            self.Submit_Name_Button.pack_forget()
            
            try:
                self.error_label.pack_forget()
            except:
                pass
            
            self.John_Button = tkinter.Button(self.window, text = "John", command = self.john_clicked, width = 10, height = 5, bg = "green")
            self.John_Button.pack()
            self.Jane_Button = tkinter.Button(self.window, text = "Jane", command = self.jane_clicked, width = 10, height = 5, bg = "orange")
            self.Jane_Button.pack()
            
        else:
            try:
                self.error_label.config(text = "Name Ineligible To Vote. Check Spelling and Capitalizaton.")
            except AttributeError:
                self.error_label = tkinter.Label(self.window, text = "Name Ineligible To Vote. Check Spelling and Capitalizaton.")
                self.error_label.pack()
    
    def rb_clicked(self):
        """
        This function should be called when Results_Button is pressed.
        
        Upon being called, all buttons should be removed and the vote count for both John and Jane should be displayed
        """
        self.header_label.config(text = "Current Voting Results")
        self.Vote_Button.pack_forget()
        self.Results_Button.pack_forget()
        
        john_votes = count_votes()[0]
        jane_votes = count_votes()[1]
        if john_votes == 1:
            self.john_label = tkinter.Label(self.window, text = "John has 1 vote")
        else:
            self.john_label = tkinter.Label(self.window, text = f"John has {john_votes} votes")
        if jane_votes == 1:
            self.jane_label = tkinter.Label(self.window, text = "Jane has 1 vote")
        else:
            self.jane_label = tkinter.Label(self.window, text = f"Jane has {jane_votes} votes")
        self.john_label.pack()
        self.jane_label.pack()
        
        
    def john_clicked(self):
        """
        This function should be called when John_Button is pressed.
        
        Upon being called, the user should be returned to the orignial screen with the thank you for voting message.
        """
        
        john_voted()
        
        self.header_label.config(text = "Thank you for voting. What would you like to do next?")
        self.header_label.pack()

        self.John_Button.pack_forget()
        self.Jane_Button.pack_forget()
        
        self.Vote_Button = tkinter.Button(self.window, text = "Vote", command = self.vb_clicked, width = 10, height = 5, bg = "white")
        self.Vote_Button.pack()
        self.Results_Button = tkinter.Button(self.window, text = "View Results", command = self.rb_clicked, width = 10, height = 5, bg = "white")
        self.Results_Button.pack()
        
        
        
    def jane_clicked(self):
        """
        This function should be called when Jane_Button is pressed.
        
        Upon being called, the user should be returned to the orignial screen with the thank you for voting message.
        """
        jane_voted()
        
        self.header_label.config(text = "Thank you for voting. What would you like to do next?")
        self.header_label.pack()
        
        self.John_Button.pack_forget()
        self.Jane_Button.pack_forget()

        self.Vote_Button = tkinter.Button(self.window, text = "Vote", command = self.vb_clicked, width = 10, height = 5, bg = "white")
        self.Vote_Button.pack()
        self.Results_Button = tkinter.Button(self.window, text = "View Results", command = self.rb_clicked, width = 10, height = 5, bg = "white")
        self.Results_Button.pack()
        
        
        