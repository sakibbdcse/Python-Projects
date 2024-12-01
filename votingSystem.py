# Constants
MAX_C = 10  # Maximum number of candidates
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '~', '+']  # Available symbols

# Candidate structure as a class
class Candidate:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.votes = 0

# List to store all candidates
all_candidates = []
symbol_taken = [False] * len(SYMBOLS)  # Keep track of used symbols

# Functions
def fill_candidate(c_num):
    print("Available Symbols:")
    for i, symbol in enumerate(SYMBOLS):
        if not symbol_taken[i]:
            print(f"{i + 1}: {symbol}")

    while True:
        try:
            symbol_choice = int(input(f"Enter the symbol number for candidate {c_num + 1}: ")) - 1
            if 0 <= symbol_choice < len(SYMBOLS) and not symbol_taken[symbol_choice]:
                symbol_taken[symbol_choice] = True
                symbol = SYMBOLS[symbol_choice]
                break
            else:
                print("Invalid or already chosen symbol. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    name = input(f"Enter the name of candidate {c_num + 1}: ")
    all_candidates.append(Candidate(name, symbol))

def display_all_candidates():
    print("\nCandidates:")
    for candidate in all_candidates:
        print(f"{candidate.name} ({candidate.symbol})")

def get_votes(num_voters):
    for voter in range(num_voters):
        display_all_candidates()
        while True:
            try:
                choice = int(input(f"Voter {voter + 1}, please enter your choice (1-{len(all_candidates)}): ")) - 1
                if 0 <= choice < len(all_candidates):
                    all_candidates[choice].votes += 1
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

def get_results():
    max_votes = max(candidate.votes for candidate in all_candidates)
    winners = [candidate for candidate in all_candidates if candidate.votes == max_votes]

    print("\n-----RESULT-----")
    if len(winners) > 1:
        print("No candidate has majority votes.")
    elif winners:
        winner = winners[0]
        print(f"The winner is: {winner.name}\nCandidate Symbol: {winner.symbol}\nwith {winner.votes} votes!")
    else:
        print("No votes were cast.")

# Main logic
def main():
    global all_candidates
    while True:
        try:
            candidate_count = int(input("Enter the number of candidates: "))
            if 1 <= candidate_count <= MAX_C:
                break
            else:
                print(f"Number of candidates must be between 1 and {MAX_C}.")
        except ValueError:
            print("Please enter a valid number.")

    for i in range(candidate_count):
        fill_candidate(i)

    while True:
        try:
            num_voters = int(input("Enter the number of voters: "))
            if num_voters > 0:
                break
            else:
                print("Number of voters must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    get_votes(num_voters)
    get_results()

# Run the program
if __name__ == "__main__":
    main()
