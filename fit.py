from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)

# CSV 파일 읽어오기
csv_file_path = 'data.csv' 
data = pd.read_csv(csv_file_path, encoding='cp949')
data = data[['식품명', '에너지(kcal)', '단백질(g)', '지방(g)', '탄수화물(g)', '식품중량']].dropna()

# 특성 및 레이블 설정
X = data[['에너지(kcal)', '단백질(g)', '지방(g)', '탄수화물(g)']]
y = data['식품명']

# 데이터 정규화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# BMI에 따른 일일 칼로리 필요량 계산 함수
def calculate_caloric_needs(bmi):
    if bmi < 18.5:
        return 2500
    elif 18.5 <= bmi < 24.9:
        return 2000
    elif 25 <= bmi < 29.9:
        return 1800
    else:
        return 1500

# 예측 및 식단 추천 함수
def recommend_diet(model, daily_caloric_needs, scaler, data):
    recommended_diet = []
    total_calories = 0

    for _, row in data.iterrows():
        if total_calories >= daily_caloric_needs:
            break

        food_features = row[['에너지(kcal)', '단백질(g)', '지방(g)', '탄수화물(g)']].values.reshape(1, -1)
        food_features_scaled = scaler.transform(food_features)

        food_name = model.predict(food_features_scaled)[0]
        food_calories = row['에너지(kcal)']
        food_weight = row['식품중량']

        if total_calories + food_calories <= daily_caloric_needs:
            recommended_diet.append((food_name, food_calories, food_weight))
            total_calories += food_calories

    return recommended_diet