class MyResume:
    """ если у объекта нет переменной, то он пользуется переменной класса"""
    total_resume = 0
    zagolovok = "Моё резюме"

    def __init__(self):
        MyResume.total_resume += 1

    def __str__(self):
        return self.zagolovok + ': ' + str(self.total_resume)


resume_1 = MyResume()
resume_2 = MyResume()
resume_3 = MyResume()

print(MyResume.total_resume)
resume_1.zagolovok = "Нет резюме"
print(resume_1)
print(resume_2)
