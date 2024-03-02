import math

class formations:
    #fix these formations
    # 3-1-4-2
    ThreeOneFourTwo = ['GK', 'CB', 'CB', 'CB', 'CDM', 'CM', 'CM', 'LM', 'RM', 'ST', 'ST']

    # 3-4-1-2
    ThreeFourOneTwo = ['GK', 'CB', 'CB', 'CB', 'CM', 'CM', 'LM', 'RM', 'CAM', 'ST', 'ST']

    # 3-4-2-1
    ThreeFourTwoOne = ['GK', 'CB', 'CB', 'CB', 'CM', 'CM', 'LM', 'RM', 'CF', 'CF', 'ST']

    # 3-4-3
    ThreeFourThree = ['GK', 'CB', 'CB', 'CB', 'CM', 'CM', 'LM', 'RM', 'LW', 'ST', 'RW']

    # 3-5-2
    ThreeFiveTwo = ['GK', 'CB', 'CB', 'CB', 'CDM', 'CM', 'LM', 'RM', 'CAM', 'ST', 'ST']

    # 4-1-2-1-2
    FourOneTwoOneTwo = ['GK', 'CB', 'CB', 'LB', 'RB', 'CDM', 'LM', 'RM', 'CAM', 'ST', 'ST']

    # 4-1-2-1-2 (2)
    FourOneTwoOneTwo_2 = ['GK', 'CB', 'CB', 'LB', 'RB', 'CDM', 'CM', 'CM', 'CAM', 'ST', 'ST']

    # 4-1-3-2
    FourOneThreeTwo = ['GK', 'CB', 'CB', 'LB', 'RB', 'CDM', 'CM', 'LM', 'RM', 'ST', 'ST']

    # 4-1-4-1
    FourOneFourOne = ['GK', 'CB', 'CB', 'LB', 'RB', 'CDM', 'CM', 'CM', 'LM', 'RM', 'ST']

    # 4-2-1-3
    FourTwoOneThree = ['GK', 'CB', 'CB', 'LB', 'RB', 'CDM', 'CDM',  'CAM', 'LW', 'RW', 'ST']

    # 4-2-2-2
    FourTwoTwoTwo = ['GK', 'CB', 'CB', 'LB', 'RB', 'CDM', 'CM', 'CAM', 'CAM', 'ST', 'ST']

    # 4-2-3-1
    FourTwoThreeOne = ['GK', 'CB', 'CB', 'LB', 'RB', 'CDM', 'CDM', 'CAM', 'CAM', 'CAM', 'ST']

    # 4-2-3-1 (2)
    FourTwoThreeOne_2 = ['GK', 'CB', 'CB', 'LB', 'RB', 'CDM', 'CDM' , 'CAM', 'LM', 'RM', 'ST']

    # 4-2-4
    FourTwoFour = ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'LW', 'RW', 'ST', 'ST']

    # 4-3-1-2
    FourThreeOneTwo = ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'CM', 'CAM', 'ST', 'ST']

    # 4-3-2-1
    FourThreeTwoOne = ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'CM', 'CF', 'CF' , 'ST']

    # 4-3-3
    FourThreeThree = ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'CM', 'LW', 'RW', 'ST']

    # 4-3-3 (2)
    FourThreeThree_2 = ['GK', 'CB', 'CB', 'LB', 'RB', 'CDM', 'CM', 'CM', 'LW', 'RW', 'ST']

    # 4-3-3 (3)
    FourThreeThree_3 = ['GK', 'CB', 'CB', 'LB', 'RB', 'CDM', 'CM', 'CM', 'LW', 'RW', 'ST']

    # 4-3-3 (4)
    FourThreeThree_4 = ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'CAM', 'LW', 'RW', 'ST']

    # 4-3-3 (5)
    FourThreeThree_5 = ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CDM', 'CM', 'CF', 'LW', 'RW']

    # 4-4-1-1
    FourFourOneOne = ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'CF', 'LM', 'RM', 'ST']

    # 4-4-1-1 (2)
    FourFourOneOne_2 = ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'CAM', 'LM', 'RM', 'ST']

    # 4-4-2
    FourFourTwo = ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'LM', 'RM', 'ST', 'ST']

    # 4-4-2 (2)
    FourFourTwo_2 = ['GK', 'CB', 'CB', 'LB', 'RB', 'CDM', 'CM', 'LM', 'RM', 'ST', 'ST']

    # 4-5-1
    FourFiveOne = ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'LM', 'RM', 'CAM', 'ST']

    # 4-5-1 (2)
    FourFiveOne_2 = ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'CM', 'LM', 'RM', 'ST']

    # 5-2-1-2
    FiveTwoOneTwo = ['GK', 'CB', 'CB', 'CB', 'LWB', 'RWB', 'CM', 'CAM', 'ST', 'ST']

    # 5-2-2-1
    FiveTwoTwoOne = ['GK', 'CB', 'CB', 'CB', 'LWB', 'RWB', 'CM', 'ST', 'LW', 'RW']

    # 5-2-3
    FiveTwoThree = ['GK', 'CB', 'CB', 'CB', 'LWB', 'RWB', 'CM', 'ST', 'LW', 'RW']

    # 5-3-2
    FiveThreeTwo = ['GK', 'CB', 'CB', 'CB', 'LWB', 'RWB', 'CDM', 'CM', 'ST', 'ST']

    # we are going have to rework how we handle formations as in the frontend
    #the user just gives us the number of players in each position
    def build_formation(userInput):
        formation = []
        for position in userInput:
            formation.append(position)
        return formation

