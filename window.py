from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.title = self.__root
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    
    def close(self):
        self.running = False


def main():
    win = Window(800, 600)
    win.wait_for_close()


main()