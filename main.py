import re

# Function to convert spoken input to card value and suit
def convert_spoken_input(input_string):
    card_pattern = re.compile(r'([2-9TtJjQqKkAa]|(10))( of )(hearts|diamonds|clubs|spades)', re.IGNORECASE)
    match = card_pattern.match(input_string)
    if match:
        value, _, suit = match.groups()
        value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'T': 10, 't': 10, 'J': 11, 'j': 11, 'Q': 12, 'q': 12, 'K': 13, 'k': 13, 'A': 14, 'a': 14}
        suit_dict = {'hearts': '♥', 'diamonds': '♦', 'clubs': '♣', 'spades': '♠'}
        return value_dict[value], suit_dict[suit.lower()]
    else:
        return None

# Function to calculate preflop pot odds
def calculate_preflop_pot_odds(user_hand, total_players, pot_size):
    # Your calculation logic here
    # Replace this placeholder logic with your actual calculation

    return "Your preflop pot odds are 25%"

# Simulating user input
user_input = input("Please speak your card: ")
card = convert_spoken_input(user_input)
if card:
    print(f"You said: {card[0]} of {card[1]}")

    # Simulated values for total players and pot size
    total_players = 6
    pot_size = 100

    # Calculating preflop pot odds
    preflop_pot_odds = calculate_preflop_pot_odds(card, total_players, pot_size)
    print(preflop_pot_odds)
else:
    print("Invalid input. Please try again.")
