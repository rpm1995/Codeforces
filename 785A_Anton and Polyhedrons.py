n = int(input())
shapes = []
for _ in range(n):
    shapes.append(input())
shape_faces = {"Tetrahedron": 4,
               "Cube": 6,
               "Octahedron": 8,
               "Dodecahedron": 12,
               "Icosahedron": 20}
ans = 0

for shape in shapes:
    ans += shape_faces[shape]

print(ans)
