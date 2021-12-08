hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]

def get_score(team_name, teams):

     if team_name not in teams: 
         return  'Poxa, não encontramos esse time... Tente outro'
     else:
         pos = teams.index(team_name)
         return f'A {team_name} ficou classificada em {pos + 1}'       