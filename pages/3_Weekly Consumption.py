import streamlit as st
from database_connection import connect_nutritional_database
import pandas as pd
from authentication import logout_button, create_form

class Week_Consumption:
    def _weekly_consumption(self):
        from main import Monday, Tuesday
        """ For each day of the week, for each meal, count the quantity of food"""
        weekly_food = {}
        days = [Monday, Tuesday]

        # Iterate over days
        for day in days:
            # Iterate over meals
            for meal in day.meals:
                # Iterate over food
                for food in day.meals[meal]:
                    # If the food is already in the collection as a key, add the quantity to the related value
                    if food in weekly_food:
                        weekly_food[food] += day.meals[meal][food][0]
                    # Else, add a new key-value pair
                    else:
                        weekly_food[food] = day.meals[meal][food][0]
                        
        # Generate a dataframe
        weekly_food = pd.DataFrame.from_dict(weekly_food, orient = 'index', columns = ['quantity'])
        
        return weekly_food
    
    def _retrieve_info(self):
        """Retrieve item name, gr/pack, quantity per pack and price per pack"""
        info = connect_nutritional_database().iloc[:, [0, 3, -1]]
        return info
    
    def _weekly_consumption_and_unit_expense(self, weekly_consumption, info):
        """Join the weekly consumption dataframe with the info related to each food"""
        df = pd.merge(weekly_consumption, info, left_index=True, right_on='item', how='left').reset_index(drop = True).loc[:,["item", "quantity", "gr/pack", "price_per_pack"]]
        return df

    def _to_be_bougth_and_total_expense(self):
        """Calculate the quantity to be bought and the weekly expense"""
        df = self._weekly_consumption_and_unit_expense(self._weekly_consumption(), self._retrieve_info())

        # The quantity to be bought is 1, if the quantity per pack > weekly quantity, else the quantity of packs to fill the weekly consumption
        df['quantity_to_be_bought'] = df.apply(lambda row: 1 if row['gr/pack'] >= row['quantity'] else math.ceil(row['quantity'] / row['gr/pack']), axis=1)
        df['weekly_expense'] = df['quantity_to_be_bought'] * df['price_per_pack']
        return df
    
    def __init__(self):
        self.df = self._to_be_bougth_and_total_expense()

class Webpage:
    def _page_config(self):
        st.set_page_config(layout='wide')
        st.title('Weekly Consumption and Expense')
        st.header('The quantity to be bought for each food, weekly')
        create_form()
        logout_button()

    def _page_content(self):
        weekly_consumption = Week_Consumption().df.iloc[:,[0, -2, -1]]
        st.dataframe(weekly_consumption, use_container_width = True)
        st.write("Each week you spend {}€ for groceries :smile:".format(weekly_consumption['weekly_expense'].sum()))

    def __init__(self):
        self._page_config()
        self._page_content()

webpage = Webpage()
