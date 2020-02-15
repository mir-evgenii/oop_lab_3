from tkinter import *

class GUI:

    def __init__(self, maze, res):

        self.root = Tk()

        maze = self.show_res_in_maze(maze, res)

        self.maze(maze)

        self.root.mainloop()

    def maze(self, maze):

        for list in maze:
            frame = Frame(self.root)
            for i in list:
                but = Button(frame)
                but["text"] = i
                but.pack(side=LEFT)
            frame.pack()

    def show_res_in_maze(self, maze, res):

        for node in res:
            maze[node[0]][node[1]] = '3'

        return maze




