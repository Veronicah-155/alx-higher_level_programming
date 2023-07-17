#!/usr/bin/python3
"""
Class Base Module
"""
import json
import csv
import turtle


class Base:
    """Define the class base"""
    __nb_objects = 0


    def __init__(self, id=None):
        """initializing the base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, "w") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as f:
                json_data = f.read()
                data = cls.from_json_string(json_data)
                instances = [cls.create(**item) for item in data]
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def to_csv_row(obj):
        """adding the class methods"""
        if isinstance(obj, Rectangle):
            return [obj.id, obj.width, obj.height, obj.x, obj.y]
        elif isinstance(obj, Square):
            return [obj.id, obj.size, obj.x, obj.y]

    @staticmethod
    def from_csv_row(row):
        """Rectangle class method"""
        if len(row) == 5:
            return Rectangle(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]))
        elif len(row) == 4:
            return Square(int(row[0]), int(row[1]), int(row[2]), int(row[3]))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """claas method to save file"""
        filename = cls.__name__ + ".csv"
        rows = [cls.to_csv_row(obj) for obj in list_objs]

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """class method to load file"""
        filename = cls.__name__ + ".csv"
        objs = []

        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                obj = cls.from_csv_row(row)
                objs.append(obj)
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """creating draw class"""
        turtle.setup(800, 600)
        window = turtle.Screen()
        window.bgcolor("white")
        t = turtle.Turtle()
        t.speed(2)

        for rectangle in list_rectangles:
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            t.forward(rectangle.width)
            t.left(90)
            t.forward(rectangle.height)
            t.left(90)
            t.forward(rectangle.width)
            t.left(90)
            t.forward(rectangle.height)
            t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)

        turtle.done()

class Rectangle(Base):
    """Rectangle base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the rect. base"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

class Square(Base):
    """Square base class module"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the square"""
        super().__init__(id)
        self.size = size
        self.x = x
        self.y = y
