# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "Cadeau", "Trimble", "Washington", "Tyson", "Jackson", "Claude", "Brown", "Withers"],
          "First Name": ["Armando", "RJ", "Elliot", "Seth", "Jalen", "Cade","Ian", "Ty", "James", "Jaelyn"],
          "height": [83, 72, 73, 75, 82, 79, 76, 79, 82, 81],
          "weight": [240,180,180,195,235,200,190,230,215,220]
}
data = pd.DataFrame(player)

# bmi = weight in kg / height in meter squared
data["bmi"] = ((data["weight"]/2.205)/((data["height"]/39.37)**2)).round(2)

print(data)

data.to_csv("bmi.csv")