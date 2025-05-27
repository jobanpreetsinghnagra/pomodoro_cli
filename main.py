import time
import typer

app = typer.Typer()


def get_input():
    default_time = 25
    timer = default_time

    print("Do you want to go with the Classic Pomodoro (25 minutes)?: [y]/[n]")

    while True:
        answer = input(": ").strip().lower()
        if answer in ("y", "n"):
            break
        print("Please enter a valid input: [y] for yes or [n] for no.")


    if answer == "n":
        user_time = int(input("Enter Time in minutes: "))
        timer = user_time
    return timer

def display_time(timer):
    timer_sec = timer*60


    for x in range(timer_sec ,0 ,-1):
        seconds = x%60
        minutes = int(x / 60) %60
        print(f"00:{minutes:02}:{seconds:02}")
        time.sleep(1)



@app.command()
def start_timer():
    display_time(get_input())


if __name__ == "__main__":
    app()
