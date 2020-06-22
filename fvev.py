from frfr import AnomousSurvey

question = "Якы квыти тобы подобаються"

my_survey = AnomousSurvey(question)

my_survey.show_question()
print("Нажмите 'g' для віхода с опроса. \n")
while True:
    responses = input("Language:")
    if responses == 'q':
        break
    my_survey.store_response(responses)

print("\n Спасибо за ответ")
my_survey.show_results()
