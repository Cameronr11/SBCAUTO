import sqlite3
import math
import Flask.Helper as  Helper #to test just this file take out "Flask.Helper as" 
import random
import json

class Player:
    def __init__(self, Name, Rating, PrefPosition, Alt_position, League, Rarity, Nation, Club):
        self.name = Name
        self.rating = Rating
        self.preferred_position = PrefPosition
        self.alternate_position = [pos.strip().strip("'") for pos in Alt_position.strip("[]").split(',')] if Alt_position else []
        self.league = League
        self.rarity = Rarity
        self.nation = Nation
        self.club = Club
        self.positions = [self.preferred_position] + self.alternate_position
        self.chemistry = 0

    def __str__(self):
        alt_positions = ', '.join(self.alternate_position) if self.alternate_position else 'None'
        return f"{self.name} {self.rating} {self.preferred_position} [{alt_positions}] {self.league} {self.rarity} {self.nation} {self.club} {self.chemistry}"

class Squad:
    def __init__(self, formation):
        self.formation = formation
        self.player_assignments = []
        self.added_player_names = []
        self.fitness = 0
        self.total_chemistry = 0



    def calculate_chemistry_for_all(self):
        # Reset total squad chemistry
        self.total_chemistry = 0

        # Calculate attribute counts for the entire squad
        league_counts, nation_counts, club_counts = self.count_attributes_for_squad()

        # Assign chemistry points to each player based on attribute counts
        for position, player in self.player_assignments:
            self.assign_chemistry_points(player, league_counts, nation_counts, club_counts)
            self.total_chemistry += player.chemistry


    def assign_chemistry_points(self, player, league_counts, nation_counts, club_counts):
        # Reset player's chemistry
        player.chemistry = 0

        # Assign points based on league
        player.chemistry += self.calculate_points(league_counts[player.league], [3, 5, 8])
        # Assign points based on nation
        player.chemistry += self.calculate_points(nation_counts[player.nation], [2, 5, 8])
        # Assign points based on club
        player.chemistry += self.calculate_points(club_counts[player.club], [2, 4, 7])

    def count_attributes_for_squad(self):
        league_counts, nation_counts, club_counts = {}, {}, {}
        for _, player in self.player_assignments:
            league_counts[player.league] = league_counts.get(player.league, 0) + 1
            nation_counts[player.nation] = nation_counts.get(player.nation, 0) + 1
            club_counts[player.club] = club_counts.get(player.club, 0) + 1
        return league_counts, nation_counts, club_counts
    
    def calculate_points(self, count, thresholds):
        points = 0
        for threshold, point in zip(thresholds, [1, 2, 3]):
            if count >= threshold:
                points = point
            else:
                break
        return points

    def add_player(self, player, position):
        if position in self.formation and player.name not in self.added_player_names:
            self.player_assignments.append((position,player))
            self.added_player_names.extend(player.name)


    def calculate_fitness(self, json_input):
        self.fitness = 0
        for criterion_id, value in json_input.items():
            if criterion_id in Helper.checkers.all_checkers:
                if Helper.checkers.check_is_not_valid(self):
                    self.fitness = 0
                    break
                check_function = Helper.checkers.all_checkers[criterion_id]
                if criterion_id == 22:  # Special case for check_min_2_leagues
                    league1 = value[0]  # Extract the first league
                    league2 = value[1]  # Extract the second league
                    min_players = value[2]  # Extract the minimum number of players
                    if check_function(self, league1, league2, min_players):
                        self.fitness += 10
                    else:
                        self.fitness -= 5
                elif criterion_id == 21:  # Special case for check_min_2_nations
                    nation1 = value[0]  # Extract the first nation
                    nation2 = value[1]  # Extract the second nation
                    min_players = value[2]  # Extract the minimum number of players
                    if check_function(self, nation1, nation2, min_players):
                        self.fitness += 10
                    else:
                        self.fitness -= 5
                elif criterion_id == 20:  # Special case for check_min_club
                    club = value[0]  # Extract the club
                    min_players = value[1]  # Extract the minimum number of players
                    if check_function(self, club, min_players):
                        self.fitness += 10
                    else:
                        self.fitness -= 5
                elif criterion_id == 15:  # Special case for check_min_2_clubs
                    club1 = value[0]  # Extract the first club
                    club2 = value[1]  # Extract the second club
                    min_players = value[2]  # Extract the minimum number of players
                    if check_function(self, club1, club2, min_players):
                        self.fitness += 10
                    else:
                        self.fitness -= 5
                elif criterion_id == 14:  # Special case for check_min_ovr
                    min_ovr = value[0]  # Extract the minimum overall rating
                    min_players = value[1]  # Extract the minimum number of players
                    if check_function(self, min_ovr, min_players):
                        self.fitness += 10
                    else:
                        self.fitness -= 5
                elif criterion_id == 13:  # Special case for check_min_nation
                    nation = value[0]  # Extract the nation
                    min_players = value[1]  # Extract the minimum number of players
                    if check_function(self, nation, min_players):
                        self.fitness += 10
                    else:
                        self.fitness -= 5
                elif criterion_id == 3:  # Special case for check_league
                    league = value[0]  # Extract the league
                    min_players = value[1]  # Extract the minimum number of players
                    if check_function(self, league, min_players):
                        self.fitness += 10
                    else:
                        self.fitness -= 5
                else:
                    # Handle other criteria as before
                    if check_function(self, value):
                        self.fitness += 10
                    else:
                        self.fitness -= 5

    def __iter__(self):
        for _, player in self.player_assignments:
            yield player

    def __str__(self):
        squad_str = ""
        # Adjust to use position from tuple
        for position, player in self.player_assignments:
            squad_str += f"{position}: {player}\n"
        return f"Squad:\n{squad_str}"
    



