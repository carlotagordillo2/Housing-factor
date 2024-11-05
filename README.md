# Housing factor
**Your gateway to smart real estate investing**

## Objective 🎯

We aim to provide insights into Spain's real estate market by gathering and analyzing housing data from multiple sources. Using real estate portal data and official social and cadastral records, we deliver a data-driven foundation for making informed investment decisions.

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
hrough our analysis, we identified several key insights:

- **High Demand, Limited Supply**: Major cities like Madrid, Barcelona, Seville, and Málaga exhibit high Social Security affiliation rates but have limited housing availability. This suggests a supply-demand imbalance, making these cities potential targets for new housing developments.
  
- **University-Driven Rental Demand**: Cities with large student populations, such as Granada and Madrid, show a high demand for rentals, particularly for 1- and 2-bedroom apartments. Expanding rental options in these areas, especially for student-friendly housing, would be beneficial.

- **Tourist Influence on Housing Prices**: Tourist-heavy cities like Palma, Las Palmas, and Alicante show greater variability in rental prices and higher average prices. This trend aligns with seasonal rental demand and points to strong investment potential in short-term rental properties.

- **Profitability Analysis**:
  - *L’Hospitalet de Llobregat* stands out with a profitability rate exceeding 6%, making it a prime location for rental investment near Barcelona.
  - *Elche*, while profitable, may not be ideal for investment due to its high ownership rates and lower population density.

- **Potential for Luxury Market Expansion**: Las Palmas and other tourist destinations have shown promise for luxury real estate investments, especially properties with beachfront access and high-end amenities.


## Summary Report 📄

Our summary report highlights the following:

1. **Top Investment Cities**: Based on profitability and demand metrics, our top cities for investment are:
   - **L’Hospitalet de Llobregat**: High profitability and demand due to proximity to Barcelona.
   - **Madrid & Barcelona**: Although dense, these cities still show a housing supply shortage, with high profitability in certain sectors.
   - **Granada**: Significant student-driven rental demand, especially for 3-room units, with limited availability of larger units.
   - **Las Palmas**: Luxury tourism potential and diverse room offerings make it a strategic choice for high-end housing.

2. **Rental Market Opportunities**: 
   - Increased demand for single-room apartments in urban centers such as Madrid and Barcelona.
   - University cities like Granada would benefit from additional 3- and 4-room rental units.

3. **Tourism-Related Investment**:
   - Cities with high seasonal rental demand, including Palma, Las Palmas, and Alicante, present strong opportunities for short-term rental investments.

4. **Next Steps for Enhanced Analysis**:
   - Further study of neighborhood-level demand within each municipality, using INE and other official sources.
   - Assess availability of local amenities (e.g., hospitals, schools) to gauge quality of life and appeal for residents.
   - Investigate the supply-demand balance for luxury housing in popular tourist areas.



## Project Structure 📁

- `files/`: 
    - `csv/`: Folder to keep oficial data such as *Año de construcción.csv*.
    - `viviendas_idealista.csv`: data frame with the result of web scraping for purchase housing.
    - `viviendas_idealista_alquiler.csv`: data frame with the result of web scraping for renting housing.
- `graficos/`: Folder with all grahps creates to analyse. All of them have been created in `visualization_df.ipynb` Jupyter Notebook.
- `src/`: 
  - `files/datos_para_almacenar/`: Folder to data frame after cleaning process.
    - `datos_limpios.csv`: final data frame.
  - `visualization/`: Folder to store Jupyter Notebooks for data visualization.
     - `visualization_df.ipynb` : Jupyter Notebook with the visualization process. 
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
- `report.rd`: This file contains a extend explanation about the project.

## Project Presentation 🎤

The project findings were presented in a detailed Canva presentation, which includes:
- 📋 An overview of the data analysis process.
- 🔍 Key insights and visualizations.
- 📊 Recommendations based on the findings.




## Project Members 👥

| Name       | GitHub Profile                           |
|------------|------------------------------------------|
| **Bruno** | [GitHub Profile](https://github.com/member1) |
| **Carlota Gordillo** | [GitHub Profile](https://github.com/carlotagordillo2) |
| **Javier Mora** | [GitHub Profile](https://github.com/jmorsal) |
----

Feel free to reach out for any questions or suggestions!
