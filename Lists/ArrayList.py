from tkinter import *

class Table:   
    def __init__(self, root):
        lst = [("",'Einfach verkettet', 'doppelt verkettet', "ArrayList"), 
                ("append", 'O(n)', 'O(1)', 'O(n)'), 
                ("prepend", 'O(1)', 'O(1)', '---'), 
                ("insert", 'O(n)', 'O(n)', 'O(n)'), # evtl. 2n wegen kopieren des Arrays wenn zu groß
                ("remove", 'O(n)', 'O(n)', 'O(1)'),
                ("delete", 'O(n)', 'O(n)', '---'), 
                ("getByIndex", 'O(n)', 'O(n)', 'O(1)'), 
                ("go_to_index", 'O(n)', 'O(n)', '---'), 
                ("clear", 'O(1)', 'O(1)', 'O(1)'),
                ("reverse", 'O(n)', 'O(n)', 'O(n)'), 
                ("sort", 'O(n^2)', 'O(n^2)', 'O(n log(n))'), 
                ("pop", 'O(n)', 'O(1)', 'O(1)'),
                ("__len__", 'O(1)', 'O(1)', 'O(1)'), 
                ("__str__", 'O(n)', 'O(n)', 'O(?)')]      
        total_rows = len(lst) 
        total_columns = len(lst[0]) 
        for i in range(total_rows): 
            for j in range(total_columns):  
                mystr = StringVar()
                mystr.set(lst[i][j])  
                self.e = Entry(textvariable=mystr, width=20, fg='black', state=DISABLED, font=('bold', 16))    
                self.e.grid(row=i, column=j) 

class ArrayList:
    def __init__(self): # O(1)
        self.array = []

    def append(self, data): # O(1)
        self.array.append(data)

    def prepend(self, data):
        # gibts nicht
        pass

    def insert(self, index, data): # O(n)
        self.array.insert(index, data)

    def remove(self, data): #
        self.array.remove(data)

    def delete(self):
        # existiert nicht
        pass

    def getByIndex(self, index): # O(1)
        return self.array[index]

    def go_to_index(self):
        # existiert nicht
        pass

    def clear(self): # O(1)
        self.array.clear()

    def reverse(self): # O(n)
        self.array.reverse()

    def sort(self): # O(n log n)
        self.array.sort()

    def pop(self): # O(1)
        self.array.pop()

    def __len__(self): # O(1)
        return len(self.array)

    def __str__(self): # O(?)
        return self.array.__str__()
    
def main():
    a = ArrayList()
    a.append(3)
    a.append(5)
    a.append(1)
    a.append(4)
    a.append(2)
    print(a)
    a.sort()
    print(a)

    root = Tk()
    root.title("Aufwandsklassen") 
    t = Table(root) 
    root.mainloop() 

if __name__ == "__main__":
    main()

  
  

  

   

   
