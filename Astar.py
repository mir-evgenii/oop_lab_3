from Node import Node

class Astar:

    def __init__(self, maze, start, end):

        # Инициалицация начальной и конечной точки
        self.start_node = Node(None, start)
        self.start_node.g = self.start_node.h = self.start_node.f = 0
        self.end_node = Node(None, end)
        self.end_node.g = self.end_node.h = self.end_node.f = 0

        self.maze = maze

        # Инициализация списков открытых и закрытых точек
        self.open_list = []
        self.closed_list = []

        # Записываем стартовую точку
        self.open_list.append(self.start_node)


    def find(self):
        """
        Функция поиска пути
        Возвращяет кортеж точек от начальной точки до конечной
        """

        maze = self.maze

        # Выполняется до тех пор пока не найдет конечную точку
        while len(self.open_list) > 0:

            # Get the current node
            current_node = self.open_list[0]
            current_index = 0
            for index, item in enumerate(self.open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            self.open_list.pop(current_index)
            self.closed_list.append(current_node)

            # Found the goal
            if current_node == self.end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1] # Return reversed path

            # Generate children
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue

                # Make sure walkable terrain
                if maze[node_position[0]][node_position[1]] != 0:
                    continue

                # Create new node
                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in self.closed_list:
                    if child == closed_child:
                        continue

                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = ((child.position[0] - self.end_node.position[0]) ** 2) + ((child.position[1] - self.end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in self.open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                self.open_list.append(child)


