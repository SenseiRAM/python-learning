import time
from datetime import datetime
from datetime import timedelta
import winsound
frequency = 2000  # Set Frequency To 2500 Hertz
duration = 250  # Set Duration To 1000 ms == 1 second
program_running = True
beeps = 3

print('Welcome to your Pomodoro timer!\n')


def pomodoro(frequency, duration, program_running, beeps):
    while program_running:
        beeps = 3
        timer_minutes = input('How many minutes would you like to focus? ')

        current_time = datetime.now()
        print('The current time is: ' + str(current_time))
        print(f'Another message will appear in {timer_minutes} minutes!\n')

        time.sleep(float(timer_minutes)*60)

        print(f'Your {timer_minutes} timer has expired. I hope you were able to focus! The current time is {str(datetime.now())}')

        while beeps > 0:
            winsound.Beep(frequency, duration)
            beeps -= 1

        time_over = input("Break time! When you're ready to start again, press Y. Enter any other key if you'd like to exit the program.\n")

        if time_over.lower() != 'y':
            program_running = False


def main():
    pomodoro(frequency, duration, program_running, beeps)

if __name__ == '__main__':
    main()
