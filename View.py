from tkinter import Tk, Canvas

class View:
    def init(self):
        self.root = Tk() # Creation fenetre principale
        self.root.title("S.M.A.")
        self.canvas = Canvas(self.root, background="white")
        self.canvas.create_oval((10,10),(20,20), width=1, fill="black")
        self.canvas.grid()
        self.root.mainloop() # Lancement boucle principale

if __name__ == "__main__":
    view = View()
    view.init()