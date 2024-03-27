import datetime
import pandas as pd

class Person:
    def __init__(self, name: str, year: int, gender: str, height: int, weight: float, exercise: float, bmr=None, tdee=None):
        self.name = name
        self.age = int(datetime.date.today().year) - year 
        self.gender = gender
        self.height = height
        self.weight = weight
        self.exercise = exercise
        
        # if the bmw is not known, calculate using Harris-Benedict formula
        if bmr is None:
            if gender == 'F':
                self.bmr = round(655 + (9.6 * weight) + (1.8 * height) - (4.7 * self.age))
            elif gender == 'M':
                self.bmr = round(66 + (13.7 * weight) + (5 * height) - (6.8 * self.age))
        else:
            self.bmr = bmr
        
        # if tdee is not known, calculate using the activity multiplier 
        if tdee is None:
            self.tdee = self.bmr * exercise
        else:
            self.tdee = tdee
            
class NutritionalTable:
    """ Create a class for storing the nutritional database """
    def __init__(self, dataframe):
        self.df = dataframe
        self.df.set_index('item', drop = True, inplace = True)
        
class Day:
    def __init__(self):
        self.meals = {}

    def adding_food(self, dictionary_food, nutritional_dataframe, meal_label):
        """Create a function which creates a dictionary for each meal"""
        
        # Create an empty dictionary which will contain info for each meal   
        food_data = {}
          
        for food, quantity in dictionary_food.items():
            # Create a list which will return the nutritional value of the food you'd like to eat, multiplied by the quantity of it starting from the nutritional db
            lista = [round(quantity * float(value), 2) for value in nutritional_dataframe.loc[food].iloc[3:-1].tolist()]
            # Append the quantity and the meal label on the list
            lista.insert(0, quantity)
            lista.append(meal_label)
            # Associate each food with its information
            food_data[food] = lista
            
        # Add to the meals method, the meal label, the food and its information
        self.meals[meal_label] = food_data
        
    def _calories_summary(self, df):
        """ Create a daily calories dataframe, multiplying each macronutrient for each unitary calory""" 
        lista = {}
        
        # For day
        for index in df.index:
            # Keep daily calories
            if index == 'Kcal':
                lista[index] = df[index]
            # Multiply daily fat by 9 and calories by 4
            elif index == 'Fat':
                lista[index] = df[index] * 9
            elif index == 'Carbs' or index == 'Proteins':
                lista[index] = df[index] * 4
            
        return lista
    
    def _check_proportions(self, daily):
        """ Discovering how macronutrients contribute to the daily kcal"""
        
        nutrient_values = self._calories_summary(daily)
        proportions = {}
        # For each nutrient, find the proportion with respect to total Kcalories
        for nutrient in ["Fat", "Carbs", "Proteins"]:
            proportions[nutrient] = '{:.0%}'.format((nutrient_values[nutrient] / nutrient_values["Kcal"]))
            
        proportions = pd.DataFrame.from_dict(proportions, orient = 'index', columns = ['Percentage'])
            
        return proportions
            
    def summary(self, verbose = False):
        """ Create a daily summary """

        self.day_summary = pd.DataFrame()
        
        for meal in self.meals:
            temp_df = pd.DataFrame.from_dict(self.meals[meal], orient = 'index', columns=['Quantity', 'Kcal', 'Fat', 'Sat_Fat', 'Carbs', 'Sugars', 'Fibers', 'Proteins', 'Salt', 'Meal'])
            self.day_summary = pd.concat([self.day_summary, temp_df], axis = 0)
        
        if verbose == True:
            
            self.daily_summary = self.day_summary.iloc[:,1:-1].sum()
            self.meal_summary = self.day_summary.groupby('Meal').sum().reindex(['breakfast', 'lunch', 'dinner'])
            self.calories_summary = self._check_proportions(self.daily_summary)
            
            return self.day_summary, self.daily_summary.to_frame().T, self.meal_summary, self.calories_summary	
        
            
        return self.day_summary