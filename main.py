import datetime
import time

if __name__ == '__main__':
    max_time = 300
    begin_time = datetime.datetime.now()

    white_turn = True
    turn_starts = [datetime.datetime.now(), datetime.datetime.now()]
    while True:
        white_seconds = datetime.timedelta(seconds=0)
        black_seconds = datetime.timedelta(seconds=0)

        time_pos = 1
        while len(turn_starts) > time_pos:
            player_color = time_pos % 2

            #print(player_color)

            if player_color == 0:
                white_seconds = white_seconds + (turn_starts[time_pos] - turn_starts[time_pos - 1])
            elif player_color == 1:
                black_seconds = black_seconds + (turn_starts[time_pos] - turn_starts[time_pos - 1])
            time_pos += 1

        white_str = time.strftime("%M:%S", time.gmtime(max_time - white_seconds.seconds))
        black_str = time.strftime("%M:%S", time.gmtime(max_time - black_seconds.seconds))

        print("white: " + white_str + " & black: " + black_str)

        player_color = time_pos % 2
        if player_color == 0:
            print("White's turn.")
        elif player_color == 1:
            print("Black's turn.")

        input("Press enter key to end turn...\n")
        turn_starts.append(datetime.datetime.now())
