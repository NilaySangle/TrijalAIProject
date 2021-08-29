from Question import Question

question_prompts = [
    "1)What does IIT stands for?\n(a) Indian institute of telepathy\n(b) Indian Institute Of Technology\n(c) Internation institute of Technology\n\n",

    "2)Who is the Education Minister of India\n(a) Sanjay Shamrao\n(b) Subhas Sarkar\n(c) dharmedra pradhan\n\n",

    "3)How much is the literacy rate in India\n(a) 77.7%\n(b) 69.3%\n(c) 50%\n\n",

    "4)Which country talks in the inequality income\n(a) Russia\n(b) South africa\n(c) India\n\n",

    "5)After 6 months you can also speak English __________ me\n(a) without \n(b) about\n(c) like\n\n",

    "6)The change in focal length of an eye lens is caused by the action of the \n(a) ciliary muscles\n(b) pupil\n(c) retina\n\n",

    "7)Rainbow is caused due to \n(a) reflection of sun,light,air\n(b) dispersion of sunlight from water drops\n(c) refraction of sunlight from water drops\n\n",

    "8)The total no. of factors of a prime number is \n(a) 1\n(b) 2\n(c) 3\n\n",

    "9)2root3 is an \n(a) integer\n(b) whole number\n(c) irrational number\n\n",

    "10)if 3 coins are tossed together then what is the probability to get 2 heads\n(a) 3/8\n(b) 1/4\n(c) 5/8\n\n",

    "An event is very unlikely to happen it's probability is closest to\n(a) 0.0001\n(b) 0.001\n(c) 0.01\n\n",




]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "c"),


]





def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("Congrats you scored"+str(score) + "/" + str(len(questions))+"correct")

    if (score>8):
        print("Congrats You have won a prize "
              "You can use it in a f mart,for getting 5% discount on your school supplies"
              "code - CR7-LM10-RL9")
    if (score<8):
        print("Hard Luck,Try again later XD.")

    if (score == 8):
        print("Congrats You have won a prize "
              "You can use it in a f mart,for getting 3% discount on your school supplies"
              "code - 6ix9ine-wizKhalifa-lil nasX")


run_test(questions)




