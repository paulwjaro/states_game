from turtle import Screen, Turtle
import pandas
from label import Label


running = True
screen = Screen()
screen.title("States Game")
image = "blank_states_img.gif"
screen.addshape(image)

map_image = Turtle(shape=image)
state_data = pandas.read_csv("50_states.csv")
state_list = state_data["state"].tolist()
#x_list = state_data["x"].tolist()
#y_list = state_data["y"].tolist()
guessed_states = []

def pop_state(list_index):
    guessed_states.append(state_list[list_index])
    state_list[list_index] = "None"


question_state = "Enter your first guess."


while running:
    answer_state = screen.textinput(f"Progress: {len(guessed_states)}/50", f"{question_state}").lower()
    if answer_state == "quit":
        running = False

    for states in range(len(state_list)):
        if state_list[states].lower() == answer_state:
            new_state = Label()
            new_data = state_data[state_data.state == answer_state.title()]
            new_state.create_label(int(new_data.x), int(new_data.y), state_list[states])
            pop_state(states)
            question_state = "Enter your next guess."
            break
        else:
            for g_states in guessed_states:
                if answer_state == g_states.lower():
                    question_state = "You already guessed that state. Guess again."
                    break
                else:
                    question_state = "That is not a State. Guess again."

    if len(guessed_states) == 50:
        running = False

new_state_data = []

if len(guessed_states) < 50:
    for i in range(len(state_list)):
        if state_list[i] != "None":
            new_state_data.append(state_list[i])

unknown_states = pandas.DataFrame(new_state_data)

unknown_states.to_csv("States_to_Learn")
