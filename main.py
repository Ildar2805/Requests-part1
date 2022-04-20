from pprint import pprint
import requests
import operator

def find_superhero(heroes):
        list = {}
        for hero in heroes:
            url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
            response = requests.get(url)
            char = response.json()
            list[hero] = int(char['results'][0]['powerstats']['intelligence'])
        return list
def the_highest_intelligence():
    sorted_list = sorted(find_superhero(superhero_list).items(), key=operator.itemgetter(1))
    print(f'Самый умный: {sorted_list[-1][0]}')
if __name__ == '__main__':
    superhero_list = ['Hulk', 'Captain America', 'Thanos']
    the_highest_intelligence()