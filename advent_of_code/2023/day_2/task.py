import re

games = []
gamesPowers = []

# 12 red, 13 green, 14 blue

id = 1

with open("input.txt", mode="r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        game = line.split(":")
        sets = game[1].split(";")
        colors = {
            "green": 0,
            "red": 0,
            "blue": 0
        }
        for set in sets:
            data = set.split(",")
            for nums in data:
                filtered = re.sub("[^0-9]", "", nums)
                if "green" in nums:
                    if colors["green"] < int(filtered):
                        colors["green"] = int(filtered)
                elif "red" in nums:
                    if colors["red"] < int(filtered):
                        colors["red"] = int(filtered)
                else:
                    if colors["blue"] < int(filtered):
                        colors["blue"] = int(filtered)
        
        if colors["red"] <= 12 and colors["blue"] <= 14 and colors["green"] <= 13:
            games.append(id)
        id += 1
        pow = 1
        for key in colors.keys():
            pow = pow * colors[key]
        gamesPowers.append(pow)
    file.close()

print(sum(games))
print(sum(gamesPowers))





