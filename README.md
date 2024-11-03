# Housing factor
**Your gateway to smart real estate investing**

## Objective 🎯

We focus on collecting information both on the characteristics of housing in our country, through real estate portals, as well as social and cadastral data through official sources.

## Functionality ⚙️

- 🧹 **Data Cleaning**: Process raw data to remove inconsistencies and prepare it for analysis.
- 📈 **Data Visualization**: Create visual representations of the data to identify trends and patterns.
- 📝 **Reporting**: Generate summary reports and figures to present findings.

## Tools Used 🛠️

- 🐍 **Python**: Main programming language used for data processing and analysis.
- 🐼 **Pandas**: Library for data manipulation and analysis.
- 📊 **Matplotlib & Seaborn**: Libraries for data visualization.
- 📓 **Jupyter Notebooks**: Interactive environment for data cleaning and visualization.
- 🌐 **Git**: Version control system for tracking changes and collaboration.

## Development Process 🚀

1. 📥 **Data Collection**: Web Scaping from Idealista Web and Oficial data from INE, IGN, SS and SEPE.
2. 🧹 **Data Cleaning**: Drop duplicates, nan values and integrate all data frame. 
3. 🔍 **Data Analysis**: The main objective of our analysis was to find the best real estate investement among the twenty most poblated towns in Spain, which the following stand out *Barcelona, Madrid, Sevilla, Granada, Córdoba, Las Palmas de Gran Canaria, Elche*. 
4. 📊 **Data Visualization**: We have done differents graffics with the objective to understand our data. We can hightlight some bar charts which represent the quantity of houses offers (rent and sell) against how the popultation live in these towns (renting or in ownership). Also, there are some graphs which represents the gross housing profitability.
5. 📝 **Reporting**

## Results 📊



## Summary Report 📄



## Project Structure 📁

- `files/`: 
    - `csv/`: 
- `graficos/`: 

- `src/`: 
  - `files/datos_para_almacenar/`: Folder to data frame after cleaning process.
    - `datos_limpios.csv`: final data frame.
  - `visualization/`: Folder to store Jupyter Notebooks for data visualization.
  - `clenaning_functions.py`: Python script with utility functions.
  - `clean_df.ipynb`: Jupyter Notebooks where data frame is cleaning.
  - `dataframe_ciudades.ipynb`: Jupyter Notebooks where oficials data frame is cleaning, for example Tenencia.csv
  - `idealista.ipynb`: Jupyther Notebooks where the web scraping process takes place for homes for purchase.
  - `idealista_alquiler.ipynb`: Jupyther Notebooks where the web scraping process for rental housing takes place.
- `presentation/`: 
  - `PDF_presentation/`: Folder to store PDF presentations.

- `.gitignore`: File to specify intentionally untracked files to ignore.
- `README.md`: File to describe the project and how to set it up.
- `requirements.txt`: File to list the project dependencies.

## Project Presentation 🎤

The project findings were presented in a detailed canva presentation, which includes:
- 📋 An overview of the data analysis process.
- 🔍 Key insights and visualizations.
- 📊 Recommendations based on the findings.




## Project Members 👥

| Name       | GitHub Profile                           |
|------------|------------------------------------------|
| **Bruno** | [GitHub Profile](https://github.com/member1) |
| **Carlota Gordillo** | [GitHub Profile](https://github.com/carlotagordillo2) |
| **Javier Mora** | [GitHub Profile](https://github.com/jmorsal) |
