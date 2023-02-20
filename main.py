import tkinter
import customtkinter
import matplotlib.pyplot as plt


hours = 0
minutes = 0
seconds = 0

hs = "0"
frequency_hours = 0
frequency_minutes = 0
frequency_seconds = 0
frequency_start_timer = True
frequency_clock = f"{hs}{frequency_hours}:0{frequency_minutes}:0{frequency_seconds}"

hs = "0"
FONT = "Courier"
start_timing = True

clock = f"{hs}{hours}:0{minutes}:0{seconds}"
hours_coded = ""


def start_timing_contractions():
    global seconds, minutes, hours, hs, start_timing, clock

    if start_timing:

        if hours == 10:
            hs = ""

        if minutes < 10 and seconds < 10:
            clock = f"{hs}{hours}:0{minutes}:0{seconds}"

        elif minutes < 10 <= seconds:
            clock = f"{hs}{hours}:0{minutes}:{seconds}"

        elif minutes >= 10 > seconds:
            clock = f"{hs}{hours}:{minutes}:0{seconds}"

        elif minutes >= 10 and seconds >= 10:
            clock = f"{hs}{hours}:{minutes}:{seconds}"

        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
        update_canvas()
    window.after(1000, start_timing_contractions)


def start_timing_frequency():
    global frequency_hours, frequency_minutes, frequency_seconds, frequency_start_timer, hs, frequency_clock

    if frequency_start_timer:

        if frequency_hours == 10:
            hs = ""

        if frequency_minutes < 10 and frequency_seconds < 10:
            frequency_clock = f"{hs}{frequency_hours}:0{frequency_minutes}:0{frequency_seconds}"

        elif frequency_minutes < 10 <= frequency_seconds:
            frequency_clock = f"{hs}{frequency_hours}:0{frequency_minutes}:{frequency_seconds}"

        elif frequency_minutes >= 10 > frequency_seconds:
            frequency_clock = f"{hs}{frequency_hours}:{frequency_minutes}:0{frequency_seconds}"

        elif frequency_minutes >= 10 and frequency_seconds >= 10:
            frequency_clock = f"{hs}{frequency_hours}:{frequency_minutes}:{frequency_seconds}"

        frequency_seconds += 1
        if frequency_seconds == 60:
            frequency_seconds = 0
            frequency_minutes += 1
            if frequency_minutes == 60:
                frequency_minutes = 0
                frequency_hours += 1

    print(frequency_clock)
    window.after(1000, start_timing_frequency)


def end_timing_frequency():
    global frequency_hours, frequency_minutes, frequency_seconds, frequency_start_timer, hs, frequency_clock
    frequency_start_timer = False
    with open("frequency_of_contractions.txt", 'a') as file:
        save = [frequency_hours, frequency_minutes, frequency_seconds]
        file.write(f"{save[1]}.{frequency_seconds}\n")
    frequency_clock = f"{hs}{frequency_hours}:0{frequency_minutes}:0{frequency_seconds}"


def end_of_contraction():
    global seconds, minutes, hours, hs, start_timing, clock
    start_timing = False
    with open("length_of_contraction.txt", 'a') as file:
        save = [hours, minutes, seconds]
        file.write(f"{save[1]}.{seconds}\n")


def update_canvas():
    canvas.itemconfig(timer_text, text=clock)


def new_contraction():
    global seconds, minutes, hours, clock, start_timing, frequency_start_timer, frequency_hours, frequency_minutes, \
        frequency_seconds
    seconds = 0
    minutes = 0
    hours = 0
    clock = f"{hs}{hours}:0{minutes}:0{seconds}"
    update_canvas()
    start_timing = True

    end_timing_frequency()
    frequency_hours = 0
    frequency_minutes = 0
    frequency_seconds = 0
    frequency_start_timer = True


def get_length_of_contractions():
    length_of_contraction = []
    with open("length_of_contraction.txt", 'r') as file:
        for line in file:
            line = line.rstrip()
            line = float(line)
            length_of_contraction.append(line)

    return length_of_contraction

    # print(length_of_contraction)


def get_frequency_of_contractions():
    frequency_of_contractions = []
    with open("frequency_of_contractions.txt", 'r') as file:
        for line in file:
            line = line.rstrip()
            line = float(line)
            frequency_of_contractions.append(line)

    return frequency_of_contractions

    # print(time_between_contraction)


def show_graph():

    frequency_of_contractions = get_frequency_of_contractions()
    length_of_contractions = get_length_of_contractions()

    if len(length_of_contractions) != len(frequency_of_contractions):
        print(f'length of contraction: {len(length_of_contractions)}, '
              f'frequency of contractions: {len(frequency_of_contractions)}')
        print("Can not show graph yet. Must wait until in a contraction")

    else:
        plt.scatter(10, 1, s=200, c='red', marker='o')

        plt.plot(frequency_of_contractions, length_of_contractions, marker='o', color='blue')
        plt.gca().invert_xaxis()

        # Add labels to the axes
        plt.xlabel('Frequency of Contractions')
        plt.ylabel('Length of Contraction')

        # Add a title to the plot
        plt.title('Length and Frequency of Contractions')

        plt.show()


# -------------------------- GUI -----------------------------------------


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

window = customtkinter.CTk()
window.title("Contraction Plot")
window.geometry("500x300")

canvas = tkinter.Canvas(width=350, height=60, bg="black", highlightthickness=0)
timer_text = canvas.create_text(175, 30, text=f"00:00:00", fill="blue", font=("Lorem ipsum dolor sit amet", 40))
canvas.grid(row=0, column=0, columnspan=2, pady=50, padx=50)

start_labour_button = customtkinter.CTkButton(master=window, text="Start Labour", command=start_timing_contractions,
                                              text_color="black")
start_labour_button.grid(row=1, column=0, pady=5, padx=10)


stop_button = customtkinter.CTkButton(master=window, text="End of Contraction", command=end_of_contraction,
                                      text_color="black")
stop_button.grid(row=1, column=1, pady=5, padx=10)

new_contraction_button = customtkinter.CTkButton(master=window, text="Start New Contraction", command=new_contraction,
                                                 text_color="black")
new_contraction_button.grid(row=2, column=1, pady=5, padx=10)

show_graph_button = customtkinter.CTkButton(master=window, text="Show Graph", command=show_graph, text_color="black")
show_graph_button.grid(row=3, column=1, pady=5, padx=10)

start_timing_frequency_button = customtkinter.CTkButton(master=window, text="Start Frequency",
                                                        command=start_timing_frequency, text_color="black")
start_timing_frequency_button.grid(row=2, column=0, pady=5, padx=10)

window.mainloop()
