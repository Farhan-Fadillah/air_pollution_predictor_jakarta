# Jakarta's Air Polution Predictor App : An Alert for all
Jakarta, as the capital city of Indonesia, is one of the most densely populated urban areas in Southeast Asia. Rapid urbanization, industrial growth, and increasing vehicular traffic have significantly contributed to deteriorating air quality in the region. Air pollution poses a serious threat to public health, the environment, and overall quality of life.

![jakarta](https://github.com/Farhan-Fadillah/picture_list/blob/039fc4643af941893e8a1d941898c15c35384295/jakarta.jpg)

Despite efforts to monitor air quality, the dynamic and complex nature of pollution sources makes it challenging to predict pollution levels accurately and in a timely manner. This creates a critical need for advanced predictive tools that can forecast air pollution trends, enabling proactive measures to mitigate adverse effects.

![jakarta_pollution](https://github.com/Farhan-Fadillah/picture_list/blob/cda28029919fff8c235c864126960aac5f54eb5b/jakarta%20air%20polution.jpg)

The development of a machine learning-based air pollution prediction system for Jakarta aims to address this gap by leveraging historical data, environmental factors, and advanced algorithms to provide accurate, real-time forecasts of air pollution levels.

# What's the benefit of this project?
a. Proactive Public Health Protection
  - Early warnings about high pollution levels allow residents, especially vulnerable groups such as children, elderly, and those with
    respiratory conditions, to take precautionary actions.
  - Helps healthcare providers prepare for potential increases in pollution-related illnesses.

b. Informed Policy and Decision Making
  - Enables government agencies and environmental authorities to implement timely interventions, such as traffic restrictions or industrial regulations, based on
    predicted pollution spikes.
  - Supports urban planning and environmental management strategies to reduce pollution sources.
    
c. Community Awareness and Engagement
  - Provides accessible and understandable pollution forecasts to the public, raising awareness about air quality issues.
  - Encourages behavioral changes, such as reducing outdoor activities during high pollution periods or using cleaner transportation options.

d. Technological Advancement
  - Demonstrates the application of machine learning and data science in environmental monitoring.
  - Opens pathways for integrating real-time sensor data, IoT devices, and smart city initiatives.

# Importance and Impact on Environment and Society
Environmental Impact
  - Reduction of Pollution Sources: Predictive insights can guide targeted actions to reduce emissions from traffic, industry, and other sources.
  - Sustainable Urban Development: Supports the creation of greener, healthier urban environments by informing policies that balance growth with environmental
    preservation.
  - Climate Change Mitigation: Improved air quality contributes to reducing greenhouse gases and other pollutants that exacerbate climate change.

Societal Impact
  - Improved Public Health: Lower exposure to harmful pollutants reduces respiratory and cardiovascular diseases, improving overall community health.
  - Economic Benefits: Reducing pollution-related health issues decreases healthcare costs and productivity losses.
  - Enhanced Quality of Life: Cleaner air contributes to better living conditions, making Jakarta a more attractive city for residents and businesses.

# SUMMARY
![summary](https://github.com/Farhan-Fadillah/picture_list/blob/cda28029919fff8c235c864126960aac5f54eb5b/TABLE%20ASPECT%20POLUTION%20APP.png)
The air pollution prediction project for Jakarta is a crucial initiative that combines cutting-edge machine learning technology with environmental science to tackle one of the city’s most pressing challenges. By providing accurate forecasts, it empowers policymakers, healthcare providers, and the public to take informed actions that protect health, preserve the environment, and enhance the quality of life.

# 🌫️ Jakarta Air Pollution Predictor App

A machine learning-powered web application built using **Streamlit** that predicts air pollution levels (Air Quality Index – AQI) across Jakarta for up to 7 days into the future. It uses a trained `RandomForestRegressor` model, provides health-based recommendations, and visualizes results on an interactive Jakarta map.

---

## Project Overview

- **Model**: RandomForestRegressor
- **Interface**: Streamlit Web App
- **Visualization**: Folium Map (via `streamlit_folium`)
- **Regions Covered**: Jakarta Pusat, Utara, Barat, Selatan, Timur
- **Prediction Horizon**: 0 to 7 days from today

---

## Why RandomForestRegressor?

`RandomForestRegressor` is chosen for this project because:

- ✅ **Handles non-linear data well**: Air pollution depends on multiple environmental variables that may not follow a linear pattern.
- ✅ **Robust to overfitting**: By combining many decision trees, the model generalizes better to unseen data.
- ✅ **Performs well with limited data**: Suitable for moderate-sized datasets like our Jakarta air pollution data.
- ✅ **Built-in feature importance**: Helps understand which features (temperature, humidity, date) most affect predictions.
- ✅ **Minimal preprocessing required**: Unlike linear models, it doesn’t require normalization or strong assumptions.

---

## How RandomForestRegressor Works

RandomForestRegressor is an **ensemble learning algorithm** that builds multiple decision trees during training and outputs the **average of their predictions**.

### Step-by-step process:
1. The dataset is bootstrapped (sampled with replacement) multiple times.
2. A decision tree is trained on each bootstrapped subset.
3. At each split in a tree, only a random subset of features is considered, increasing diversity among trees.
4. During prediction, each tree gives a prediction.
5. The final prediction is the **mean of all individual tree predictions**.

This results in a **more stable and accurate** prediction than a single decision tree.

---

## Machine Learning Details

- **Features**:
  - `Suhu` (Temperature)
  - `Kelembaban` (Humidity)
  - `Tanggal_Ordinal` (Date converted to ordinal format)
- **Target**:
  - `Polusi_Udara` (AQI Value)
- **Model**:
  - RandomForestRegressor with 100 estimators, trained on a local CSV dataset

---

## How It Works

1. **User selects a future date** (0–7 days ahead).
2. The app loads the trained RandomForest model (cached for performance).
3. For each Jakarta region:
   - Random values for temperature and humidity are generated.
   - The selected date is converted to ordinal format.
   - The model predicts the AQI using `[Suhu, Kelembaban, Tanggal_Ordinal]`.
   - The AQI is categorized and matched with a health recommendation.
4. **Results are displayed**:
   - In a table showing region, AQI, category, and advice.
   - On an interactive map of Jakarta, with color-coded markers.

---

## 🎯 AQI-Based Recommendation System

After the model predicts the Air Quality Index (AQI), each result is **automatically classified** into a category based on standardized air quality ranges. Each category is paired with a **personalized health suggestion**, offering users actionable guidance:

| AQI Range | Category                            | Recommendation                                             |
|-----------|--------------------------------------|-------------------------------------------------------------|
| 0–49      | Good                                 | Air is clean and safe for outdoor activities.               |
| 50–99     | Moderate                             | Sensitive individuals should be cautious.                   |
| 100–149   | Unhealthy for Sensitive Groups       | Limit outdoor activity if you have respiratory conditions.  |
| 150–199   | Unhealthy                            | Reduce outdoor exposure.                                    |
| 200+      | Very Unhealthy                       | Avoid outdoor activities and wear a mask if necessary.      |

These recommendations are shown both in the result table and in the popup message on the interactive map, ensuring users get a clear understanding of health risks per region.

---

## Interactive Map Visualization

The application includes a **real-time interactive map** of Jakarta powered by [Folium](https://python-visualization.github.io/folium/), where each region is marked with a color-coded **circle marker** based on the predicted AQI:

| AQI Range | Marker Color | Meaning               |
|-----------|--------------|------------------------|
| 0–49      | 🟢 Green      | Good air quality       |
| 50–99     | 🟠 Orange     | Moderate air quality   |
| 100+      | 🔴 Red        | Unhealthy or worse     |

Each marker includes a popup with:
- Region name
- Predicted AQI value
- AQI category
- Health recommendation

This feature gives users a quick and intuitive visual overview of pollution conditions across all Jakarta regions.

---

## 🚀 Streamlit App Features

The Streamlit application includes several interactive and informative components:

![aplikasi](https://github.com/Farhan-Fadillah/picture_list/blob/6e00f2881391831dafd329057ae35081f399a158/prediction%20app%20air%20polution.png)

### 🔘 Date Selection
Users can select a date between today and the next 7 days. This allows for **short-term forecasting** of air pollution.

### 📊 Tabular Output
A dynamic table displays predicted AQI results for each Jakarta region, along with:
- The region name
- AQI value
- AQI category
- Corresponding health recommendation

This gives a **quick, readable summary** of pollution risk levels.

![result](https://github.com/Farhan-Fadillah/picture_list/blob/6e00f2881391831dafd329057ae35081f399a158/result%20prediction%20app%20air%20polution.png)

### 🗺️ Interactive Jakarta Map
A live-rendered map of Jakarta using Folium:
- Displays regional pollution levels with **color-coded markers**
- Shows detailed info via popups when markers are clicked
- Helps users **visually compare air quality across regions**

### 🔁 Prediction Refresh
Each time the "Predict" button is pressed, new randomized temperature and humidity values are used. This allows users to **simulate different possible scenarios** for the same date.

### 🧠 Cached Model
The RandomForestRegressor is loaded and cached to **optimize app performance**, especially when users repeatedly interact with the app.

---