class checkers:

    def check_is_not_valid(squad):
        count = 0
        players = set()
        for player in squad:
            count+=1
            players.add(player.name)
        if count != len(players):
            return True
        else: 
            return False
            

    #Team Rating: Min. (X)
    def check_team_rating(squad, min_rating):
        # Step 1: Sum up the ratings
        players = list(squad)
        total_rating = sum(player.rating for player in players)

        # Step 2: Get the average rating per player
        average_rating = total_rating / len(players)
        # Step 3: Calculate the correction factor
        cf = sum(player.rating - average_rating for player in squad if player.rating > average_rating)
        # Step 4: Add the correction factor to the sum
        total_with_cf = total_rating + cf

        # Step 5: Divide by the number of players
        raw_team_rating = total_with_cf / len(players)

        # Step 6: Round down
        team_rating = math.floor(raw_team_rating)

        # Check if the team rating meets the minimum rating
        return team_rating >= min_rating

    #leauge: min (a number) Player(s)
    #(X): Min. (X) Player(s)
    def check_league(squad, league, min_players):
        count = 0
        for player in squad:
            if player.league == league:
                count += 1
        return count >= min_players 

    #Number of Players in the Squad: (X)
    def check_num_players(squad, num_players):
        return len(squad) == num_players

    #Players from the same League: Max (X)
    def check_max_players_same_league(squad, max_players):
        leagues = {}
        for player in squad:
            if player.league in leagues:
                leagues[player.league] += 1
            else:
                leagues[player.league] = 1
        return max(leagues.values()) <= max_players

    #Players from the same Club: Max (X)
    def check_max_players_same_club(squad, max_players):
        clubs = {}
        for player in squad:
            if player.club in clubs:
                clubs[player['club']] += 1
            else:
                clubs[player.club] = 1
        return max(clubs.values()) <= max_players

    #Rare: Min. (X) Players
    #change this to say like to the right of the split on player rarity: Bronze Rare we are looking for the rare
    def check_min_rare(squad, min_rare):
        count = 0
        for player in squad:
            if 'Rare' in player.rarity.split(' '):
                count += 1
        return count >= min_rare


    #Leagues in Squad: Min. (X)
    def check_min_leagues(squad, min_leagues):
        leagues = set()
        for player in squad:
            leagues.add(player.league)
        return len(leagues) >= min_leagues

    #Clubs in Squad: Min. (x)
    def check_min_clubs(squad, min_clubs):
        clubs = set()
        for player in squad:
            clubs.add(player.club)
        return len(clubs) >= min_clubs

    #Gold: Min. (X) Players
    def check_min_gold(squad, min_gold):
        count = 0
        for player in squad:
            if player.rating >= 75:
                count += 1
        return count >= min_gold

    #Silver: Min. (X) Players
    def check_min_silver(squad, min_silver):
        count = 0
        for player in squad:
            if player.rating >= 65 and player.rating < 75:
                count += 1
        return count >= min_silver

    #Bronze: Min. (X) Players
    def check_min_bronze(squad, min_bronze):
        count = 0
        for player in squad:
            if player.rating < 65:
                count += 1
        return count >= min_bronze

    #nation      (a number)
    #(X) : Min. (X) Players
    def check_min_nation(squad, nation, min_nation):
        count = 0
        for player in squad:
            if player.nation == nation:
                count += 1
        return count >= min_nation

    #Players with minimum OVR of (X): Min.(X)
    def check_min_ovr(squad, min_ovr, min_players):
        count = 0
        for player in squad:
            if player.rating >= min_ovr:
                count += 1
        return count >= min_players

    #this can be like Club or Club: Min. (X) Player(s)
    #(X) OR (X): Min. (X) Player(s)
    def check_min_2_clubs(squad, club1, club2, min_players):
        count1 = 0
        count2 = 0
        for player in squad:
            if player.club == club1:
                count1 += 1
            elif player.club == club2:
                count2 += 1
        return count1 >= min_players or count2 >= min_players


    #Nationalities in Squad: Min. (X)
    def check_min_nationalities(squad, min_nationalities):
        nationalities = set()
        for player in squad:
            nationalities.add(player.nation)
        return len(nationalities) >= min_nationalities
    
    def check_totw(squad, min_totw):
        count = 0
        for player in squad:
            if player.rarity == 'Team of the Week':
                count += 1
        return count >= min_totw

    def check_player_quality(squad, quality):
        for player in squad:
            if quality not in player.rarity.split(' '):
                return False
        return True

    #def check_total_chemistry(squad, min_chemistry):
    #def check_chem_per_player(squad, min_chemistry):


    def check_min_club(squad, club, min_players):
        count = 0
        for player in squad:
            if player.club == club:
                count += 1
        return count >= min_players

    def check_min_2_nations(squad, nation1, nation2, min_players):
        count1 = 0
        for player in squad:
            if player.nation == nation1:
                count1 += 1
            elif player.nation == nation2:
                count1 += 1
        return count1 >= min_players

    def check_min_2_leagues(squad, league1, league2, min_players):
        count1 = 0
        for player in squad:
            if player.league == league1:
                count1 += 1
            elif player.league == league2:
                count1 += 1
        return count1 >= min_players

    def check_total_chemistry(squad, min_chemistry):
        return squad.total_chemistry >= min_chemistry
    
    def check_chem_per_player(squad, min_chemistry):
        for player in squad:
            if player.chemistry < min_chemistry:
                return False
        return True

    all_checkers = {
        #Team Rating: Min. (X)
        1: check_team_rating,

        #Team of the Week: Min. (X) Player(s)
        2: check_totw,

        #(X): Min. (X) Player(s)
        3: check_league, 

        #Number of Players in the Squad: (X)
        4: check_num_players,

        #Players from the same League: Max (X)
        5: check_max_players_same_league,

        #Players from the same Club: Max (X)
        6: check_max_players_same_club,

        #Rare: Min. (X) Players
        7: check_min_rare,

        #Leagues in Squad: Min. (X)
        8: check_min_leagues,

        #Clubs in Squad: Min. (x)
        9: check_min_clubs,

        #Gold: Min. (X) Players
        10: check_min_gold,

        #Silver: Min. (X) Players
        11: check_min_silver,

        #Bronze: Min. (X) Players
        12: check_min_bronze,

        # (X) : Min. (X) Players
        13: check_min_nation,

        #Players with minimum OVR of (X): Min.(X)
        14: check_min_ovr,

        #(X) or (X): Min. (X) Player(s)
        15: check_min_2_clubs,

        #Nationalities in Squad: Min. (X)
        16: check_min_nationalities,

        #Player Quality: Exactly (X)
        17: check_player_quality,

        #Total Chemistry: Min. (X)
        18: check_total_chemistry,

        #Chemistry Points on Each Player: Min.(X)
        19:check_chem_per_player,

        #(X): Min. (X) Players
        20: check_min_club,

        #(X) or (X): Min. (X) Player(s)
        21: check_min_2_nations,

        #(X) or (X): Min. (X) Player(s)
        22: check_min_2_leagues,
    }