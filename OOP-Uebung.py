from collections import Counter

class Person:
    def __init__(self, fname, lname, gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender

    def __str__(self):
        return self.fname + " " + self.lname + " " + self.gender


class Mitarbeiter(Person):
    def __init__(self, fname, lname, gender, dept):
        super().__init__(fname, lname, gender)
        self.dept = dept

    def __str__(self):
        return super().__str__() + " " + self.dept

class Gruppenleiter(Mitarbeiter):
    def __init__(self, fname, lname, gender, dept, group):
        super().__init__(fname, lname, gender, dept)
        self.group = group

    def __str__(self):
        return super().__str__() + " " + str(self.group)

class Firma:
    def __init__(self, name, emps):
        self.name = name
        self.emps = emps
    
    def a_emps(self):
        emps_str = ""
        for i in range(len(self.emps)):
            emps_str = emps_str + str(self.emps[i]) + ", "
        return emps_str

    def mitarbeiter_count(self):
        return len(self.emps)

    def gruppenleiter_count(self):
        g = 0
        for i in range(len(self.emps)):
            if type(self.emps[i]) == Gruppenleiter:
                g = g + 1
        return g

    def dept_count(self):
        a = []
        for i in range(len(self.emps)):
            s = str(self.emps[i]).split(" ")
            a.append(s[3])
        return len(set(a)), set(a), a

    def mitarbeiter_strongest_dep(self):
        x = self.dept_count()
        counter = Counter(x[2])
        return counter.most_common(1)[0][0]

    def gender_ratio(self):
        m = 0
        for i in range(len(self.emps)):
            s = str(self.emps[i]).split(" ")
            if s[2] == "male":
                m = m + 1
        male = (m / len(self.emps)) * 100
        female = 100 - male
        return "männlich: " + str(round(male, 2)) + " %" + " weiblich: " + str(round(female, 2)) + " %"

    def __str__(self):
        return self.name + " hat " + str(self.mitarbeiter_count()) + " Mitarbeiter, davon " + \
            str(self.gruppenleiter_count()) + " Gruppenleiter, " + str(self.dept_count()[0]) + \
            " Abteilungen, wovon " + str(self.mitarbeiter_strongest_dep()) + \
            " die mitarbeiterstärkste ist. Das Geschlechtsverhältnis ist: " + str(self.gender_ratio())


def main():
    Bob = Mitarbeiter("Bob", "Baumeister", "male", "IT")
    Alice = Mitarbeiter("Alice", "Musterfrau", "female", "Sales")
    Werner = Gruppenleiter("Werner", "Mair", "male", "IT", "Project 1")

    f = Firma("HTL Anichstrasse", [Bob, Alice, Werner])
    print(f)

    Max = Mitarbeiter("Max", "Mustermann", "male", "Advertisement")
    Anna = Mitarbeiter("Anna", "Musterfrau", "female", "Sales")
    Lena = Gruppenleiter("Lena", "Müller", "female", "Management", "Project 2")
    Florian = Mitarbeiter("Florian", "Müller", "male", "Sales")

    f2 = Firma("HTL Bau und Design", [Max,Anna,Lena,Florian])
    print(f2)
    

if __name__ == "__main__":
    main()


