import tkinter as tk

'''
BMI Calculation tool using the Tkinter framework. 
Calculated using the following formula:

****************************************************
!               weight % (height ^ 2)              !
****************************************************

'''


class BMICalculator:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # Declaring variable types for tkinter

        self.user_weight = tk.IntVar()
        self.user_height = tk.DoubleVar()
        self.user_bmi = tk.StringVar(self.frame)

        # Labels defining for each entry field
        self.weight_label = tk.Label(self.frame, text="Weight in kg:")
        self.height_label = tk.Label(self.frame, text="Height in metres:")
        self.display_label = tk.Label(self.frame, text="Your BMI is:")
        self.bmi_display = tk.Label(self.frame, textvariable=self.user_bmi)

        # Text Entry Fields

        self.weight_entry_field = tk.Entry(self.frame, textvariable=self.user_weight)
        self.height_entry_field = tk.Entry(self.frame, textvariable=self.user_height)
        self.display_output = tk.Entry(self.frame, textvariable=self.user_bmi)

        # Button to enter the input and perform calculation using the calculate_bmi method

        self.submit_button = tk.Button(self.frame, command=lambda: self.calculate_bmi(self.user_weight.get(),
                                                                                      self.user_height.get()),
                                       text='Submit')

        # Layout configuration

        # Labels for each entry field
        self.weight_label.grid(row=0, column=0)
        self.height_label.grid(row=1, column=0)
        self.display_label.grid(row=2, column=0)

        # Entry fields

        self.weight_entry_field.grid(row=0, column=1)
        self.height_entry_field.grid(row=1, column=1)
        self.bmi_display.grid(row=2, column=1)
        self.submit_button.grid(row=3, column=1)

        self.frame.pack()

    # Method to calculate BMI which updates the user_bmi attribute

    def calculate_bmi(self, weight, height):
        bmi = float(weight) / (float(height) ** 2)
        self.user_bmi.set(round(bmi))
        print(bmi)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("BMI Calculator")
    root.geometry("256x100")
    BMICalculator(root)
    root.mainloop()

