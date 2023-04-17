import functions as func
import creation as crt
from time import sleep
def chooseTest():
    testIndex:int = 0
    pupilIndex:int

    testdata = func.readJsonFile("data.json")
    print(f"Найдено {str(len(testdata))} тестов. ")
    for i in range(len(testdata)):
        print(f"\n{i+1}. {testdata[i]['name']}.")

    try:
        testIndex = int(input("Какую загрузить?"))
    except ValueError:
        print("Вы ввели не число!")

    pupilData = func.readJsonFile("pupils.json")
    if len(pupilData) == 0:
        print("В системе не зарегестрирован ни один ученик!\n Пройдите регистрацию:")
        crt.CreatePupil()
        return
    print(f"Найдено {len(pupilData)}. Какие из них выберите?")
    for i in range(len(pupilData)):
        print(f"{i+1}. {pupilData[i]['name']} {pupilData[i]['surname']}")

    pupilChoose = int(input())

    if (pupilChoose > len(pupilData)):
        print('damn')
        return
    pupilIndex = pupilChoose
    del pupilChoose
    print("Тест начнется через 3...")
    sleep(1)
    print("Тест начнется через 2...")
    sleep(1)
    print("Тест начнется через 1...")
    sleep(1)
    print("Вперед!\n")
    GoToTest(testIndex, pupilIndex)
    
def GoToTest(testIndex:int, pupilIndex:int):
    pupilStructure:object = func.readJsonFile("pupils.json")[pupilIndex - 1]
    testStructure:object = func.readJsonFile("data.json")[testIndex - 1]

    startTime = (crt.getDate()['hour'], crt.getDate()['minute'], crt.getDate()['second'])
    endTime:tuple
    answers:list = []
    curQuest:int = 0

    for i in range(len(testStructure['questions'])):
        print(testStructure['questions'][i]['question_text'])

        for i in range(len(testStructure['questions'][curQuest]['answerOptions'])):
            print(f"{i+1}. {testStructure['questions'][curQuest]['answerOptions'][i]}")

        answers.append(int(input("Выберите вариант ответа: ")))
    else:
        endTime = (crt.getDate()['hour'], crt.getDate()['minute'], crt.getDate()['second'])
        curQuest+=1

    for i in range(len(answers)):
        answers[i] = answers[i] == testStructure['questions'][i]['rightAnswer'] + 1
            

    def Result():
        amountOfQues:int = len(testStructure['questions'])
        rightAnswers:int = 0
        
        grade = ['Плохо', "Нормально", "Хорошо", "Отлично", "Идеально"]
        grade_fin = ""
        for i in range(len(answers)):
            if (answers[i]):
                rightAnswers += 1

        print(endTime-startTime)
        # print(f"{rightAnswers} {amountOfQues}")
        # print(grade_fin)
    Result()

chooseTest()