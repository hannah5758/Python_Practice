from sklearn.linear_model import LogisticRegression
import numpy as np

#학습 데이터 준비
x = np.array([[10,66],[20,85],[30,86],[40,92],[50,96]]) #공부 시간, 지난 시험 성적
y = np.array([0,0,1,1,1]) #합격 or not

#모델 객체 생성 및 학습
model = LogisticRegression()
model.fit(x,y)

#타깃 예측 및 결과 확인
y_predicted = model.predict(x)
print(y_predicted)