class genetic:
    def initialize_population(formation, players, json_input, population_size=1000):
        population = []
        for _ in range(population_size):
            squad = Squad(formation)
            for position in formation:
                eligible_players = []
                for player in players:
                    if position in player.positions and player.name not in squad.added_player_names:
                        eligible_players.append(player)
                    else:
                        print(f"Skipped player: {player.name} for position: {position}")


                if eligible_players:
                    selected_player = random.choice(eligible_players)
                    squad.add_player(selected_player, position)
            squad.calculate_chemistry_for_all()
            squad.calculate_fitness(json_input)  # Calculate fitness for the squad after all players are added
            population.append(squad)
        return population


    def tournament_selection(population, tournament_size):
        selected_squads = []
        for _ in range(len(population)):
            # Randomly select squads for the tournament
            tournament_candidates = random.sample(population, tournament_size)
            # Choose the squad with the highest fitness in the tournament
            winner = max(tournament_candidates, key=lambda squad: squad.fitness)
            selected_squads.append(winner)
        return selected_squads

    def crossover(squad1, squad2, json_input):
        # Choose a random crossover point
        crossover_point = random.randint(1, len(squad1.player_assignments) - 1)
        
        # Create offspring by swapping player assignments at the crossover point
        offspring1 = Squad(squad1.formation)
        offspring2 = Squad(squad2.formation)
        
        offspring1.player_assignments = squad1.player_assignments[:crossover_point] + squad2.player_assignments[crossover_point:]
        offspring2.player_assignments = squad2.player_assignments[:crossover_point] + squad1.player_assignments[crossover_point:]
        
        # Recalculate fitness for the offspring
        offspring1.calculate_fitness(json_input)
        offspring2.calculate_fitness(json_input)
        
        return offspring1, offspring2


    def mutation(squad, players, mutation_rate, json_input):
        if random.random() < mutation_rate:
            # Choose a random position in the squad to mutate
            position_to_mutate = random.choice(squad.formation)
            
            # Filter players not already in the squad and eligible for the position
            eligible_players = [player for player in players if position_to_mutate in player.positions and player.name not in squad.added_player_names]
            
            if eligible_players:
                # Choose a random player to replace the player at the selected position
                new_player = random.choice(eligible_players)
                
                # Find the player currently assigned to this position
                for i, (position, player) in enumerate(squad.player_assignments):
                    if position == position_to_mutate:
                        # Safety check before removing
                        if player.name in squad.added_player_names:
                            squad.added_player_names.remove(player.name)
                        squad.added_player_names.extend(new_player.name)  # Update the set with the new player's name
                        # Replace the player in the assignment
                        squad.player_assignments[i] = (position, new_player)
                        break

                # Recalculate fitness for the mutated squad
                squad.calculate_fitness(json_input)
        
        return squad


    def reproduce(selected_squads, crossover_rate, mutation_rate, players, json_input):
        new_population = []
        for i in range(0, len(selected_squads), 2):
            squad1 = selected_squads[i]
            squad2 = selected_squads[(i + 1) % len(selected_squads)]  # Ensure index is within bounds
            # Apply crossover with a certain probability
            if random.random() < crossover_rate:
                offspring1, offspring2 = genetic.crossover(squad1, squad2, json_input)  # Corrected to remove json_input
            else:
                offspring1, offspring2 = squad1, squad2
            # Apply mutation with a certain probability
            offspring1 = genetic.mutation(offspring1, players, mutation_rate, json_input)
            offspring2 = genetic.mutation(offspring2, players, mutation_rate, json_input)
            new_population.extend([offspring1, offspring2])
        return new_population


def load_players_from_database():
    connection = sqlite3.connect('Scraped_Player_Database.db')
    cursor = connection.cursor()
    query = "SELECT Name, Rating, PrefPosition, Alt_position, League, Rarity, Nation, Club FROM players"
    cursor.execute(query)
    players_data = cursor.fetchall()
    connection.close()
    # Transform the fetched data into Player objects and return them
    players = [Player(*player_data) for player_data in players_data]
    return players

def solve_sbc(formation, players, json_input):
# Generate a single population of squads
    count = 0
    while count < 11:
        population = genetic.initialize_population(formation, players, json_input, population_size=15)
        tournament_size = 10
        crossover_rate = 0.8
        mutation_rate = 0.1
        num_generations = 500

        # Inside your main loop where you evolve the generations
        for generation in range(num_generations):
            selected_squads = genetic.tournament_selection(population, tournament_size)
            population = genetic.reproduce(selected_squads, crossover_rate, mutation_rate, players, json_input)
            # Update fitness for the new population
            for squad in population:
                squad.calculate_fitness(json_input)
                squad.calculate_chemistry_for_all()
    # Ensure there are squads left to check
        best_squad = max(population, key=lambda squad: squad.fitness)
        if best_squad.fitness == len(json_input) * 10:
            break
        else:
            count += 1

    # Print the best squad
    print("Best Squad:")
    print(best_squad)
    print("Best Squad Fitness:", best_squad.fitness)
    print(f"Total Chemistry: {best_squad.total_chemistry}")
    return best_squad


#to test just this file un comment tests below

#formation = ['GK', 'LB', 'CB', 'CB', 'RB', 'LM', 'CM', 'CM', 'RM', 'ST', 'ST']
#json_input = {
    #1: 80,
    #8: 4,
    #18:10
#}
#players = load_players_from_database()
#solve_sbc(formation, players, json_input)