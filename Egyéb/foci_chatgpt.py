class Team:
    def __init__(self, name):
        self.name = name
        self.matches = 0
        self.points = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0

    @property
    def goal_difference(self):
        return self.goals_for - self.goals_against

    def record_match(self, goals_for, goals_against):
        self.matches += 1
        self.goals_for += goals_for
        self.goals_against += goals_against
        if goals_for > goals_against:
            self.wins += 1
            self.points += 3
        elif goals_for < goals_against:
            self.losses += 1
        else:
            self.draws += 1
            self.points += 1

    def __str__(self):
        return f'{self.name}: {self.matches} matches, {self.wins} wins, {self.draws} draws, {self.losses} losses, {self.points} points, goal difference: {self.goal_difference}'


def process_match(team1, team2, result):
    goals_team1, goals_team2 = map(int, result.split('-'))
    team1.record_match(goals_team1, goals_team2)
    team2.record_match(goals_team2, goals_team1)


def main():
    germany = Team('Németország')
    scotland = Team('Skócia')
    hungary = Team('Magyarország')
    switzerland = Team('Svájc')

    matches = [
        (germany, scotland, input(f'{germany.name} - {scotland.name} ')),
        (hungary, switzerland, input(f'{hungary.name} - {switzerland.name} ')),
        (germany, hungary, input(f'{germany.name} - {hungary.name} ')),
        (scotland, switzerland, input(f'{scotland.name} - {switzerland.name} ')),
        (scotland, hungary, input(f'{scotland.name} - {hungary.name} ')),
        (switzerland, germany, input(f'{switzerland.name} - {germany.name} '))
    ]

    for team1, team2, result in matches:
        if result:
            process_match(team1, team2, result)
        else:
            print(f'A {team1.name} - {team2.name} meccs még nem került megrendezésre!')

    teams = [germany, scotland, hungary, switzerland]

    print('\n--- "A" csoport ---')
    for team in teams:
        print(team)


if __name__ == "__main__":
    main()
