import tkinter as tk
from app import App

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Birds Sounds to Images App")
        self.master.geometry("400x300")
        self.configure_gui(bg="white")
        self.create_widgets()

    def configure_gui(self, bg):
        self.master.configure(bg=bg)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
    
    def create_widgets(self):
        self.run_button = tk.Button(self.master, text="Run App", command=self.run_app)
        self.run_button.pack(pady=20)
    
    def run_app(self):
        app = App()
        app.run()
    
    def run(self):
        self.master.mainloop()

def main():
    root = tk.Tk()
    app = Application(root)
    app.run()

if __name__ == '__main__':
    main()