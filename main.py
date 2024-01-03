# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# tem_list = data["temp"].to_list()
# print(tem_list)
# tem_list_avera = sum(tem_list)/len(tem_list)
# print(tem_list_avera)
#
# ave=data["temp"].mean()
# print(ave)
#
# max_temp = data["temp"].max()
# print((max_temp))

# get data in row
# row_monday = data[data["day"] == "Monday"]
# print(row_monday)

# get max temperature row
# max_temp_row = data[data["temp"] == data.temp.max()]
# print(max_temp_row)

# get monday temp
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# f= monday_temp*(9/5) + 32
# print(f)

# create data frame
#
# data_student = {
#     "student" : ["any", "james", "Angela"],
#     "scores":[76,56, 65]
# }
#
# data_student_panda = pandas.DataFrame(data_student)
# data_student_panda.to_csv("new csv")

##############################################################################
# NYS squirrels

# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240103.csv")
# # print(squirrel_data)
# # monday = data[data.day == "Monday"]
# squirrel_grey_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
# squirrel_cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
# squirrel_black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
#
# new_data = {
#     "Fur Color": ["grey", "red" , "black"],
#     "Count": [squirrel_grey_count, squirrel_cinnamon_count , squirrel_black_count],
# }
# squirrel_new_data = pandas.DataFrame(new_data)
# squirrel_new_data.to_csv("squirrel_count")


###################################################
# U.S.A. States game


import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S.A. States game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

import turtle

# Get coordinate of mouse
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()


data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guest_state = []
missing_state = []


def write_state_name(answer_state, state_list, guest_state,pen_color):
    if answer_state in state_list and answer_state not in guest_state:
        guest_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.pencolor(pen_color)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


while len(guest_state) < 50:
    answer_state = screen.textinput(title=f"{len(guest_state)} / 50", prompt="What's another state's name").title()
    if answer_state == "Exit":
        for state in state_list:
            if state not in guest_state:
                write_state_name(state, state_list, guest_state, pen_color="Red")
                missing_state.append(state)

        missing_state_panda = pandas.DataFrame(missing_state)
        missing_state_panda.to_csv("missing_state csv")
        break

    write_state_name(answer_state, state_list, guest_state, "Black")


screen.exitonclick()
