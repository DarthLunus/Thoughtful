from sort import sort_packages

packages = [
    {"width": 30, "height": 40, "length": 50, "mass": 5},
    {"width": 30, "height": 40, "length": 50, "mass": 25},
    {"width": 160, "height": 30, "length": 40, "mass": 10},
    {"width": 100, "height": 100, "length": 100, "mass": 10},
    {"width": 100, "height": 100, "length": 100, "mass": 25},
    {"width": 200, "height": 160, "length": 180, "mass": 25},
    {"width": 10, "height": 10, "length": 10, "mass": 1},
    {"width": 50, "height": 40, "length": 30, "mass": 22},
    {"width": 150, "height": 50, "length": 50, "mass": 10},
    {"width": 149, "height": 149, "length": 44, "mass": 19.9},
]


sorted_packages = sort_packages(packages)

for p in sorted_packages:
    print(p)
