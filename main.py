import tkinter as tk
import random

user1 = False
user2 = False
count = 9
user_name = ""
buttons = ["" for i in range(9)]
game_on = True


def determine_first_user():  # when game starts it determines who start first
    global user1, user2, user_name
    user_numb = random.randint(1, 2)
    if user_numb == 1:
        user1 = True
        user_name = "Player 1 starts"
    else:
        user2 = True
        user_name = "Player 2 starts"
    info_label.configure(text=user_name)


def game_status_check():  # Controls and checks whether game is finished or not
    global count, game_on
    for player in ["X", "O"]:
        if ((buttons[0] == buttons[1] == buttons[2] == player) or
                (buttons[3] == buttons[4] == buttons[5] == player) or
                (buttons[6] == buttons[7] == buttons[8] == player) or
                (buttons[0] == buttons[3] == buttons[6] == player) or
                (buttons[1] == buttons[4] == buttons[7] == player) or
                (buttons[2] == buttons[5] == buttons[8] == player) or
                (buttons[0] == buttons[4] == buttons[8] == player) or
                (buttons[2] == buttons[4] == buttons[6] == player)):
            user = "Player1" if player == "X" else "Player2"
            end_game(f"{user} won the game")
            return
    if count == 0:
        end_game("Draw")


def end_game(game_message):
    global game_on
    info_label.configure(text=f"{game_message}")
    game_on = False


def user_move(but_id, but_sel):  # When box selected by user, writes X or O for related box and updates box array
    global user1, user2, count, user_name, game_on
    if buttons[but_id - 1] == "" and count > 0 and game_on:
        if user1:
            user_text = "X"
            user_name = "Player 2's turn"
            user1 = False
            user2 = True
        else:
            user_text = "O"
            user_name = "Player 1's turn"
            user1 = True
            user2 = False
        buttons[but_id - 1] = user_text
        but_sel.configure(text=user_text, )
        info_label.configure(text=user_name)
        count -= 1
        game_status_check()


# _____________________________________  BOARD GUI _______________________________________________
lb = tk.Tk()
lb.title("Tic Toc Game")
lb.configure(bg="salmon3")
lb.geometry("550x600+10+10")
lb.resizable(False, False)
i = tk.PhotoImage(width=1, height=1)

info_label = tk.Label(text="", bg="salmon3", fg="salmon4", font=('arial', 20, 'bold'))
info_label.place(x=10 + 10, y=550, width=500, height=50)

button_size = 170
padding = 10
button_count = 1
for row in range(3):
    for col in range(3):
        button_id = f"{button_count}"
        button = tk.Button(
            lb,
            relief="flat",
            borderwidth=0,
            bg="salmon2",
            activebackground="salmon2",
            font=('arial', 80, 'bold'),
            image=i,
            compound='bottom',
            anchor="center",
            fg="salmon4",

        )
        button.config(command=lambda b=button, b_id=int(button_id): user_move(b_id, b))
        button.place(x=col * (button_size + padding) + padding, y=row * (button_size + padding) + padding,
                     width=button_size, height=button_size)
        button_count += 1

determine_first_user()
lb.mainloop()
