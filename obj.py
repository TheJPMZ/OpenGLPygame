class Obj:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.texcoords = []
        self.normals = []
        self.faces = []

        for line in self.lines:
            try:
                prefix, value = line.split(' ', 1)
            except:
                continue

            if prefix == 'v':  # Vertices
                try:
                    self.vertices.append(list(map(float, value.split(' '))))
                except ValueError:
                    print(value)
                    raise
            elif prefix == 'vt':
                self.texcoords.append(list(map(float, value.split(' '))))
            elif prefix == 'vn':
                self.normals.append(list(map(float, value.split(' '))))
            elif prefix == 'f':
                try:
                    self.faces.append([list(map(int, vert.strip().split('/'))) for vert in value.strip().split(' ')])
                except ValueError:
                    print(value)
                    raise
        print("Successfully loaded Model: ", filename)
