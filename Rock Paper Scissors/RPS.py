# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, 
    opponent_history=[],
    sequence_hist = {}     
    ):
    
    opponent_history.append(prev_play)
    guess = "P"

    if len(opponent_history) > 2:
        # beat opponent's last play
        guess = beat(opponent_history[-1])

    # prediction based on sequences len=5 stored in sequence_hist (could iterate through opponent_history for every play, but the dict method is a lot faster)
    if len(opponent_history) > 5:
        # determine last sequence of plays
        last_sequence = ("".join(opponent_history[-5:]))
        
        # add last sequence to dict(sequence history)
        sequence_hist[last_sequence] = sequence_hist.get(last_sequence, 0) + 1

        # list of possible next sequences
        possible_next = [
            last_sequence[1:] + "R",
            last_sequence[1:] + "P",
            last_sequence[1:] + "S"
            ]

        # get the counts of the possible next sequences
        filtered_sequ_hist = {
            sequ: sequence_hist[sequ] 
            for sequ in possible_next if sequ in sequence_hist
        }

        # determine most encountered sequence
        # if new sequence, i.e. filtered_sequ_hist is empty: counter last move
        if not filtered_sequ_hist:
            prediction = opponent_history[-1]
        else:
            prediction = max(filtered_sequ_hist, key = filtered_sequ_hist.get)[-1]
        guess = beat(prediction)

    # clear opponent and sequence history after 1000 games
    if len(opponent_history) == 1000:
        opponent_history.clear()
        sequence_hist.clear()

    return guess

def beat(play):
    if play == "R":
        return "P"
    elif play == "P":
        return "S"
    elif play == "S":
        return "R"

