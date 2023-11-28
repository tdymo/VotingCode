from voteGUI import *

def main():
    window = tkinter.Tk()
    window.geometry('300x300')
    window.title("Vote Menu")
    window.resizable(False, False)
    
    voteGUI(window)
    window.mainloop()



if __name__ == "__main__":
    main()