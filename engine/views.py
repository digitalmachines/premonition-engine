from django.http import HttpResponse

import requests

def index(request):

    # Get detailed home and away win-loss standings
    standings = requests.get("https://statsapi.web.nhl.com/api/v1/standings?expand=standings.record")
    standingsJSON = standings.json()

    print(standingsJSON)
        
    totalGames = ""

    # Get schedule of games for that day
    s = requests.get("https://statsapi.web.nhl.com/api/v1/schedule")
    response = s.json()
    
    games = response["totalGames"]
    print ('There are {} NHL games today.' .format(games))

    # Get team statistics
    stats = requests.get("https://statsapi.web.nhl.com/api/v1/teams/5/stats")
    teamStats = stats.json()

    statTypes = requests.get('https://statsapi.web.nhl.com/api/v1/statTypes')
    types = statTypes.json()

    # Top Plays
    # ATS Standings URL: https://www.actionnetwork.com/nhl/nhl-against-the-spread-standings
        # Islanders: 100% Home SU | 12-0 | Playing Today: NO
        # Hurricanes: 90.9% Home SU | 10-1 | Playing Today: NO
        # Golden Knights: 84.6% Home SU | 11-2 | Playing Today: YES | 10:00 PM | -239
        # Lightning: 83.3% Home SU | 10-2 | Playing Today: NO
        # Penguins: 80% Home SU | 12-3 | Playing Today: NO
        # Wild: 76.9% Home SU | 10-3 | Playing Today: NO

        # Blues: 83.3% Away SU | 10-2 | Playing Today: YES | 10:00 PM | -139
        # Panthers: 83.3% Away SU | 10-2 | Playing Today: YES | 10:00 PM | -139

    return HttpResponse(standingsJSON)