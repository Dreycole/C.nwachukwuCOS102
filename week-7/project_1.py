import tkinter as tk
from tkinter import messagebox
import random

#list of employees
employees_list=[
    "Mary Evans","Eyo Ishan","Durojaiye Dare","Adams Ali","Andrew ugwu",
    "stella Mankinde","jane Akibo","Ago James","Michelle Taiwo","Abraham Jones",
    "Nicole Anide","kosi Koroso","Adele Martins","Emmanuel Ojo","Ajayi Fatima"

]

#list of tasks
task_list=["Loading","Transporting","Reviewing Orders","Customer Services","Delivering Items"]

#employee Class
class Employee:
    def _init_(self, name):
        self.name=name

    def check_employees(self):
        return self.name in employees_list 
       
    def take_attendance(self):
        return f"{self.name} marked present for today."
    
    def assign_task(self):
        task=random.choice(task_list)
        return f"{self.name},your task for today is:{task}"
    
    def refuse_access(self):
        return f"Acess denied.{self.name} is not recognized as an employees."
    
    #GUI
    def process_employee():
        name =name_entry.get().strip()
        emp =Employee(name)

        if emp.check_employee():
        attendance = emp.take_attendance()
        task = emp.assign_task()
        messagebox.showinfo("Access Granted", f"{attendance}\n{task}")
    else:
        messagebox.showwarning("Access Denied", emp.refuse_access())