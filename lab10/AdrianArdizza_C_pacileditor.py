from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

# TODO: Lengkapi class Application dibawah ini
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()
        self.create_buttons()
        self.create_editor()

    def initUI(self):
        # TODO: Atur judul dan ukuran dari main window,
        # lalu buat sebuah Frame sebagai anchor dari seluruh button
        self.master.title('Pacil Editor')
        self.master.geometry('800x600')
        self.ButtonFrame = Frame(self.master)
        self.ButtonFrame.pack(side=TOP, fill='x', expand=FALSE)

    def create_buttons(self):
        # TODO: Implementasikan semua button yang dibutuhkan
        self.OpenButton = Button(self.ButtonFrame, text='Open File', command=self.load_file)
        self.SaveButton = Button(self.ButtonFrame, text='Save File', command=self.save_file)
        self.QuitButton = Button(self.ButtonFrame, text='Quit Program', command=self.master.destroy)
        self.OpenButton.pack(side=LEFT, padx=5, pady=5)
        self.SaveButton.pack(side=LEFT, padx=5, pady=5)
        self.QuitButton.pack(side=LEFT, padx=5, pady=5)


    def create_editor(self):
        # TODO: Implementasikan textbox
        self.edit = Text(self.master)
        self.master.bind("<Control-s>", self.save_file_event)
        self.master.bind("<Control-o>", self.load_file_event)
        self.edit.pack(expand=TRUE, fill="both")

    def load_file_event(self, event):
        self.load_file()

    def load_file(self):
        file_name = askopenfilename(
            filetypes=[("All files", "*")]
        )
        if not file_name:  # Jika pengguna membatalkan dialog, langsung return
            return
        text_file = open(file_name, 'r', encoding="utf-8")
        result = text_file.read()
        self.set_text(result)

    def save_file_event(self, event):
        self.save_file()

    def save_file(self):
        file_name = asksaveasfilename(
            filetypes=[("All files", "*")]
        )
        if not file_name:  # Jika pengguna membatalkan dialog, langsung return
            return
        # TODO: ambil isi dari textbox lalu simpan dalam file dengan nama file_name
        with open(file_name, 'w') as file:
            file.write(self.get_text())
        

    def set_text(self, text=''):
        self.edit.delete('1.0', END)
        self.edit.insert('1.0', text)
        self.edit.mark_set(INSERT, '1.0')
        self.edit.focus()

    def get_text(self):
        return self.edit.get('1.0', END+'-1c')


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
