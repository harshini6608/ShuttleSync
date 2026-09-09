class StudentTracker:

    def __init__(self):
        # Hash Map:
        # Student ID -> bus they are currently inside
        self.students = {}

    def enter_bus(self, student_id, bus):

        # Student is already inside a bus
        if student_id in self.students:
            print("Student", student_id, "is already inside a bus.")
            return False

        # Check whether bus has space
        if not bus.add_passenger():
            print("Bus is FULL.")
            return False

        # Store student in Hash Map
        self.students[student_id] = bus.bus_id

        print(
            "Student",
            student_id,
            "entered",
            bus.bus_id
        )

        return True

    def exit_bus(self, student_id, bus):

        # Student is not registered as inside
        if student_id not in self.students:
            print(
                "Student",
                student_id,
                "is not inside a bus."
            )
            return False

        # Check that student is exiting the correct bus
        if self.students[student_id] != bus.bus_id:
            print(
                "Student",
                student_id,
                "is inside",
                self.students[student_id]
            )
            return False

        # Remove passenger
        bus.remove_passenger()

        # Remove student from Hash Map
        del self.students[student_id]

        print(
            "Student",
            student_id,
            "exited",
            bus.bus_id
        )

        return True