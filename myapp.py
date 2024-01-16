import seaborn as sns
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
tips['time_order'] = pd.date_range(start='2023-01-01', end='2023-01-31', periods=len(tips))
sort_date = tips.groupby(tips['time_order'].dt.date)[['tip','total_bill']].sum().reset_index()


st.sidebar.title(':orange[Графики Steamlit-а]')

st.title('Выбранный график')

st.sidebar.button("Выбрать другой график", type="primary")
if st.sidebar.button('**Линейный** график показывающий динамику чаевых во времени'):
    st.line_chart(data = sort_date, x = 'time_order' , y = 'tip')
    
elif st.sidebar.button('**Гистограмма** общей выручки по дате'):
    sort_bill = tips.groupby(tips['time_order'].dt.date)['total_bill'].sum().reset_index()
    st.bar_chart(data= sort_bill, x ='time_order' , y = 'total_bill') 
    
elif st.sidebar.button('**Scatterplot**, показывающий связь между total_bill и tip'):
    st.scatter_chart(data=sort_date , x='total_bill' , y='tip')
    
elif st.sidebar.button('**Scatterplot** связывающий total_bill, tip, и size'):
    st.scatter_chart(data=tips, x='total_bill', y='tip', color = ['#00ff00'] , size='size')
    
elif st.sidebar.button('График отражающий связь между днем недели и размером счета'):
    sort_day = tips.groupby(tips['day'])[['total_bill','tip',]].sum().reset_index()
    st.bar_chart(data= sort_day , x = 'day' , y = 'total_bill' , color= 'day')
    
elif st.sidebar.button('**Scatter plot** с днем недели по оси **Y**, чаевыми по оси **X**'):
    st.scatter_chart(data=tips, x='day', y='tip', color = 'sex')

elif st.sidebar.button('**Box plot** c суммой всех счетов за каждый день'):
    fig = plt.figure(figsize=(10, 10))
    ax = sns.boxplot(data= tips , x= 'day' , y = 'total_bill' , hue='time')
    ax.set(xlabel = ' День' , ylabel = 'сумма счета');
    st.pyplot(fig)
    
elif st.sidebar.button('**Гистограммы** чаевых на обед и ланч'):
    fig2 = ax = sns.displot(data = tips, x = 'tip' , col = 'time')
    ax.set(xlabel = 'чай' , ylabel = 'Кол - во чая');
    st.pyplot(fig2)
    
elif st.sidebar.button('Scatter plot связь размера счета и чаевых, c разбивкой по курящим/некурящим.'):
    fig3 =ax = sns.relplot(data = tips , x = 'tip', y = 'total_bill' , col = 'sex' , hue = 'smoker')
    ax.set(xlabel = 'Сумма чая', ylabel = 'Сумма счета');
    st.pyplot(fig3)

elif st.sidebar.button('Тепловая карта зависимостей численных переменных.'):
    temp_map = tips.select_dtypes(include='number').corr()
    fig4, ax = plt.subplots()
    sns.heatmap(temp_map, annot=True, cmap='YlGnBu');
    st.pyplot(fig4)

    
st.sidebar.markdown("Загрузить ипользуемый [csv файл](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv).")
    