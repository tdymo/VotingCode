import tkinter

class voteGUI:
    global john_votes
    global jane_votes
    john_votes = 0
    jane_votes = 0
    def __init__(self, window):
        self.window = window
    
        self.header_label = tkinter.Label(window, text = "What would you like to do?")
        self.header_label.pack()

        self.Vote_Button = tkinter.Button(window, text = "Vote", command = self.vb_clicked, width = 10, height = 5, bg = "white")
        self.Vote_Button.pack()
        self.Results_Button = tkinter.Button(window, text = "View Results", command = self.rb_clicked, width = 10, height = 5, bg = "white")
        self.Results_Button.pack()
        
    def vb_clicked(self):
        self.header_label.config(text = "Who would you like to vote for?")
        self.Vote_Button.pack_forget()
        self.Results_Button.pack_forget()
        
        self.John_Button = tkinter.Button(self.window, text = "John", command = self.john_clicked, width = 10, height = 5, bg = "green")
        self.John_Button.pack()
        self.Jane_Button = tkinter.Button(self.window, text = "Jane", command = self.jane_clicked, width = 10, height = 5, bg = "orange")
        self.Jane_Button.pack()
        
    def rb_clicked(self):
        self.header_label.config(text = "Current Voting Results")
        self.Vote_Button.pack_forget()
        self.Results_Button.pack_forget()
        
        if john_votes == 1:
            self.john_label = tkinter.Label(self.window, text = f"John has 1 vote")
        else:
            self.john_label = tkinter.Label(self.window, text = f"John has {john_votes} votes")
        if jane_votes == 1:
            self.jane_label = tkinter.Label(self.window, text = f"Jane has 1 vote")
        else:
            self.jane_label = tkinter.Label(self.window, text = f"Jane has {jane_votes} votes")
        self.john_label.pack()
        self.jane_label.pack()
        
        
    def john_clicked(self):
        global john_votes
        john_votes += 1
        
        self.header_label.config(text = "You voted for John. What would you like to do next?")
        self.header_label.pack()

        self.John_Button.pack_forget()
        self.Jane_Button.pack_forget()
        
        self.Vote_Button = tkinter.Button(self.window, text = "Vote", command = self.vb_clicked, width = 10, height = 5, bg = "white")
        self.Vote_Button.pack()
        self.Results_Button = tkinter.Button(self.window, text = "View Results", command = self.rb_clicked, width = 10, height = 5, bg = "white")
        self.Results_Button.pack()
        
        
        
    def jane_clicked(self):
        global jane_votes
        jane_votes += 1
        
        self.header_label.config(text = "You voted for Jane. What would you like to do next?")
        self.header_label.pack()
        
        self.John_Button.pack_forget()
        self.Jane_Button.pack_forget()

        self.Vote_Button = tkinter.Button(self.window, text = "Vote", command = self.vb_clicked, width = 10, height = 5, bg = "white")
        self.Vote_Button.pack()
        self.Results_Button = tkinter.Button(self.window, text = "View Results", command = self.rb_clicked, width = 10, height = 5, bg = "white")
        self.Results_Button.pack()
        
        
        