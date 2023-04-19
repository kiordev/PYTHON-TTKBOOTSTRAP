import ttkbootstrap as tkb
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.validation import add_regex_validation

class Gradebook(tkb.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.name = tkb.StringVar(value="")
        self.course_name = tkb.StringVar(value="")
        self.student_id = tkb.StringVar(value="")
        self.final_score = tkb.StringVar(value=0)
        self.data=[]
        self.colors = master_window.style.colors

        instruction_text = "Please Enter your contact information: "
        instrucion = tkb.Label(self, text=instruction_text, width=50)
        instrucion.pack(fill=tkb.X, pady=10)

        self.create_form_entry("Name: ", self.name)
        self.create_form_entry("ID: ", self.student_id)
        self.create_form_entry("Course: ", self.course_name)
        self.final_score_input = self.create_form_entry("Final Score: ", self.final_score)

        self.create_meter()
        self.create_button()
        self.table = self.create_table()
    def create_form_entry(self, label, variable): #Create Inputs
        form_field_container = tkb.Frame(self)
        form_field_container.pack(fill=tkb.X, expand=YES, pady=5)

        form_field_label = tkb.Label(master=form_field_container, text=label, width=15)
        form_field_label.pack(side=tkb.LEFT, padx=12)

        form_input = tkb.Entry(master=form_field_container, textvariable=variable)
        form_input.pack(side=tkb.LEFT, padx=5, fill=tkb.X, expand=YES)

        add_regex_validation(form_input, r'^[a-zA-Z0-9_]*$')
        return form_input

    def create_meter(self): #Create Meter
        meter = tkb.Meter(
            master=self,
            metersize=150,
            padding=5,
            amounttotal=100,
            amountused=50,
            metertype='full',
            subtext="Final Score",
            interactive=True,
        )
        meter.pack()
        self.final_score.set(meter.amountusedvar)
        self.final_score_input.configure(textvariable=meter.amountusedvar)


    def create_button(self): # Create buttons
        button_container = tkb.Frame(self)
        button_container.pack(fill=tkb.X, expand=YES, pady=(15, 10))

        cancel_button = tkb.Button(
            master=button_container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle='danger',
            width=6
        )
        cancel_button.pack(side=RIGHT, padx=5)

        submit_button = tkb.Button(
            master=button_container,
            text="Submit",
            command=self.on_submit,
            bootstyle='info',
            width=6,
        )
        submit_button.pack(side=RIGHT, padx=5)


    def on_submit(self):
        name = self.name.get()
        student_id = self.student_id.get()
        course_name = self.course_name.get()
        final_score = self.final_score_input.get()

        toast = ToastNotification(
            title="Submition successful",
            message = "Your data has been successfully submitted",
            duration=3000,
        )

        toast.show_toast()

        self.data.append((name, student_id, course_name, final_score))
        self.table.destroy()
        self.table = self.create_table()

    def on_cancel(self):
        self.quit()


    def create_table(self):
        coldata=[
            {"text": "Name"},
            {"text": "Student ID"},
            {"text": "Course Name"},
            {"text": "Final Score"},
        ]

        table = Tableview(
            master=self,
            coldata=coldata,
            rowdata=self.data,
            paginated=True,
            searchable=True,
            bootstyle='primary',
            stripecolor=(self.colors.light, None)
        )

        table.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        return table

if __name__ == "__main__":
    app = tkb.Window("GradeBook", "vapor", resizable=(False, False))
    Gradebook(app)
    app.mainloop()