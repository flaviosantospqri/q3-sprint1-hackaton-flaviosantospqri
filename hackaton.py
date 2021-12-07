hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]

def get_score(team_name, teams):
     if team_name not in teams:
         return print('Poxa, não encontramos esse time... Tente outro')
     else:
         pos = teams.index(team_name)
         return print(f'Legal! A equipe {team_name} ficou na {pos + 1}ø colocação')
         
team_name = str(input('Digite o nome do Time: '))
teams = str(input('Digite o Evento: '))

if teams == 'hackathon_1':
    get_score(team_name, hackathon_1)
elif teams == 'hackathon_2':
    get_score(team_name, hackathon_2)
else:
    get_score(team_name, hackathon_3)