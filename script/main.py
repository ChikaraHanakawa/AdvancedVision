import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageTk
from app import App

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Birds Sounds to Images App")
        self.master.geometry("800x500")
        self.file_path = None
        self.configure_gui(bg="white")
        self.create_widgets()

    def configure_gui(self, bg):
        self.master.configure(bg=bg)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
    
    def create_widgets(self):
        self.label = tk.Label(self.master, text="Select a sound file", bg="white")
        self.label.pack(pady=10)
        
        self.button = tk.Button(self.master, text="Browse", command=self.open_file)
        self.button.pack(pady=10)
        
        self.file_label = tk.Label(self.master, text="", bg="white")
        self.file_label.pack(pady=10)
        
        self.run_button = tk.Button(self.master, text="Run App", command=self.run_app)
        self.run_button.pack(pady=10)

        self.message = tk.Message(self.master, text="Images of results from bird song estimation, found mainly in tropical and subtropical regions of Central and South America and Australia", font=("", 20), bg="blue")
        self.message.pack(pady=10)
    
    def open_file(self):
        self.file_path = fd.askopenfilename()
        self.file_label.config(text=self.file_path)
        print(self.file_path)
    
    def image_frame(self):
        self.image_frame = tk.Frame(self.master)
        self.image_frame.pack(pady=20)
        canvas = tk.Canvas(self.image_frame, width=300, height=300)
        canvas.pack()
        img = Image.open('data/serch_bird.jpg')
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_img)
    
    def run_app(self):
        if self.file_path:
            app = App(self.file_path)
            app.run()
            self.message.destroy()
            self.image_frame()
        else:
            print("No file selected")
    
    def run(self):
        self.master.mainloop()

def main():
    root = tk.Tk()
    app = Application(root)
    app.run()

if __name__ == '__main__':
    main()