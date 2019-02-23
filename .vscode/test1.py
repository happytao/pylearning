HEIGHT = 1.75
WEIGHT = 80.5
float(bmi) = WEIGHT/(HEIGHT*HEIGHT)
if bmi < 18.5:
    print('bmi = %f,过轻' %bmi)
elif bmi < 25.0:
    print('bmi = %f,正常' %bmi)
elif bmi < 28.0:
    print('bmi = %f,过重' %bmi)
elif bmi < 32.0:
    print('bmi = %f,肥胖' %bmi)
else:
    print('bmi = %f,严重肥胖' %bmi)