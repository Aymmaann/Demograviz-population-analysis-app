import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("quarterly_canada_population.csv")

st.header("Population of Canada")
st.write("Source table can be found [here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901)")

with st.expander("See full data table"):
    st.dataframe(data)

with st.form(key="Population data"):
    col1, col2, col3 = st.columns(3)

    col1.write("Choose a starting date")
    col1_quarter = col1.selectbox("Quarter", options=["Q1","Q2","Q3","Q4"], key="col_1_quarter_widget")
    col1_year = col1.slider("Year", min_value=1991, max_value=2023, key="col_1_year_widget")

    col2.write("Choose an end date")
    col2_quarter = col2.selectbox("Quarter", options=["Q1", "Q2", "Q3", "Q4"], key="col_2_quarter_widget")
    col2_year = col2.slider("Year", min_value=1991, max_value=2023, key="col_2_year_widget", value=2023)

    col3.write("Choose a location")
    location = col3.selectbox("Choose a location", options=data.columns[1:])

    button = st.form_submit_button("Analyze")

outcome = True
if button:
    quarter_years = [f"{col1_quarter} {col1_year}", f"{col2_quarter} {col2_year}"]
    outcome = all(quarter_year in data['Quarter'].values for quarter_year in quarter_years)
    if not outcome:
        st.warning(f"No data available. Check your quarter and year selection.")

    if col1_year > col2_year:
        st.warning(f"Dates don't work. Start date must come before end date.")
        outcome = False


# tabs
if outcome:
    tab1, tab2 = st.tabs(["Population change", "Compare"])

    with tab1:
        st.subheader(f"Population change from {col1_quarter} {col1_year} to {col2_quarter} {col2_year}")
        col1, col2 = st.columns(2)

        old_value = data.loc[data["Quarter"] == f"{col1_quarter} {col1_year}", location].iloc[0]
        new_value = data.loc[data["Quarter"] == f"{col2_quarter} {col2_year}", location].iloc[0]
        percent = ((new_value - old_value) / old_value) * 100
        col1_1991 = col1.metric(f"{col1_quarter} {col1_year}", value=data.loc[data["Quarter"] == "Q3 1991", location])
        col1_2023 = col1.metric(f"{col2_quarter} {col2_year}", value=data.loc[data["Quarter"] == "Q1 2023", location],
                                delta=f"{round(percent, 2)}%")

        fig, ax = plt.subplots()
        ax.plot(data.Quarter, data[location])
        ax.set_xlabel("Time")
        ax.set_ylabel("Population")
        x_labels = ['Q3 1991', 'Q1 2023']
        ax.set_xticks(data[data['Quarter'].isin(x_labels)]['Quarter'])
        ax.set_xticklabels(x_labels)
        fig.autofmt_xdate()
        col2.pyplot(fig)

    with tab2:
        selection = st.multiselect("Choose other locations", options=data.columns[1:], default="Canada")
        fig, ax = plt.subplots()
        ax.plot(data.Quarter, data[selection])
        ax.set_xlabel("Time")
        ax.set_ylabel("Population")
        x_labels = ['Q3 1991', 'Q1 2023']
        ax.set_xticks(data[data['Quarter'].isin(x_labels)]['Quarter'])
        ax.set_xticklabels(x_labels)
        fig.autofmt_xdate()
        st.pyplot(fig)