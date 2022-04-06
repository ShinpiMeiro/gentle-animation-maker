import tkinter as tk
#TODO  this code must be replaced with JScript code
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack(anchor="s", side="bottom")

        self.contents = tk.StringVar()

        self.contents.set("this is a variable")

        self.entrythingy["textvariable"] = self.contents

        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("320x600")
    myapp = App(root)
    myapp.mainloop()
