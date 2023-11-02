def egg_dropping_simulation(total_floors):
    # Initialize variables
    attempts = 0  # Number of attempts made
    x = 14  # Starting floor based on the formula

    while x <= total_floors:
        attempts += 1
        # Drop an egg from floor x
        if x >= total_floors:
            print(f"Egg broke on floor {x}, and it took {attempts} attempts.")
            break
        else:
            print(f"Egg didn't break on floor {x}.")
            x += (x - 1)  # Calculate the next floor to try

    print(f"Highest safe floor found: {x - (x - 1)}")
    print(f"Total attempts made: {attempts}")

# Call the simulation for a 100-story building
if __name__ == '__main__':
    egg_dropping_simulation(100)