def arcade2001():
    '''
    Computer game: player and computer get random amounts of points until one of them has 2001 points.
    :return: "Player 1 won!" or "Player 2 won!"
    '''
    import random



    player_1_score = 0
    player_2_score = 0



    game_start = input("Press enter to play!")
    print(game_start)

    player_1_score = player_1_score + random.randint(1, 6) + random.randint(1, 6)
    player_2_score = player_2_score + random.randint(1, 6) + random.randint(1, 6)

    print(f"Player 1 score: {player_1_score}")
    print(f"Player 2 score: {player_2_score}")


    continue_game = input("Press enter to continue!")

    while True:
        player_1_new_points = random.randint(1, 6) + random.randint(1, 6)
        player_2_new_points = random.randint(1, 6) + random.randint(1, 6)




        if player_1_new_points == 7:
            player_1_score = player_1_score // 7
        elif player_1_new_points == 11:
            player_1_score = player_1_score * 11
        else:
            player_1_score = player_1_score + player_1_new_points

        if player_2_new_points == 7:
            player_2_score = player_2_score // 7
        elif player_2_new_points == 11:
            player_2_score = player_2_score * 11
        else:
            player_2_score = player_2_score + player_2_new_points



        print(f"Player 1 score: {player_1_score}")
        print(f"Player 2 score: {player_2_score}")

        if player_1_score >= int(2001):
            return "Player 1 won!"
        elif player_2_score >= int(2001):
            return "Player 2 won!"
        else: continue_game = input("Press enter to continue!")

print(arcade2001())


































