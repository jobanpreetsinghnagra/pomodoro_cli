import time
import typer

app = typer.Typer()

@app.command()
def start(timer: int = typer.Argument(25, help="The duration of the Pomodoro in minutes.")):
    """
    Starts a Pomodoro timer.
    """
    final_timer_minutes = timer # Start with the value provided via CLI or the default

    # Only ask for input if the default was used AND the user wants to choose
    if timer == 25: # Check if the default 25 minutes was used (or if the user explicitly typed 25)
        print("Do you want to go with the Classic Pomodoro (25 minutes)?: [y]/[n]")
        answer = ""
        while True:
            answer = input(": ").strip().lower()
            if answer in ("y", "n"):
                break
            print("Please enter a valid input: [y] for yes or [n] for no.")

        if answer == "n":
            while True:
                try:
                    user_time = int(input("Enter Time in minutes: "))
                    if user_time > 0:
                        final_timer_minutes = user_time
                        break
                    else:
                        print("Please enter a positive integer for the time.")
                except ValueError:
                    print("Invalid input. Please enter a whole number for minutes.")

    # Display logic (same as base before)
    def display_time(timer_minutes_to_display):
        timer_sec = timer_minutes_to_display * 60
        for x in range(timer_sec, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            print(f"00:{minutes:02}:{seconds:02}", end='\r')
            time.sleep(1)
        print("\nTime's up!")

    display_time(final_timer_minutes)

if __name__ == "__main__":
    app()