
# Demograviz - A Streamlit Population Analysis App


## Overview
Demograviz provides a comprehensive analysis of population data for Canada. Users can explore population trends over different quarters and years, compare locations, and gain insights into demographic changes. The application offers interactive visualizations and a user-friendly interface for a seamless experience.

## Try Out My Application
Visit [https://demograviz.onrender.com/](https://demograviz.onrender.com/) to try out Demograviz!

## Features

- **Quarterly Population Analysis:** Explore population changes over different quarters.
- **Yearly Trends:** Analyze population trends over the years.
- **Location Comparison:** Compare population data for different locations.
- **Visualizations:** Interactive charts for a better understanding of demographic changes.

## Prerequisites

- Python 3.6 or later
- Install dependencies:

```bash
  pip install -r requirements.txt
```

## Usage
1. Run the Streamlit application:
```python
streamlit run app.py
```
2. Open your browser and navigate to https://demograviz.onrender.com/ to interact with the application.


## File Overview in Demograviz
- #### app.py:
This Python script serves as the main application file. It contains the code for the Streamlit application, defining the user interface, data processing, and visualization logic. The application allows users to analyze and explore population trends in Canada.

- #### quarterly_canada_population.csv,:
This CSV file contains the dataset used by the application. It includes quarterly population data for Canada, with columns such as "Quarter," "Year," and demographic information. The application uses this data for analysis and dynamic visualizations.

- #### requirements.txt:
This file lists the Python dependencies required to run the application. Use the following command to install the dependencies:
```bash
  pip install -r requirements.txt
```


## Acknowledgments
- Data source: [Statistics Canada](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901)
- Streamlit: [Streamlit Documentation](https://docs.streamlit.io/)
- Matplotlib: [Matplotlib Documentation](https://matplotlib.org/stable/index.html)

