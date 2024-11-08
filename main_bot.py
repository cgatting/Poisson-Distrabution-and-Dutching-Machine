import requests
from bs4 import BeautifulSoup
from datetime import datetime
import random as r
import itertools

def calculate_optimal_stakes(pct_list, bankroll):
    o = [100/p for p in pct_list]
    c = list(itertools.combinations(o, 3))
    if not c:
        return None, None, None, None, None
    t = [1/sum(1/x for x in b) for b in c]
    d = [[round(p/x*100, 2) for x in b] for p,b in zip(t,c)]
    r = [round(sum(bankroll*p/100 for p in x)-bankroll,2) for x in d]
    max_idx = r.index(max(r))
    o_comb = list(c)[max_idx]
    o_pct = [round(100/x, 2) for x in o_comb]
    o_dutch = d[max_idx]
    o_stake = [round(bankroll*x/100, 0) for x in o_dutch]
    dutching_profit = max(o_dutch) * bankroll / 100
    return o_pct, o_comb, o_stake, o_dutch, dutching_profit

def dutch():
    # Example usage:
    pct_list = [float(input("%ages: ")) for _ in range(6)]
    bankroll = float(input("How much we playing with: "))
    optimal_pct, optimal_combination, optimal_stakes, optimal_dutch_list, dutching_profit = calculate_optimal_stakes(pct_list, bankroll)

    if optimal_pct is None:
        print("Not enough values to calculate optimal stakes.")
    else:
        print("Optimal percentages:", optimal_pct)
        print("Optimal combination:", optimal_combination)
        print("Optimal stakes:", optimal_stakes)
        print("Dutching profit returned:", dutching_profit)

def team_names():
    invalid = ["AC ", "FC ", " Utd", "Nottm", "Wolverhampton", " B", "Hellas ", "Leicester City"]
    url = 'https://www.soccerstats.com/matches.asp?matchday=1&listing=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': 'btable'})
    rows = table.find_all('tr')
    count = 0
    home_teams, away_teams = [], []
    for row in rows:
        if count <= 0:
            cols = row.find_all('td')
            if cols:
                t1, t2 = [cols[i].text.strip() for i in [9, 11]]
                home_teams.append(t1)
                away_teams.append(t2)
                count += 1
    new_home_teams = home_teams
    new_away_teams = [away_teams[home_teams.index(i)] for i in new_home_teams]
    invalid_home_names = list(new_home_teams)
    invalid_away_names = list(new_away_teams)
    for i in range(len(new_home_teams)):
        for code in invalid:
            if code in new_home_teams[i]:
                replace = ""
                if code == "Wolverhampton":
                    replace = "Wolves"
                if code == "Bilbao":
                    replace = "Club"
                elif code == "Nottm":
                    replace = "Nottingham"
                elif code == "Leicester City":
                    replace = "Leicester"
                new_home_teams[i] = new_home_teams[i].replace(code, replace)
            if code in new_away_teams[i]:
                replace = ""
                if code == "Wolverhampton":
                    replace = "Wolves"
                elif code == "Nottm":
                    replace = "Nottingham"
                elif code == "Leicester City":
                    replace = "Leicester"
                new_away_teams[i] = new_away_teams[i].replace(code, replace)
    return new_home_teams, new_away_teams, invalid_home_names, invalid_away_names


def find_teams_names(team_name):
    invalid = ["AC ", "FC ", " Utd", "Nottm", "Wolverhampton", " B"]
    url = 'https://www.soccerstats.com/matches.asp?matchday=1&listing=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': 'btable'})
    rows = table.find_all('tr')
    home_teams, away_teams = [], []
    for row in rows:
        cols = row.find_all('td')
        if cols:
            if cols[9].text == team_name or cols[11].text == team_name:
                t1, t2, time = [cols[i].text.strip() for i in [9, 11, 10]]
                home_teams.append(t1)
                away_teams.append(t2)
    new_home_teams = home_teams
    new_away_teams = [away_teams[home_teams.index(i)] for i in new_home_teams]
    invalid_home_names = list(new_home_teams)
    invalid_away_names = list(new_away_teams)
    for i in range(len(new_home_teams)):
        for code in invalid:
            if code in new_home_teams[i]:
                replace = ""
                if code == "Wolverhampton":
                    replace = "Wolves"
                if code == "Bilbao":
                    replace = "Club"
                elif code == "Nottm":
                    replace = "Nottingham"
                new_home_teams[i] = new_home_teams[i].replace(code, replace)
            if code in new_away_teams[i]:
                replace = ""
                if code == "Wolverhampton":
                    replace = "Wolves"
                elif code == "Nottm":
                    replace = "Nottingham"
                new_away_teams[i] = new_away_teams[i].replace(code, replace)
    return new_home_teams, new_away_teams, invalid_home_names, invalid_away_names

