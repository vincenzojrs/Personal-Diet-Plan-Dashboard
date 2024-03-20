from personalplan_cloud import Person, NutritionalTable, Day
from nutritional_database_connection import import_nutritional_database

vincenzo = Person("Vincenzo", 1999, "M", 177, 83.5, 1.2)

nutritionaltable = NutritionalTable(import_nutritional_database()).df

daily_breakfast = {'skyr': 1, 'fette toast': 4, 'schocokreme': 50}
monday_lunch = {'mix legumi': 200, 'olio evo' : 15}
monday_dinner = {'pasta': 100, 'olio evo' : 20, 'feta greca' : 1}

tuesday_lunch = {}
tuesday_dinner = {}

wednesday_lunch = {}
wednesday_dinner = {}

thursday_lunch = {}
thursday_dinner = {}

friday_lunch = {}
friday_dinner = {}

saturday_lunch = {}
saturday_dinner = {}

sunday_lunch = {}
sunday_dinner = {}

Monday = Day()
Monday.adding_food(daily_breakfast, nutritionaltable, 'breakfast')
Monday.adding_food(monday_lunch, nutritionaltable, 'lunch')
Monday.adding_food(monday_dinner, nutritionaltable, 'dinner')
Monday.summary()