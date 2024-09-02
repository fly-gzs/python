# Csapatok nevei
teams = ['Németország', 'Skócia', 'Magyarország', 'Svájc']

# Csapatok statisztikái
stats = {
    'Németország': {'meccsek': 0, 'pontok': 0, 'győzelmek': 0, 'döntetlenek': 0, 'vereségek': 0, 'rúgott': 0, 'kapott': 0},
    'Skócia': {'meccsek': 0, 'pontok': 0, 'győzelmek': 0, 'döntetlenek': 0, 'vereségek': 0, 'rúgott': 0, 'kapott': 0},
    'Magyarország': {'meccsek': 0, 'pontok': 0, 'győzelmek': 0, 'döntetlenek': 0, 'vereségek': 0, 'rúgott': 0, 'kapott': 0},
    'Svájc': {'meccsek': 0, 'pontok': 0, 'győzelmek': 0, 'döntetlenek': 0, 'vereségek': 0, 'rúgott': 0, 'kapott': 0}
}

# Mérkőzések listája (csapat1, csapat2, eredmény)
matches = [
    ('Németország', 'Skócia', input('Németország - Skócia: ')),
    ('Magyarország', 'Svájc', input('Magyarország - Svájc: ')),
    ('Németország', 'Magyarország', input('Németország - Magyarország: ')),
    ('Skócia', 'Svájc', input('Skócia - Svájc: ')),
    ('Skócia', 'Magyarország', input('Skócia - Magyarország: ')),
    ('Svájc', 'Németország', input('Svájc - Németország: '))
]

def process_match(team1, team2, result):
    goals_team1, goals_team2 = map(int, result.split('-'))
    
    stats[team1]['meccsek'] += 1
    stats[team2]['meccsek'] += 1
    stats[team1]['rúgott'] += goals_team1
    stats[team1]['kapott'] += goals_team2
    stats[team2]['rúgott'] += goals_team2
    stats[team2]['kapott'] += goals_team1
    
    if goals_team1 > goals_team2:
        stats[team1]['pontok'] += 3
        stats[team1]['győzelmek'] += 1
        stats[team2]['vereségek'] += 1
    elif goals_team1 < goals_team2:
        stats[team2]['pontok'] += 3
        stats[team2]['győzelmek'] += 1
        stats[team1]['vereségek'] += 1
    else:
        stats[team1]['pontok'] += 1
        stats[team2]['pontok'] += 1
        stats[team1]['döntetlenek'] += 1
        stats[team2]['döntetlenek'] += 1

# Mérkőzések feldolgozása
for team1, team2, result in matches:
    if result:
        process_match(team1, team2, result)
    else:
        print(f'A {team1} - {team2} meccs még nem került megrendezésre!')

# Eredmények kiíratása
print('\n--- "A" csoport ---')
for team in teams:
    print(f"{team}: {stats[team]['meccsek']} meccs, {stats[team]['győzelmek']} győzelem, {stats[team]['döntetlenek']} döntetlen, {stats[team]['vereségek']} vereség, {stats[team]['pontok']} pont, gólkülönbség: {stats[team]['rúgott']}-{stats[team]['kapott']}")

print(teams)
print(stats)
print(matches)