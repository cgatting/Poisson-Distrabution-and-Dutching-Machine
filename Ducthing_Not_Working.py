demo_list = ["Draw", "1:1", "Under 2.5"]
demo_odds = [1.23, 2.65, 26]

def dutching(odds, bankroll):
    demo_dec = [1/x for x in odds]
    stakes = []
    for i in range(len(demo_dec)):
        stake = max(round((demo_dec[i]/sum(demo_dec))*bankroll, 2), 1)
        stakes.append(stake)
    loss = sum(stakes[1:])
    profit = round(abs((odds[0]-1)*stakes[0]), 2)
    dutching_profit = profit - loss
    return stakes, round(dutching_profit, 2)

def minimum_total_stake(odds):
    stakes_data = []
    for bankroll in range(0, 10000):
        bankroll = bankroll / 100
        demo_dec = [1/x for x in odds]
        stakes = []
        for i in range(len(demo_dec)):
            stake = round((demo_dec[i]/sum(demo_dec))*bankroll, 2)
            stakes.append(stake)
            stakes_data.append(stakes)
    return stakes_data

def find_closest_above_one(list_of_lists):
    closest_list = None
    closest_difference = float('inf')  # Initialize with a large value

    for sublist in list_of_lists:
        all_above_one = all(value > 1 for value in sublist)
        if all_above_one:
            for value in sublist:
                difference = abs(value - 1)
                if difference < closest_difference:
                    closest_difference = difference
                    closest_list = sublist
    return closest_list, round(sum(closest_list), 2) if closest_list is not None else (None, None)



def main(odds, bankroll):
    # Run the dutching calculation
    stakes, dutching_profit = dutching(odds, bankroll)

    # Find the minimum total stake that leads to all stakes above 1
    stakes_data = minimum_total_stake(odds)
    closest_stakes, total_stake = find_closest_above_one(stakes_data)

    # Generate the output sentence
    stake_str = ', '.join([f'{stake:.2f}' for stake in stakes])
    closest_stakes_str = ', '.join([f'{stake:.2f}' for stake in closest_stakes])
    
    output = (f"For a bankroll of {bankroll:.2f}, the dutching stakes would be {stake_str} with a dutching profit of {dutching_profit:.2f}. "
              f"The minimum total stake for all stakes above 1 is {total_stake:.2f}, and the stakes would be {closest_stakes_str}.")
    
    return output

    return closest_list, round(sum(closest_list), 2)


print(main(demo_odds, 10))