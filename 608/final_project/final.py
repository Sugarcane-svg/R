import pandas as pd
import streamlit as st
import plotly.express as px

# my approach
# 1. display table in the web
# 2. graph with distribution of genre
# 3. show relationship between domestic sales and international sales
# 4. show plot with user selection of the distribution of distributor



# header
st.header("608 FINAL PROJECT")
st.text('by Jie Zou')

# data title
st.subheader("Display Data")
st.text('Highest Holywood Grossing Movies Dataset')

# read data from csv file
data = pd.read_csv("https://raw.githubusercontent.com/Sugarcane-svg/R/main/608/final_project/Highest_Holywood_Grossing_Movies.csv", index_col=0)

# 1. display data in website
st.dataframe(data)

# add line break
st.markdown("***")

# *******
# 2. distribution of genres
# 
# split data
genres = []
gross_type = []
gross = []

for i in data["Genre"]:

    # split genre into individuals and store them
    temp = i.strip().replace("[", "").replace("'", "").replace("]","").split(", ")
    # print(temp)
    z = 0
    for j in temp:
        genres.append(j)
        genres.append(j)
        gross_type.append('domestic')
        gross_type.append('internaltional')
        gross.append(data['Domestic Sales (in $)'][z])
        gross.append(data['International Sales (in $)'][z])
        z += 1

# create data frames
genre_df = pd.DataFrame(index=range(len(genres)), columns = ['genre', 'gross_type', 'sales'])

# assign column value
genre_df['genre'] = genres
genre_df['gross_type'] = gross_type
genre_df['sales'] = gross

# display the distribution of genres
st.subheader('Distribution of genres')

for_distribution = genre_df.groupby(['genre', 'gross_type']).count().reset_index()

fig = px.bar(
    data_frame=for_distribution.sort_values(by='sales', ascending = False), 
    x = "genre", 
    y = 'sales',
    labels = {
        'sales' : 'number of movies'
    }
)

st.plotly_chart(fig)

# 3. display the relationship between domestic sale and international sale
st.markdown("***")
st.subheader("Difference Between Domestic Sales and International Sales")

view = st.radio(
    "Select a view you like",
    ('Full View', 'Individual View')
)
if view == 'Full View':
    f = pd.DataFrame(genre_df.groupby(['genre','gross_type']).sum()['sales']/genre_df.groupby('genre').sum()['sales']).reset_index()

    fig2 = px.bar(
        f, 
        x = 'genre', 
        y = 'sales', 
        color = 'gross_type',
        labels = {
            'sales' : 'genre sales ratio'
        },
        title = "Domestic sales VS international sales in %"
    )

    st.plotly_chart(fig2)
else:
    option = st.selectbox(
    'Pick a genre you like to see its sales',
    (set(genres)))

    relation = genre_df.groupby(['genre', 'gross_type']).sum().reset_index().set_index('genre').filter(like=option, axis = 0)

    fig2 = px.bar(
        data_frame=relation, 
        x = relation.index, 
        y = "sales", 
        color='gross_type', 
        barmode='group',
        text ="sales",
        title = "Domestic sale VS international sales in $"
    )

    st.plotly_chart(fig2)

# 4. distributio of distributor

# check if distributor is unique
st.markdown("***")
st.subheader("Distribution of Distributors")

# check if each row contains only one distributor
def is_unique():
    for i in range(len(data)):
        if len(data.filter(items=['Distributor']).iloc[i,0].split(","))!=1:
            return False
    return True

print(str(is_unique()))

# radio2
# general distributor data
distributor = data[['Title','Distributor']]
# make data frame with count
d_general = distributor.groupby(['Distributor']).count().sort_values(by="Title", ascending= False).reset_index()

# advanced distributor data
# generate list with title, distributor and genre
distri = []
gen = []
tle = []
genre_set = set(genres)
set_length = len(genre_set)
for i in range(set_length):
    elem = genre_set.pop()
    for j in range(len(data)):
        if data['Genre'][j].find(elem) != -1:
            gen.append(elem)
            distri.append(data['Distributor'][j])
            tle.append(data['Title'][j])
del genre_set

# create data frame
gen_dist = pd.DataFrame(index = range(len(distri)))
gen_dist['genre'] = gen
gen_dist['distributor'] = distri
gen_dist['title'] = tle

t = gen_dist.groupby(['distributor', 'genre']).count().reset_index()


view2 = st.radio("Select the view you like", ('General View', 'Genre View'))

if view2 == 'General View':

    fig3 = px.bar(
        d_general, 
        x = 'Distributor', 
        y = 'Title',
        labels = {
            "Title": "number of movies distributed"
        },
        title = "Distribution of Distributors"
    )

    st.plotly_chart(fig3)
else:
    selected = st.selectbox("Select a distributor to see the distribution by genre", (set(data['Distributor'])))

    fig3 = px.histogram(
        t[t["distributor"] == selected],
        x = "genre",
        y = 'title', 
        barmode = 'group',
        labels = {
            "title":'number of movies distributed'
        },
        title = "Distribution of genres(by distributors)"
    )
    st.plotly_chart(fig3)

