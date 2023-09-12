# import turtle
# timmy = turtle.Turtle()
# in the above line, the "turtle" is a module that we imported at the top of the code. the "Turtle" is a class that inside the "turtle" module.
# the name of the class usually follow this format.lets say the class is carmodle. we should type it or name it CarModle.

# from turtle import Turtle, Screen
# # the line above means from turtle module import Turtle class.
# timmy = Turtle()
# #  the line above means that we created an object called timmy.
# timmy.shape("turtle")
# timmy.color("pink", "green")
# timmy.forward(100)
#
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "c"
# can also get this done,simply add: "l" / "c" / "r" after the column list.
print(table)



