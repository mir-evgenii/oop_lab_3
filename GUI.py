from tkinter import *
from Astar import Astar

class GUI:

    def __init__(self, maze):

        self.start_node = 0
        self.end_node = 0

        self.frame_list = []

        self.root = Tk()

        self.maze = maze
        #maze = self.show_res_in_maze(maze, res)

        self.maze_print(maze)

        self.root.mainloop()

    def maze_print(self, maze):

        b = 0
        for list in maze:
            frame = Frame(self.root)
            self.frame_list.append(frame)
            for i in list:
                b = b + 1
                but = Button(frame, command=lambda c=str(b): self.init_node(c), activebackground="red")
                but["text"] = i
                but.bind("<Button-1>")
                but.pack(side=LEFT)
            frame.pack()


    def show_res_in_maze(self, maze, res):

        for node in res:
            maze[node[0]][node[1]] = '3'

        return maze

    def init_node(self, i):
        if (self.start_node == 0):
            self.start_node = self.node_init_from_num(i)
            print(self.start_node)
        else:
            self.end_node =  self.node_init_from_num(i)
            print(self.end_node)
            self.find_path()

    def node_init_from_num(self, i):
        if (int(i) > 10):
            x = str(i)[0]
            y = str(i)[1]
            return (int(x), int(y)-1)
        else:
            return (0, int(i)-1)


    def find_path(self):

        path = Astar(self.maze, self.start_node, self.end_node)
        res = path.find()
        maze = self.show_res_in_maze(self.maze, res)

        for frame in self.frame_list:
            frame.destroy()

        self.maze_print(maze)


