import functions as func
import creation as crt
from time import sleep

def MainMenu():
    print("Добро пожаловать!\nЧто вы хотите сделать?\n1. Загрузить и пройти тест\n 2. Посмотреть данные ученика")
    match int(input()):

        case 1:
            chooseTest()
        case 2:
            SeeData()

def chooseTest():
    testIndex:int = 0
    pupilIndex:int

    testdata = func.readJsonFile("data.json")
    print(f"Найдено {str(len(testdata))} тестов. ")
    for i in range(len(testdata)):
        print(f"\n{i+1}. {testdata[i]['name']}.")

    try:
        testIndex = int(input("Какую загрузить?\n")) - 1
    except ValueError:
        print("Вы ввели не число!")
        chooseTest()

    pupilData = func.readJsonFile("pupils.json")
    if len(pupilData) == 0:
        print("В системе не зарегистрирован ни один ученик!\n Пройдите регистрацию:")
        crt.CreatePupil()
        return
    print(f"Найдено {len(pupilData)}. Какие из них выберите?")
    for i in range(len(pupilData)):
        print(f"{i+1}. {pupilData[i]['name']} {pupilData[i]['surname']}")

    pupilChoose = int(input()) - 1

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
    testStructure:object = func.readJsonFile("data.json")[testIndex]

    startTime = (crt.getDate()['hour'], crt.getDate()['minute'], crt.getDate()['second'])
    endTime:tuple
    answers:list = []
    curQuest:int = 0

    for i in range(len(testStructure['questions'])):
        print(testStructure['questions'][i]['question_text'])
        curQuest = i
        for i in range(len(testStructure['questions'][i]['answerOptions'])):
            print(f"{i+1}. {testStructure['questions'][curQuest]['answerOptions'][i]}")

        answers.append(int(input("Выберите вариант ответа: ")))
    else:
        endTime = (crt.getDate()['hour'], crt.getDate()['minute'], crt.getDate()['second'])
        curQuest+=1

    for i in range(len(answers)):
        answers[i] = answers[i] == testStructure['questions'][i]['rightAnswer'] + 1
            

    def Result(answers:list, testIndex:int, pupilIndex:int):
        amountOfQues:int = len(testStructure['questions'])
        rightAnswers:int = 0
        
        # grade = ['Плохо', "Нормально", "Хорошо", "Отлично", "Идеально"]
        # grade_fin = ""
        for i in range(len(answers)):
            if (answers[i]):
                rightAnswers += 1

        # final_time:object = {"second":startTime[2] - endTime[2], "minute":endTime[1], "hour":endTime[0]}
        # print(list(answers))

        for i in range(len(answers)):
            # print(answers[i])
            if (not answers[i]):
                print(f"\nНеправильный ответ в задании № {i+1}.")
        else:
            print("\n")

        print(f"Правильные ответы: {rightAnswers}\nНеправильные: {amountOfQues - rightAnswers}")

        testResult:object = {"name":func.readJsonFile("data.json")[testIndex]['name'],
                             "amountQuest":amountOfQues,
                             "rightAnswers":rightAnswers,
                             "wrongAnswers":amountOfQues - rightAnswers
                             }
        data = func.readJsonFile("pupils.json")
        # print(data[pupilIndex]['completedTests'])
        data[pupilIndex]['completedTests'].append(testResult)
        # print(f"{data}\n{testResult}")
        func.writeJsonFile(data, "pupils.json")

        
    Result(answers, testIndex, pupilIndex)
def SeeData():
    data = func.readJsonFile("pupils.json")
    print(f"Найдено: {len(data)} учеников")
    for i in range(len(data)):
        print(f"{i+1}. {data[i]['name']} {data[i]['surname']}. Завершено тестов: {len(data[i]['completedTests'])}")
    sleep(1)
    print("\n")
    MainMenu()

MainMenu()