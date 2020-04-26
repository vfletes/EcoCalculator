def main():
  print('Welcome to the Ecological Calculator by Victoria Fletes')
  animal = input("How often do you eat animal-based products? 4 being very often and 0 being never: ")
  miles = input('How far do you travel by car each week? 4 being being 800 miles and 0 being 0 miles: ')
  fuel = input('What is your average fuel economy? 4 being 10 mpg and 0 being 100+ mpg: ')
  carpool = input('When you travel by car how often do you carpool? 4 being very often and 0 being never: ')
  public = input('How far do you travel on public transportation each week? 4 being 500 miles and 0 being 0 miles: ')
  flight = input('How many hours do you fly each year? 4 being 100+ hours and 0 being 0 hours: ')
  thrift = input('How often do you buy from a thrift store? 4 being very often and 0 being never: ')
  clothes = input('How often do you buy new clothes not from second hand shops? 4 being very often and 0 being never: ')
  score = int(animal) + int(miles) + int(fuel) + int(carpool) + int(public) + int(flight) + int(thrift) + int(clothes)
  if score == 0:
    print("Great job you got an A on your environmental impact!")
  elif score <= 8 and score >= 1:
    print("Great job you got a B on your environmental impact!")
  elif score <= 15 and score >= 9:
    print("You got a C on your environmental impact, might want to make some adjustments, but great start!")
  elif score <= 23 and score >= 16:
    print("You got a D on your environmental impact, might want to make some adjustments")
  elif score < 32 and score >= 24:
    print("You got an F on your environmental impact, might want to make some adjustments")
