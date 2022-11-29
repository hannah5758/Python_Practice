from sklearn.linear_model import LogisticRegression
import numpy as np

#학습 데이터 준비
x = np.array([[10],[20],[30],[40],[50]]) #studytime
y = np.array([0,0,1,1,1])#합격불합격여부
test_x = np.array([[23], [46], [33.4]])

#모델 객체 생성 및 학습
model = LogisticRegression()
model.fit(x,y)

#타겟 예측 및 결과 확인
y_predicted=model.predict(x)
print(y_predicted)

y_test_predict = model.predict(test_x)
print(y_test_predict)