def fixture_id(team_id):
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    querystring = {"season":"2023","team":f"{team_id}","next":"1"}

    headers = {
        "X-RapidAPI-Key": "dc742b2619msh18622996d919c7fp148b94jsnff34cbfd9239",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()
    fixture = response["response"][0]["fixture"]["id"]
    print(fixture)
    return fixture


    
    

def team_averages(team):
    url = 'https://www.soccerstats.com/matches.asp?matchday=1&listing=1'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the fixtures
    table = soup.find('table', {'id': 'btable'})


    # Find the rows in the table
    rows = table.find_all('tr')

    # Loop through the rows and extract the fixtures and leagues
    for row in rows:
        cols = row.find_all('td')
        if cols:
            if cols[9].text == team or cols[11].text == team:
                home = [cols[4].text, cols[3].text]
                away = [cols[16].text, cols[17].text]
                return home, away

                
                
def league_stats(row_name):
    invalid = ["Portugal - Primeira Liga", "Turkey - Süper Lig", "Norway - 1. Division"]
    if row_name == invalid[0]:
        row_name = "Portugal - Liga Portugal"
    elif row_name == invalid[1]:
        row_name = "Turkey - Super Lig"
    elif row_name == invalid[2]:
        row_name = "Norway - 1st Division"
    url = "https://www.soccerstats.com/leagues.asp"

    # Send an HTTP GET request to fetch the web page content
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table containing the home and away stats
    table = soup.find("table", class_="sortable")

    # Iterate over each row in the table
    for row in table.find_all("tr"):
        # Find the data cells in the row
        cells = row.find_all("td")
        
        # Check if the row has home and away stats
        if len(cells) >= 10:
            # Extract the home and away stats from the cells
            league_name = cells[0].text.strip()
            if row_name == league_name:
                home_stats = cells[7].text.strip()
                away_stats = cells[8].text.strip()
                return home_stats, away_stats
            



def get_league_name(id):
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

    querystring = {"season":"2022","team":f"{id}","type":"league"}

    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": "dc742b2619msh18622996d919c7fp148b94jsnff34cbfd9239",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring).json()
        return "".join([response["response"][0]["country"]["name"], " - ", response["response"][0]["league"]["name"]])
    except IndexError:
        return ("Try again around 00:00 and it should work. This is when the API")
        quit()

def get_team_id(team_name):
    url = f"https://api-football-v1.p.rapidapi.com/v3/teams?search={team_name}"
    headers = {
        "X-RapidAPI-Key": "dc742b2619msh18622996d919c7fp148b94jsnff34cbfd9239",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers).json()
    try:
        team_id = response["response"][0]["team"]["id"]
        return team_id
    except IndexError as e:
        print(f"No team found for {team_name}", e)
        team_id = None
    except KeyError as e:
        return (f"Sorry Daily usage for API has been completed try again tomorrow. {e}")
        team_id = None

def triple_poisson(Gx):
    from numpy import mgrid, abs, sum, newaxis, unravel_index
    from scipy.stats import poisson
    home_gx, away_gx = Gx
    home_goals, away_goals = mgrid[0:15, 0:15]
    diff_goals = home_goals - away_goals
    home_prob = poisson.pmf(home_goals, home_gx)
    away_prob = poisson.pmf(away_goals, away_gx)
    diff_prob = poisson.pmf(diff_goals, abs(home_gx - away_gx))
    joint_prob = home_prob[:, :, newaxis] * away_prob[:, newaxis, :] * diff_prob[newaxis, :, :]
    joint_prob /= joint_prob.sum()
    
    most_likely_scoreline = f"{unravel_index(joint_prob.argmax(), joint_prob.shape)[0]}:{unravel_index(joint_prob.argmax(), joint_prob.shape)[1]}"
    most_likely_prob = round(joint_prob.max() * 100, 2)
    home_goals_exp = sum(joint_prob * home_goals[:, :, newaxis])
    away_goals_exp = sum(joint_prob * away_goals[:, :, newaxis])
    
    temp = most_likely_scoreline.split(":")
    upper_goals = float(temp[0]) + float(temp[1]) + 0.5
    exp_goals_str = f"Under {upper_goals:=.1f}"
    less_than_exp_goals_prob = sum(joint_prob[home_goals + away_goals < upper_goals])
    likely_of_under = round(less_than_exp_goals_prob.sum() * 100, 2)
    
    home_win_prob = joint_prob[home_goals > away_goals].sum()
    draw_prob = joint_prob[home_goals == away_goals].sum()
    away_win_prob = joint_prob[home_goals < away_goals].sum()
    
    winning_team = "Draw"
    winning_prob = 0
    
    if home_win_prob > draw_prob and home_win_prob > away_win_prob:
        winning_team, winning_prob = "Home", home_win_prob
    elif away_win_prob > draw_prob and away_win_prob > home_win_prob:
        winning_team, winning_prob = "Away", away_win_prob
    elif draw_prob > home_win_prob and draw_prob > away_win_prob:
        winning_team, winning_prob = "Draw", draw_prob
    
    winning_prob = round(winning_prob * 100, 2)
    total_prob = most_likely_prob + likely_of_under + winning_prob
    
    home_win_prob *= 100
    away_win_prob *= 100
    draw_prob *= 100
    
    output_bets = [winning_team, most_likely_scoreline, exp_goals_str]
    
    output_string = f"The game is predicted to be won by {winning_team} with a scoreline of {most_likely_scoreline}, " \
                f"with a probability of {winning_prob:.2f}%. The most likely scoreline is {most_likely_scoreline} " \
                f"with a probability of {most_likely_prob:.2f}%. Expected goals: {exp_goals_str} " \
                f"(Likelihood of under: {likely_of_under:.2f}%). Winning team: {winning_team} " \
                f"with a probability of {winning_prob:.2f}%. " \
                f"Team 1: {home_win_prob:.2f}%, Team 2: {away_win_prob:.2f}%, Draw: {draw_prob:.2f}%. " \
                f"Overall probability: {total_prob:.2f}%."

    
    return output_string, output_bets


def calculate_gx(home_team_avg, away_team_avg, league_avg):
    try:
        home_team_att = float(home_team_avg[0]) / float(league_avg[0])
        home_team_def = float(home_team_avg[1]) / float(league_avg[1])
        away_team_att = float(away_team_avg[0]) / float(league_avg[1])
        away_team_def = float(away_team_avg[1]) / float(league_avg[0])
        home_team_gx = home_team_att * away_team_def * float(league_avg[0])
        away_team_gx = away_team_att * home_team_def * float(league_avg[1])
        
        return [home_team_gx, away_team_gx]
    except ValueError:
        return ("Sorry today we don't have any signals")
        quit()


def main(search = None):
    if search == None:
        teams = team_names()
    else:
        teams = find_teams_names(search)
    teams_scraping = teams[:len(teams) // 2]
    fixtures = [(teams_scraping[0][i], teams_scraping[1][i]) for i in range(len(teams_scraping[0]))]
    teams_API = teams[len(teams)//2:]
    teams_API = teams_API[0] + teams_API[1]
    teams_scraping = teams_scraping[0] + teams_scraping[1]
    # print the resulting lists
    team_ids = []
    league_names = []
    league_avgs = []
    team_average = []
    for i in teams_scraping:
        #Gets Team's ID's
        team_ids.append(get_team_id(i))
    for i in range(0, len(teams_scraping)):
        #Gets league for each team based of team ID's
        league_names.append(get_league_name(team_ids[i]))
    count = 0
    #This reduces league names to half of the list as fixutres of team teams are in the same league MANC AN MANU are both EPL
    updates_league_names = []
    for i in range(0, int(len(league_names)/2)):
        if league_names[i] == league_names[i+int(len(league_names)/2)]:
            updates_league_names.append(league_names[i])
            count+=1
    ##This will change this into a list of dictionairys which contains home and away average data [[HG, HC], [AG, AC]], [[HG, HC], [AG, AC]]
    for i in range(int(len(teams_scraping)/2)):
        team_average.append(team_averages(teams_API[i]))
    ##This will get league averages for each fixture
    for i in updates_league_names:
        league_avgs.append(league_stats(i))
    gx_list = []
    for i, fixture in enumerate(fixtures):
        home_team, away_team = fixture
        home_team_avg, away_team_avg = team_average[i]
        league_avg = league_avgs[i]
        home_team_gx, away_team_gx = calculate_gx(home_team_avg, away_team_avg, league_avg)
        gx_list.append(home_team_gx)
        gx_list.append(away_team_gx)
    gx_list = [(gx_list[i], gx_list[i+1]) for i in range(0, len(gx_list), 2)]
    for i in range(len(gx_list)):
        strings = triple_poisson(gx_list[i])
        strings, bets = strings[0], strings[1]
        print(strings, bets)
        strings = str(fixtures[i]) + str(strings)
        return (strings)
    


print(main("Mallorca"))