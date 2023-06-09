#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = None

    def assign_id(self, patient_id):
        self.id = patient_id

    def display_info(self):
        print("Patient Information:")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.current_id = 1

    def admit_patient(self, name, age, gender):
        patient = Patient(name, age, gender)
        patient.assign_id(self.current_id)
        self.current_id += 1
        self.patients.append(patient)
        print("Patient", patient.name, "admitted to", self.name, "with ID:", patient.id)

    def discharge_patient(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                self.patients.remove(patient)
                print("Patient", patient.name, "discharged from", self.name)
                return
        print("Patient with ID:", patient_id, "not found in", self.name)

    def display_patients(self):
        print("Patients in", self.name + ":")
        for patient in self.patients:
            patient.display_info()

hospital = Hospital("IQ Hospital")

hospital.admit_patient("Souvick", 51, "Male")
hospital.admit_patient("salini", 23, "Female")
hospital.admit_patient("Kaustav", 50, "Male")

hospital.display_patients()

hospital.discharge_patient(2)
hospital.discharge_patient(4)

hospital.display_patients()


# In[ ]:




