import streamlit as st
from authentication import logout_button, create_form
import pandas as pd
import base64

class Webpage:
    def _page_config(self):
        st.set_page_config(layout = 'wide', page_title = 'Enzo devi dimagrire', page_icon = ':pig:')
        st.title('Summary')
        create_form()
        logout_button()

    def _page_data(self):
        from main import Monday, Tuesday, Wednesday
        weekdays = ((Monday, 'monday'), (Tuesday, 'tuesday'), (Wednesday, 'wednesday'))
        
        daily_meals_in_short = pd.DataFrame()
        daily_nutrients = pd.DataFrame()
        daily_proportions = pd.DataFrame()
        
        for day, day_str in weekdays:
            daily_df = day.summary(verbose=True)[0].iloc[:, [0, -1]].copy()  # Make a copy to avoid SettingWithCopyWarning
            daily_df.loc[:, 'weekday'] = day_str  # Use .loc to set the value
            daily_meals_in_short = pd.concat([daily_meals_in_short, daily_df], axis=0)

            daily_nutrients = pd.concat([daily_nutrients, day.summary(verbose = True)[1]], axis = 0)
            daily_proportions = pd.concat([daily_proportions, day.summary(verbose = True)[-1].T], axis = 0)
            daily_proportions = daily_proportions.replace('%', '', regex=True).astype(float)
        
        return daily_meals_in_short, daily_nutrients.mean().to_frame().T, daily_proportions.mean().to_frame().T

    def _page_content(self):
        def _coloring(day):
            if day == 'monday':
                color = 'green'
            elif day == 'tuesday':
                color = ''
            elif day == 'wednesday':
                color = '#800000'
            elif day == 'thursday':
                color = ''
            elif day == 'friday':
                color = 'green'
            elif day == 'saturday':
                color = ''
            elif day == 'sunday':
                color = '#800000'
            return f'background-color: {color}'
        
        def _st_csv_download_button(dataframe):
            csv = dataframe.to_csv(index=False) #if no filename is given, a string is returned
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)  

        daily_meals_in_short, daily_nutrients, daily_proportions = self._page_data()
        st.header('My diet, in short')
        st.dataframe(daily_meals_in_short.reset_index(drop = False).style.apply(lambda x: [_coloring(x['weekday'])]*len(x), axis=1), use_container_width = True)
        _st_csv_download_button(daily_meals_in_short.reset_index(drop = False))
        st.header('Average daily nutrients')
        st.dataframe(daily_nutrients, use_container_width = True)
        st.header('Average daily kcals contribution per macronutrient, in percentage')
        st.dataframe(daily_proportions, use_container_width = True)
   
    def __init__(self):
        self._page_config()
        self._page_content()

webpage = Webpage()