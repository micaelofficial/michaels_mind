import streamlit as st
import joblib
import pandas as pd

# Загрузка модели
model = joblib.load('7.Project-VII_Flight_Delays/flight_delay_model_v3_final.pkl')

# Переключатель языка
lang = st.selectbox("Язык / Language", ["Русский", "English"])

if lang == "Русский":
    st.title("Предсказание задержки рейса (>15 мин)")
    st.markdown("Введите параметры рейса — получите вероятность задержки.")
    st.caption(
    "Для демо значения OriginDelayRate, DestDelayRate и AvgDecSnowfall зафиксированы на средних/нулевых уровнях. "
    "В реальном приложении они бы брались из внешних источников или базы данных."
)
    btn_text = "Предсказать задержку"
    result_title = "Результат"
    high_risk = "Высокий риск задержки!"
    medium_risk = "Средний риск — будьте готовы."
    low_risk = "Низкий риск — рейс скорее всего вовремя."
    prob_text = "Вероятность задержки >15 мин"
else:
    st.title("Flight Delay Prediction (>15 min)")
    st.markdown("Enter flight parameters — get delay probability.")
    st.caption(
    "For demo purposes, OriginDelayRate, DestDelayRate, and AvgDecSnowfall are fixed at average/zero values. "
    "In production, they would come from external sources or database."
)
    btn_text = "Predict Delay"
    result_title = "Result"
    high_risk = "High delay risk!"
    medium_risk = "Medium risk — be prepared."
    low_risk = "Low risk — flight likely on time."
    prob_text = "Probability of delay >15 min"

# Ввод
col1, col2 = st.columns(2)
with col1:
    dep_hour = st.slider("Час вылета / Departure Hour (CRS)", 0, 23, 12)
    is_weekend = st.selectbox("Выходной день? / Weekend?", ["Нет / No", "Да / Yes"])
    is_holiday = st.selectbox("Праздник? / Holiday?", ["Нет / No", "Да / Yes"])

with col2:
    distance = st.number_input("Расстояние (мили) / Distance (miles)", min_value=50, max_value=5000, value=1000)
    prev_delay = st.number_input("Задержка предыдущего рейса (мин) / Previous Delay (min)", min_value=0, max_value=300, value=0)

if st.button(btn_text):
    input_dict = {
        'DepHour': dep_hour,
        'IsMorning': 1 if dep_hour < 12 else 0,
        'IsWeekend': 1 if is_weekend == "Да / Yes" else 0,
        'IsHoliday': 1 if is_holiday == "Да / Yes" else 0,
        'Distance': distance,
        'AvgDecSnowfall': 0.0,
        'OriginDelayRate': 0.1,
        'DestDelayRate': 0.1,
        'DepHour_Weekend': dep_hour * (1 if is_weekend == "Да / Yes" else 0) * 3,
        'PreviousDepDelay': prev_delay,
    }

    for col in model.feature_names_in_:
        if col not in input_dict:
            input_dict[col] = 0

    input_data = pd.DataFrame([input_dict])

    prob = model.predict_proba(input_data)[0][1]

    st.subheader(result_title)
    st.metric(prob_text, f"{prob*100:.1f}%")

    if prob > 0.5:
        st.error(high_risk)
    elif prob > 0.3:
        st.warning(medium_risk)
    else:
        st.success(low_risk)
        
st.markdown("---")
st.caption("The model was trained on BTS data from December 2024. AUC = 0.766. This is a prototype.")