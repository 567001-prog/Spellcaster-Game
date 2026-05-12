def end(__a__, __b__):
    pen.clear()
    if __a__ == 4:
        status = "VICTORY"
        message_color = "gold"
        end_text = [
            f"Congratulations, {name}!",
            "Thank you so much for saving our kingdom!"
        ]
    else:
        status = "DEFEAT"
        message_color = "red"
        end_text = [
            f"You lost, {name}...",
            f"The kingdom has collapsed..."
        ]

    pen.color(message_color)
    pen.goto(0, 180)
    pen.write(status, align="center", font=("Impact", 40, "bold"))

    pen.color("white")
    current_y = 80

    for line in end_text:
        pen.goto(0, current_y)
        pen.write(
            line,
            align="center",
            font=("Times New Roman", 22, "bold")
        )
        current_y -= 50
