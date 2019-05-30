class map_data:
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
        self.max_island = 0
    
    # by reset the x, y once visted, 
    # the RunTime complexity will be O(X * Y)
    def find_island_start(self):
        for x in range(self.x):
            for y in range(self.y):
                if self.data[x][y] == 1:
                    island_size = self.find_island(x, y)
                    if island_size > self.max_island:
                        self.max_island = island_size
    
    def find_island(self, x, y):
        print("entry", x, y)
        if x < 0 or x >= self.x or y < 0 or y >= self.y or self.data[x][y] == 0:
            return 0
        island_size = 1
        self.data[x][y] = 0
        island_size += self.find_island(x+1, y)
        island_size += self.find_island(x-1, y)
        island_size += self.find_island(x, y+1)
        island_size += self.find_island(x, y-1)
        print("pass checking", x, y, island_size)
        return island_size
        
    def print_island(self):
        print(self.max_island, self.data)
        
def main():
    data = map_data([[1, 1, 0, 1, 1], [0, 1, 1, 0, 1], [0, 1, 0, 1, 1], [0, 0, 1, 1, 1]], 4, 5)
    data.print_island()
    data.find_island_start()
    data.print_island()

if __name__ == '__main__':
    main()
