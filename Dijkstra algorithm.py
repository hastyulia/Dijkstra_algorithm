class Net:
    def __init__(self):
        self.end = -1
        self.start = -1
        self.count = -1
        self.path = []
        self.previous = []
        self.nodes_list = []

    def read_net(self):
        with open('in.txt') as input_file:
            self.count = int(input_file.readline())
            for row in range(self.count):
                self.nodes_list.append([])
                line = input_file.readline().split()
                for i in range(0, len(line) - 1, 2):
                    node = int(line[i]) - 1, int(line[i + 1])
                    self.nodes_list[row].append(node)
            self.start = int(input_file.readline()) - 1
            self.end = int(input_file.readline()) - 1

    def find_way(self):
        self.path = [float('inf') for _ in range(self.count)]
        visited = [False for _ in range(self.count)]
        self.previous = [-1 for _ in range(self.count)]
        self.path[self.start] = 1
        for i in range(self.count):
            vertex = -1
            for j in range(self.count):
                if (not visited[j]) and (vertex == -1 or self.path[j] < self.path[vertex]):
                    vertex = j
            if self.path[vertex] == float('inf'):
                break
            visited[vertex] = True
            for node in self.nodes_list[vertex]:
                to = node[0]
                weight = node[1]
                if self.path[vertex] * weight < self.path[to]:
                    self.path[to] = self.path[vertex] * weight
                    self.previous[to] = vertex

    def get_way(self):
        with open('out.txt', 'w') as output_file:
            vertex = self.end
            result_path = []
            if len(result_path) == 0:
                output_file.write('N\n')
            else:
                while vertex != self.start:
                    result_path.append(vertex + 1)
                    vertex = self.previous[vertex]
                result_path.append(self.start + 1)
                result_path.reverse()
                output_file.write('Y\n')
                for element in result_path:
                    output_file.write(f'{element} ')
                output_file.write(f'\n{self.path[self.end]}')


def main():
    net = Net()
    net.read_net()
    net.find_way()
    net.get_way()


if __name__ == '__main__':
    main()
