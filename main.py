from personalplan_cloud import Person, NutritionalTable, Day
from database_connection import import_nutritional_database

vincenzo = Person("Vincenzo", 1999, "M", 177, 83.5, 1.2)

nutritionaltable = NutritionalTable(import_nutritional_database()).df

daily_breakfast = {'skyr': 1, 'fette toast': 4, 'schocokreme': 50, 'chia' : 3}
monday_lunch = {'mix legumi': 200, 'olio evo' : 15}
monday_dinner = {'pasta': 50, 'olio evo' : 15, 'feta greca' : 1, 'verdurine': 240}

tuesday_lunch = {'mix legumi': 200, 'olio evo' : 15}
tuesday_dinner = {'bastoncini': 5, 'olio evo': 15, 'verdurine': 240}

wednesday_lunch = {'mix legumi': 100, 'pane integrale': 3, 'olio evo' : 15}
wednesday_dinner = {'tonno scatola': 2, 'olio evo': 15, 'verdurine': 240}

thursday_lunch = {'riso integrale': 120, 'olio evo': 15, 'uova': 3}
thursday_dinner = {'feta greca': 1, 'verdurine': 240}

friday_lunch = {'riso integrale': 100, 'salmone affumicato': 100, 'olio evo' : 15}

Monday = Day()
Monday.adding_food(daily_breakfast, nutritionaltable, 'breakfast')
Monday.adding_food(monday_lunch, nutritionaltable, 'lunch')
Monday.adding_food(monday_dinner, nutritionaltable, 'dinner')
      
Tuesday = Day()
Tuesday.adding_food(daily_breakfast, nutritionaltable, 'breakfast')
Tuesday.adding_food(tuesday_lunch, nutritionaltable, 'lunch')
Tuesday.adding_food(tuesday_dinner, nutritionaltable, 'dinner')

Wednesday = Day()
Wednesday.adding_food(daily_breakfast, nutritionaltable, 'breakfast')
Wednesday.adding_food(wednesday_lunch, nutritionaltable, 'lunch')
Wednesday.adding_food(wednesday_dinner, nutritionaltable, 'dinner')

Thursday = Day()
Thursday.adding_food(daily_breakfast, nutritionaltable, 'breakfast')
Thursday.adding_food(thursday_lunch, nutritionaltable, 'lunch')
Thursday.adding_food(thursday_dinner, nutritionaltable, 'dinner')