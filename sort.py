from typing import List, Dict


class Package:
    def __init__(self, width: float, height: float, length: float, mass: float):
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass

    def volume(self) -> float:
        return self.width * self.height * self.length

    def is_bulky(self) -> bool:
        return (
            self.volume() >= 1_000_000
            or self.width >= 150
            or self.height >= 150
            or self.length >= 150
        )

    def is_heavy(self) -> bool:
        return self.mass >= 20


class PackageValidator:
    @staticmethod
    def classify(package: Package) -> str:
        bulky = package.is_bulky()
        heavy = package.is_heavy()

        return (
            "REJECTED" if bulky and heavy
            else "SPECIAL" if bulky or heavy
            else "STANDARD"
        )


def sort_packages(package_list: List[Dict]) -> List[Dict]:
    classified_packages = []
    for data in package_list:
        pkg = Package(
            width=data.get("width", 0),
            height=data.get("height", 0),
            length=data.get("length", 0),
            mass=data.get("mass", 0),
        )
        classification = PackageValidator.classify(pkg)
        data["classification"] = classification
        classified_packages.append(data)
    return classified_packages
