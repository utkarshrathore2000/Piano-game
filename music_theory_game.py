import random

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

def generate_notes():
    """
    This function will generate the random notes
    :return: first_note, second_note
    """
    first_note = random.choice(notes)
    second_note = random.choice(notes)
    return first_note, second_note

def calculate_semitones(first_note, second_note):
    """
        This function calculate the semitones between the two random notes
        :param: first_note, second_note
        :return: semitones
    """
    note_values = {note: iterator for iterator, note in enumerate(notes)}
    semitones = abs(note_values[first_note] - note_values[second_note])
    if semitones > 6:
        semitones = 12 - semitones
    return semitones

def play_game(instruction=True):
    """
    This function plays a game to guess the semitones between the two notes
    :param instruction:
    :return:None
    """
    if instruction:
        print("Welcome to the music theory game!")
        print("You will be presented with two random notes and asked to guess the number of semitones between them.")
    print("If you give up, the correct answer will be displayed please type `give up` if you want.")
    first_note, second_note = generate_notes()
    semitones = calculate_semitones(first_note, second_note)
    while True:
        guess = input(f"Guess the number of semitones between {first_note} and {second_note}:")
        try:
            guess = int(guess)
            if guess == semitones:
                print ("You are correct!")
                play_again()
            else:
                print ("Incorrect guess. Try again.")
        except ValueError:
            if guess.lower() == 'give up':
                print (f"The correct answer is {semitones}.")
                play_again()
            else:
                print ("Please guess the number in integer format.")
                play_game(instruction=False)

def play_again():
    response = input("Would you like to play again? (y/n): ")
    if response.lower() == 'y':
        play_game(instruction=False)
    elif response.lower() == 'n':
        print("Thanks for playing!")
        quit()
    else:
        print('Please choose the correct option.')
        play_again()


if __name__ == "__main__":
    play_game()


