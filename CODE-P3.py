from datetime import datetime
from os import remove
from sched import scheduler

next_appointment_id = 1
appointments = []

instructors_list = [
    "Actub Lord Neil",
    "Anches Laurenz Aizel",
    "Apus Glyza Mae",
    "Asesor Archieliz",
    "Bagongon Ivy Mae",
    "Baterna Junel",
    "Belmes Jayson",
    "Cainglet Riel Jun",
    "Calma Joshua",
    "Cantila Grachael",
    "Capaque Mosheh Cyril",
    "Casicas Renee Fe",
    "Colaste Gwayne Rithzel",
    "Dollera Faith Nave",
    "Dragon Claire",
    "Estroga Johnbert",
    "Gordo Rembrandt",
    "Hernandez Lloyd Aisne",
    "Lampitao Angel",
    "Larosa Alexis",
    "Llemit Arnel",
    "Lucagbo Quennie Arjee",
    "Macario Adormie",
    "Maristela Jan Nichols",
    "Montejo Heidern",
    "Opiso Irish",
    "Piquero Rachel Joy",
    "Ranan Kiven",
    "Ranara Leilani",
    "Salvador Ian Paul",
    "Simo Jeremiah",
    "Taypin Joannie",
    "Taypin Marte",
    "Turtosa Fritz Gerald",
    "Vergara Justin",
    "Villadores Alein Dhave",
    "Villanueva Love Jean",
    "Legaspi, Giann Isidore"
]
instructor_schedules = {
    "Actub Lord Neil": {
        "Monday": ["1:00 PM - 5:00 PM"],
        "Tuesday": ["1:00 PM - 5:00 PM"],
        "Wednesday": ["2:00 PM - 4:00 PM"]
    },

    "Anches Laurenz Aizel": {
        "Tuesday": ["10:30 AM - 12:00 NN", "1:00 PM - 4:30 PM"],
        "Thursday": ["10:30 AM - 12:00 NN", "1:00 PM - 4:30 PM"]
    },

    "Apus Glyza Mae": {
        "Monday": ["8:00 AM - 9:00 AM"],
        "Tuesday": ["8:00 AM - 9:00 AM"],
        "Friday": ["8:00 AM - 12:00 NN", "1:00 PM - 5:00 PM"]
    },

    "Asesor Archieliz": {
        "Tuesday": ["9:00 AM - 11:30 AM"]
    },

    "Bagongon Ivy Mae": {
        "Tuesday": ["9:00 AM - 12:00 NN", "1:00 PM - 5:00 PM"],
        "Thursday": ["9:00 AM - 12:00 NN"]
    },

    "Baterna Junel": {
        "Monday": ["2:00 PM - 5:00 PM"],
        "Wednesday": ["2:00 PM - 5:00 PM"],
        "Thursday": ["11:00 AM - 12:00 NN", "2:00 PM - 5:00 PM"]
    },

    "Belmes Jayson": {
        "Monday": ["1:30 PM - 4:30 PM"],
        "Tuesday": ["9:00 AM - 12:00 NN"],
        "Wednesday": ["9:00 AM - 12:00 NN"],
        "Thursday": ["9:00 AM - 10:00 AM"]
    },

    "Cainglet Riel Jun": {
        "Monday": ["9:00 AM - 12:00 NN"],
        "Wednesday": ["1:00 PM - 4:00 PM"]
    },

    "Calma Joshua": {
        "Monday": ["9:00 AM - 12:00 NN", "1:00 PM - 5:00 PM"],
        "Tuesday": ["8:00 AM - 9:00 AM"],
        "Wednesday": ["1:00 PM - 3:00 PM"]
    },

    "Cantila Grachael": {
        "Monday": ["9:00 AM - 12:00 NN"],
        "Wednesday": ["9:00 AM - 12:00 NN"],
        "Friday": ["1:00 PM - 5:00 PM"]
    },

    "Capaque Mosheh Cyril": {
        "Monday": ["9:00 AM - 12:00 NN"],
        "Tuesday": ["1:00 PM - 5:00 PM"]
    },

    "Casicas Renee Fe": {
        "Monday": ["8:00 AM - 12:00 NN"],
        "Wednesday": ["8:00 AM - 12:00 NN"],
        "Thursday": ["10:00 AM - 12:00 NN"]
    },

    "Colaste Gwayne Rithzel": {
        "Tuesday": ["8:00 AM - 12:00 NN", "1:00 PM - 5:00 PM"],
        "Wednesday": ["8:00 AM - 9:00 AM"],
        "Thursday": ["8:00 AM - 9:00 AM"]
    },

    "Dollera Faith Nave": {
        "Tuesday": ["10:30 AM - 12:00 NN", "1:00 PM - 4:30 PM"],
        "Wednesday": ["10:00 AM - 12:00 NN"],
        "Thursday": ["10:30 AM - 12:00 NN"]
    },

    "Dragon Claire": {
        "Monday": ["1:00 PM - 5:00 PM"],
        "Tuesday": ["11:00 AM - 12:00 NN", "1:00 PM - 3:00 PM"],
        "Thursday": ["11:00 AM - 12:00 NN", "2:00 PM - 4:00 PM"]
    },

    "Estroga Johnbert": {
        "Monday": ["7:30 AM - 1:30 PM"],
        "Tuesday": ["10:30 AM - 12:00 NN", "1:30 PM - 3:00 PM"],
        "Wednesday": ["7:30 AM - 12:00 NN"],
        "Thursday": ["10:30 AM - 12:00 NN", "1:30 PM - 3:00 PM"]
    },

    "Gordo Rembrandt": {
        "Monday": ["8:00 AM - 12:00 NN"],
        "Tuesday": ["8:00 AM - 12:00 NN"]
    },

    "Hernandez Lloyd Aisne": {
        "Tuesday": ["1:00 PM - 5:00 PM"],
        "Wednesday": ["9:00 AM - 12:00 NN"],
        "Friday": ["1:30 PM - 4:30 PM"]
    },

    "Lampitao Angel": {
        "Monday": ["1:00 PM - 5:00 PM"],
        "Tuesday": ["1:00 PM - 3:30 PM"],
        "Wednesday": ["10:00 AM - 11:00 AM"],
        "Thursday": ["1:00 PM - 3:30 PM"]
    },

    "Larosa Alexis": {
        "Monday": ["10:30 AM - 12:00 NN", "3:00 PM - 5:00 PM"],
        "Tuesday": ["10:30 AM - 12:00 NN", "3:00 PM - 5:00 PM"],
        "Thursday": ["8:00 AM - 12:00 NN"]
    },

    "Llemit Arnel": {},

    "Lucagbo Quennie Arjee": {
        "Monday": ["1:00 PM - 2:30 PM"],
        "Tuesday": ["1:00 PM - 4:00 PM"],
        "Wednesday": ["1:00 PM - 2:30 PM"],
        "Thursday": ["1:00 PM - 5:00 PM"]
    },

    "Macario Adormie": {},

    "Maristela Jan Nichols": {
        "Monday": ["10:00 AM - 12:00 NN", "3:00 PM - 5:30 PM"],
        "Wednesday": ["10:00 AM - 12:00 NN", "3:00 PM - 5:30 PM"],
        "Thursday": ["1:00 PM - 3:30 PM"]
    },

    "Montejo Heidern": {
        "Tuesday": ["11:00 AM - 12:00 NN", "1:00 PM - 5:00 PM"],
        "Thursday": ["1:00 PM - 5:00 PM"],
        "Friday": ["1:00 PM - 2:00 PM"]
    },

    "Opiso Irish": {
        "Monday": ["1:30 PM - 4:30 PM"],
        "Tuesday": ["1:00 PM - 2:30 PM"],
        "Wednesday": ["1:30 PM - 4:30 PM"],
        "Friday": ["3:00 PM - 4:30 PM"]
    },

    "Piquero Rachel Joy": {
        "Wednesday": ["8:00 AM - 9:00 AM", "1:00 PM - 4:30 PM"],
        "Thursday": ["8:00 AM - 9:00 AM"],
        "Friday": ["8:00 AM - 9:00 AM"],
        "Saturday": ["8:30 AM - 12:00 NN"]
    },

    "Ranan Kiven": {
        "Monday": ["9:00 AM - 12:00 NN", "1:00 PM - 5:00 PM"],
        "Saturday": ["8:30 AM - 10:30 AM"]
    },

    "Ranara Leilani": {
        "Monday": ["8:00 AM - 9:00 AM", "4:30 PM - 5:30 PM"],
        "Tuesday": ["8:00 AM - 12:00 NN"],
        "Thursday": ["1:00 PM - 5:00 PM"]
    },

    "Salvador Ian Paul": {
        "Thursday": ["8:00 AM - 12:00 NN"],
        "Friday": ["9:00 AM - 12:00 NN", "1:00 PM - 4:00 PM"]
    },

    "Simo Jeremiah": {
        "Monday": ["9:00 AM - 10:30 AM", "1:30 PM - 5:00 PM"],
        "Tuesday": ["1:00 PM - 4:30 PM"],
        "Wednesday": ["9:00 AM - 10:30 AM", "1:30 PM - 5:00 PM"]
    },

    "Taypin Joannie": {
        "Wednesday": ["9:00 AM - 12:00 NN"],
        "Thursday": ["9:00 AM - 12:00 NN", "1:00 PM - 5:00 PM"]
    },

    "Taypin Marte": {
        "Tuesday": ["9:00 AM - 12:00 NN"],
        "Wednesday": ["1:00 PM - 5:00 PM"],
        "Thursday": ["9:00 AM - 12:00 NN"]
    },

    "Turtosa Fritz Gerald": {
        "Monday": ["8:00 AM - 12:00 NN", "1:00 PM - 3:00 PM"],
        "Wednesday": ["8:00 AM - 12:00 NN"]
    },

    "Vergara Justin": {
        "Monday": ["1:30 PM - 4:30 PM"],
        "Tuesday": ["10:00 AM - 12:00 NN"],
        "Wednesday": ["1:30 PM - 4:30 PM"],
        "Thursday": ["1:30 PM - 3:30 PM"],
        "Friday": ["11:00 AM - 12:00 NN", "1:00 PM - 5:00 PM"]
    },

    "Villadores Alein Dhave": {
        "Monday": ["8:30 AM - 11:00 AM", "1:30 PM - 5:00 PM"],
        "Wednesday": ["8:30 AM - 12:00 NN", "1:30 PM - 2:30 PM"],
        "Friday": ["8:30 AM - 11:30 AM"]
    },

    "Villanueva Love Jean": {
        "Monday": ["1:00 PM - 5:00 PM"],
        "Tuesday": ["1:00 PM - 5:00 PM"],
        "Wednesday": ["1:00 PM - 3:00 PM"]
    },

    "Legaspi, Giann Isidore": {
        "Monday": ["8:00 AM - 12:00 NN"],
        "Tuesday": ["8:00 AM - 12:00 NN"]
    }
}

def get_valid_date(prompt):
    while True:
        date_text = input(prompt).strip()

        try:
            selected_date = datetime.strptime(
                date_text, "%Y-%m-%d"
            ).date()

            if selected_date < datetime.today().date():
                print("Error: You cannot choose a past date.")
                continue

            return selected_date

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")
            print("Example: 2026-10-15")

def choose_schedule():
    print("\n<------------------------------------------>")
    print("            AVAILABLE INSTRUCTORS")
    print("<------------------------------------------>")

    for number, instructor in enumerate(instructors_list, start=1):
        print(f"{number}. {instructor}")

    while True:
        try:
            choice = int(input("\nChoose instructor number: "))

            if 1 <= choice <= len(instructors_list):
                break

            print("Please select a number from the list.")

        except ValueError:
            print("Please enter a valid number.")

    instructor_name = instructors_list[choice - 1]
    schedule = instructor_schedules.get(instructor_name, {})

    print("\n<------------------------------------------>")
    print("          INSTRUCTOR AVAILABLE SCHEDULE")
    print("<------------------------------------------>")
    print("Instructor:", instructor_name)

    if not schedule:
        print("No consultation schedule is available for this instructor.")
        print("Please choose another instructor.")
        return None

    for day, times in schedule.items():
        print(f"\n{day}:")
        for time_range in times:
            print(f"  - {time_range}")

    while True:
        selected_date = get_valid_date(
            "\nEnter appointment date (YYYY-MM-DD): "
        )

        day_name = selected_date.strftime("%A")

        if day_name not in schedule:
            available_days = ", ".join(schedule.keys())
            print(f"\n{instructor_name} is not available on {day_name}.")
            print("Available days:", available_days)
            print("Please enter another date.")
            continue

        break

    available_times = schedule[day_name]

    print(f"\nAvailable times for {instructor_name} on {day_name}:")
    for number, time_range in enumerate(available_times, start=1):
        print(f"{number}. {time_range}")

    while True:
        try:
            time_choice = int(input("\nChoose available time number: "))

            if 1 <= time_choice <= len(available_times):
                break

            print("Please select a number from the list.")

        except ValueError:
            print("Please enter a valid number.")

    selected_time = available_times[time_choice - 1]

    for appointment in appointments:
        if (
            appointment["instructor"] == instructor_name
            and appointment["date"] == selected_date.strftime("%Y-%m-%d")
            and appointment["time"] == selected_time
            and appointment["status"] == "Scheduled"
        ):
            print("\nThat instructor's selected time is already booked.")
            print("Please try again with another time or date.")
            return None

    return {
        "instructor": instructor_name,
        "date": selected_date.strftime("%Y-%m-%d"),
        "time": selected_time
    }


def update_instructor_schedule():
    print("\n<------------------------------------------>")
    print("         UPDATE INSTRUCTOR SCHEDULE")
    print("<------------------------------------------>")

    for number, instructor in enumerate(instructors_list, start=1):
        print(f"{number}. {instructor}")

    while True:
        try:
            instructor_choice = int(input("Choose instructor number: "))
            if 1 <= instructor_choice <= len(instructors_list):
                break
            print("Invalid choice. Please select a listed number.")
        except ValueError:
            print("Please enter a valid number.")

    instructor_name = instructors_list[instructor_choice - 1]
    schedule = instructor_schedules.setdefault(instructor_name, {})


    while True:

        print("\n1. Add Available Time")
        print("2. Replace Available Time")
        print("3. Remove Available Time")
        print("4. Return to Instructor Menu")

        option = input("Enter your choice: ").strip()

        if option == "4":
            break

        if option not in ["1", "2", "3"]:
            print("Invalid choice. Please select 1-4.")
            continue

        days = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday"
        ]

        print("\nCHOOSE AVAILABLE DAY")

        for number, day in enumerate(days, start=1):
            print(f"{number}. {day}")

        while True:
            try:
                day_choice = int(input("Choose day number: "))

                if 1 <= day_choice <= 6:
                    selected_day = days[day_choice - 1]
                    break

                print("Invalid day. Please select 1-6.")

            except ValueError:
                print("Please enter a valid number.")

        if option in ["2", "3"]:
            if selected_day not in schedule or not schedule[selected_day]:
                print("No available time on this day.")
                continue

            print("\nAVAILABLE TIMES")

            for number, time_range in enumerate(
                schedule[selected_day], start=1
            ):
                print(f"{number}. {time_range}")

            print("0. Return to Update Instructor Schedule Menu")

            while True:
                try:
                    time_choice = int(input("Choose time number: "))

                    if time_choice == 0:
                        print("Returning to Update Instructor Schedule Menu.")
                        break

                    if 1 <= time_choice <= len(schedule[selected_day]):
                        break

                    print("Invalid time number.")

                except ValueError:
                    print("Please enter a valid number.")

            if time_choice == 0:
                continue

            old_time = schedule[selected_day][time_choice - 1]

            if option == "3":
                if any(
                    appointment["instructor"] == instructor_name
                    and datetime.strptime(
                        appointment["date"], "%Y-%m-%d"
                    ).strftime("%A") == selected_day
                    and appointment["time"] == old_time
                    and appointment["status"] == "Scheduled"
                    for appointment in appointments
                ):
                    print("Cannot remove this time.")
                    print("There are existing scheduled appointments.")
                    continue

                schedule[selected_day].remove(old_time)

                if not schedule[selected_day]:
                    del schedule[selected_day]

                print("\nAvailable time removed successfully!")
                print("The selected time is no longer available.")

                continue

        while True:
            start_text = input(
                "Enter starting time (example: 9:00 AM): "
            ).strip().upper()

            end_text = input(
                "Enter ending time (example: 12:00 PM): "
            ).strip().upper()

            try:
                start_time = datetime.strptime(
                    start_text, "%I:%M %p"
                )
                end_time = datetime.strptime(
                    end_text, "%I:%M %p"
                )

                if start_time >= end_time:
                    print("Ending time must be later than starting time.")
                    continue

                break

            except ValueError:
                print("Invalid time format. Use HH:MM AM/PM.")

        new_time = (
            f"{start_time.strftime('%I:%M %p').lstrip('0')} - "
            f"{end_time.strftime('%I:%M %p').lstrip('0')}"
        )

        existing_times = schedule.get(selected_day, [])

        conflict = False

        for time_range in existing_times:
            if option == "2" and time_range == old_time:
                continue

            old_start, old_end = time_range.split(" - ")

            old_start = old_start.replace("NN", "PM")
            old_end = old_end.replace("NN", "PM")

            old_start_time = datetime.strptime(
                old_start, "%I:%M %p"
            )
            old_end_time = datetime.strptime(
                old_end, "%I:%M %p"
            )

            if start_time < old_end_time and end_time > old_start_time:
                conflict = True
                break

        if conflict:
            print("This time is already included in another schedule. Please choose a different time.")
            continue

        if option == "1":
            if selected_day not in schedule:
                schedule[selected_day] = []

            schedule[selected_day].append(new_time)
            print("Available time added successfully!")

        elif option == "2":
            if any(
                appointment["instructor"] == instructor_name
                and datetime.strptime(
                    appointment["date"], "%Y-%m-%d"
                ).strftime("%A") == selected_day
                and appointment["time"] == old_time
                and appointment["status"] == "Scheduled"
                for appointment in appointments
            ):
                print("Cannot replace this time.")
                print("There are existing scheduled appointments.")
                continue

            schedule[selected_day][time_choice - 1] = new_time
            print("Available time updated successfully!")

def view_instructor_schedule_summary():
    print("\n<------------------------------------------>")
    print("         INSTRUCTOR SCHEDULE SUMMARY")
    print("<------------------------------------------>")

    if not instructor_schedules:
        print("No instructor schedules available.")
        return

    for instructor, schedule in instructor_schedules.items():
        print(f"\nInstructor: {instructor}")

        if not schedule:
            print("  No available schedule.")
            continue

        for day, times in schedule.items():
            print(f"  {day}:")
            for time_range in times:
                print(f"    - {time_range}")

def add_appointment():
    global next_appointment_id

    print("\n<------------------------------------------>")
    print("              ADD APPOINTMENT")
    print("<------------------------------------------>")

    while True:
        student_id = input("Enter your Student ID (02-0000-000000): ").strip()

        parts = student_id.split("-")

        if not student_id:
            print("Student ID cannot be empty.")

        elif (len(parts) != 3 or
              len(parts[0]) != 2 or
              len(parts[1]) != 4 or
              len(parts[2]) != 6 or
              not all(part.isascii() and part.isdigit() for part in parts)):
            print("Invalid Student ID! Use this format: 02-0000-000000")

        else:
            break

    while True:
        student_name = input("Enter your student name: ").strip()

        if not student_name:
            print("Student name cannot be empty.")

        elif not all(char.isalpha() or char.isspace() or char in ",.-'" for char in student_name):
            print("Invalid Student Name! Numbers are not allowed.")

        else:
            break
    student_section = input("Enter your section: ").strip()
    if not student_section:
        print("Student section cannot be empty.")
        return

    purpose = input("Enter the purpose of the appointment: ").strip()
    if not purpose:
        print("Purpose cannot be empty.")
        return

    selected = choose_schedule()

    if selected is None:
        print("\nAppointment was not added.")
        return

    appointment = {
        "id": next_appointment_id,
        "student_id": student_id,
        "student_name": student_name,
        "student_section": student_section,
        "purpose": purpose,
        "instructor": selected["instructor"],
        "date": selected["date"],
        "time": selected["time"],
        "status": "Scheduled"
    }

    appointments.append(appointment)

    print("\nAppointment added successfully!")
    display_appointment(appointment)

    next_appointment_id += 1

def display_appointment(appointment):
    print("\n----------------------------------------")
    print("Appointment ID :", appointment["id"])
    print("Student ID     :", appointment["student_id"])
    print("Student Name   :", appointment["student_name"])
    print("Section        :", appointment.get("student_section", "N/A"))
    print("Instructor     :", appointment["instructor"])
    print("Date           :", appointment["date"])
    print("Time           :", appointment["time"])
    print("Purpose        :", appointment["purpose"])
    print("Status         :", appointment["status"])
    print("----------------------------------------")

def find_appointment_by_id(appointment_id):
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            return appointment

    return None

def view_appointments():
    print("\n<------------------------------------------>")
    print("              ALL APPOINTMENTS")
    print("<------------------------------------------>")

    if not appointments:
        print("No appointments found.")
        return

    for appointment in appointments:
        display_appointment(appointment)

def search_appointment():
    print("\n<------------------------------------------>")
    print("              SEARCH APPOINTMENT")
    print("<------------------------------------------>")


    while True:
        keyword = input(
            "Enter student ID, student name, or instructor name: "
        ).strip().lower()

        if not keyword:
            print("Search input cannot be empty.")
            continue

        matches = []

        for appointment in appointments:
            student_id = str(appointment["student_id"]).lower()
            student_name = appointment["student_name"].lower()
            instructor = appointment["instructor"].lower()

            if (
                keyword == student_id
                or keyword in student_name
                or keyword in instructor
            ):
                matches.append(appointment)

        if not matches:
            print("Invalid! No matching appointment found.")
            continue

        break

    found = False
    for appointment in matches:
        if (
            keyword in str(appointment["student_id"]).lower()
            or keyword in appointment["student_name"].lower()
            or keyword in appointment["instructor"].lower()
        ):
            display_appointment(appointment)
            found = True

    if not found:
        print("No matching appointment found.")


def update_appointment_information():
    update_appointment()


def update_appointment():
    print("\n<------------------------------------------>")
    print("          UPDATE STUDENT INFORMATION")
    print("<------------------------------------------>")

    try:
        appointment_id = int(input("Enter appointment ID: ").strip())
    except ValueError:
        print("Invalid appointment ID.")
        return

    appointment = find_appointment_by_id(appointment_id)

    if appointment is None:
        print("Appointment not found.")
        return

    if appointment["status"] != "Scheduled":
        print("Only scheduled appointments can be updated.")
        return

    print("\nCurrent appointment:")
    display_appointment(appointment)

    print("\nChoose what to update:")
    print("1.Student ID")
    print("2.Student name")
    print("3.Student section")
    print("4.Purpose")
    print("5.Instructor, date, and time")
    print("6.Return to main menu")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        while True:
            new_id = input("Enter new student ID: ").strip()

            if not new_id:
                print("Student ID cannot be empty.")
                continue

            parts = new_id.split("-")
            if (
                len(parts) != 3
                or len(parts[0]) != 2
                or len(parts[1]) != 4
                or len(parts[2]) != 6
                or not all(part.isascii() and part.isdigit() for part in parts)
            ):
                print("Invalid Student ID! Use this format: 02-0000-000000")
                continue

            appointment["student_id"] = new_id
            print("Student ID updated successfully.")
            break

    elif choice == "2":
        while True:
            new_name = input("Enter new student name: ").strip()

            if not new_name:
                print("Student name cannot be empty.")
                continue

            if not all(
                char.isalpha() or char.isspace() or char in ",.-'" for char in new_name
            ):
                print("Invalid Student Name! Numbers are not allowed.")
                continue

            appointment["student_name"] = new_name
            print("Student name updated successfully.")
            break

    elif choice == "3":
        new_section = input("Enter new student section: ").strip()

        if new_section:
            appointment["student_section"] = new_section
            print("Student section updated successfully.")
        else:
            print("Student section cannot be empty.")

    elif choice == "4":
        new_purpose = input("Enter new purpose: ").strip()

        if new_purpose:
            appointment["purpose"] = new_purpose
            print("Purpose updated successfully.")
        else:
            print("Purpose cannot be empty.")

    elif choice == "5":
        appointments.remove(appointment)
        selected = choose_schedule()

        if selected is None:
            appointments.append(appointment)
            print("Update cancelled. Original appointment retained.")
            return

        appointment["instructor"] = selected["instructor"]
        appointment["date"] = selected["date"]
        appointment["time"] = selected["time"]

        appointments.append(appointment)
        print("Appointment schedule updated successfully.")

    elif choice == "6":
        print("Returning to main menu.")

    else:
        print("Invalid choice.")

def cancel_appointment():
    print("\n<------------------------------------------>")
    print("            CANCEL APPOINTMENT")
    print("<------------------------------------------>")

    try:
        appointment_id = int(input("Enter appointment ID: "))
    except ValueError:
        print("Invalid appointment ID.")
        return

    appointment = find_appointment_by_id(appointment_id)

    if appointment is None:
        print("Appointment not found.")
        return

    if appointment["status"] == "Cancelled":
        print("This appointment is already cancelled.")
        return

    appointment["status"] = "Cancelled"
    print("Appointment cancelled successfully.")

def view_by_date():
    print("\n<------------------------------------------>")
    print("            VIEW APPOINTMENTS BY DATE")
    print("<------------------------------------------>")

    selected_date = get_valid_date(
        "Enter date to search (YYYY-MM-DD): "
    ).strftime("%Y-%m-%d")

    found = False

    for appointment in appointments:
        if appointment["date"] == selected_date:
            display_appointment(appointment)
            found = True

    if not found:
        print("No appointments found for", selected_date)

def update_status():
    print("\n<------------------------------------------>")
    print("          UPDATE APPOINTMENT STATUS")
    print("<------------------------------------------>")

    try:
        appointment_id = int(input("Enter appointment ID: "))
    except ValueError:
        print("Invalid appointment ID.")
        return

    appointment = find_appointment_by_id(appointment_id)

    if appointment is None:
        print("Appointment not found.")
        return

    print("1. Scheduled")
    print("2. Completed")
    print("3. Cancelled")

    choice = input("Choose new status: ").strip()

    status_options = {
        "1": "Scheduled",
        "2": "Completed",
        "3": "Cancelled"
    }

    if choice not in status_options:
        print("Invalid status choice.")
        return

    new_status = status_options[choice]

    if new_status == "Scheduled":
        for other in appointments:
            if (
                other["id"] != appointment["id"]
                and other["instructor"] == appointment["instructor"]
                and other["date"] == appointment["date"]
                and other["time"] == appointment["time"]
                and other["status"] == "Scheduled"
            ):
                print("Cannot reschedule status: this time is already booked.")
                return

    appointment["status"] = new_status
    print("Appointment status updated to", new_status)

def view_instructor_schedules():
    print("\n<------------------------------------------>")
    print("            INSTRUCTOR SCHEDULES")
    print("<------------------------------------------>")

    if not instructor_schedules:
        print("No instructor schedules available.")
        return

    for instructor, schedule in instructor_schedules.items():
        print(f"\nInstructor: {instructor}")

        if not schedule:
            print("  No available schedule.")
            continue

        for day, times in schedule.items():
            print(f"  {day}:")
            for time_range in times:
                print(f"    - {time_range}")


def update_student_information():
    """Wrapper for updating student-related appointment records."""
    update_appointment_information()
    
def appointment_summary():
    print("\n<------------------------------------------>")
    print("           APPOINTMENT SUMMARY")
    print("<------------------------------------------>")

    total = len(appointments)

    scheduled = sum(
        1 for appointment in appointments
        if appointment["status"] == "Scheduled"
    )

    completed = sum(
        1 for appointment in appointments
        if appointment["status"] == "Completed"
    )

    cancelled = sum(
        1 for appointment in appointments
        if appointment["status"] == "Cancelled"
    )

    print("Total Appointments     :", total)
    print("Scheduled Appointments :", scheduled)
    print("Completed Appointments :", completed)
    print("Cancelled Appointments :", cancelled)
def add_new_instructor():
    print("\n<------------------------------------------>")
    print("          ADD NEW INSTRUCTOR")
    print("<------------------------------------------>")

    new_instructor = input("Enter the name of the new instructor: ").strip()

    if not new_instructor:
        print("Instructor name cannot be empty.")
        return
    elif not all(char.isalpha() or char.isspace() or char in ",.-'" for char in new_instructor):
        print("Invalid Instructor Name! Numbers are not allowed.")
        return

    if new_instructor in instructors_list:
        print("This instructor already exists.")
        return

    instructors_list.append(new_instructor)
    instructor_schedules[new_instructor] = {}
    print(f"Instructor '{new_instructor}' added successfully.")

def remove_instructor():
    print("\n<------------------------------------------>")
    print("        REMOVE INSTRUCTOR")
    print("<------------------------------------------>")

    if not instructors_list:
        print("No instructors available to remove.")
        return

    for number, instructor in enumerate(instructors_list, start=1):
        print(f"{number}. {instructor}")

    while True:
        try:
            choice = int(input("Choose instructor number to remove: "))
            if 1 <= choice <= len(instructors_list):
                break
            print("Invalid choice. Please select a listed number.")
        except ValueError:
            print("Please enter a valid number.")

    instructor_to_remove = instructors_list[choice - 1]

    for appointment in appointments:
        if (appointment["instructor"] == instructor_to_remove and
                appointment["status"] == "Scheduled"):
            print(f"Cannot remove '{instructor_to_remove}'. There are scheduled appointments.")
            return

    instructors_list.remove(instructor_to_remove)
    del instructor_schedules[instructor_to_remove]
    print(f"Instructor '{instructor_to_remove}' removed successfully.")
def appointment_summary():
    print("\n<------------------------------------------>")
    print("           APPOINTMENT SUMMARY")
    print("<------------------------------------------>")

    total = len(appointments)

    scheduled = sum(
        1 for appointment in appointments
        if appointment["status"] == "Scheduled"
    )

    completed = sum(
        1 for appointment in appointments
        if appointment["status"] == "Completed"
    )

    cancelled = sum(
        1 for appointment in appointments
        if appointment["status"] == "Cancelled"
    )

    print("Total Appointments     :", total)
    print("Scheduled Appointments :", scheduled)
    print("Completed Appointments :", completed)
    print("Cancelled Appointments :", cancelled)


def admin_menu():
    while True:
        print("\n<------------------------------------------>")
        print("                ADMIN MENU")
        print("<------------------------------------------>")
        print("|1. View All Student Appointments        |")
        print("|2. Search Appointment Records           |")
        print("|3. View Instructor Schedules            |")
        print("|4. Manage Instructor Schedules          |")
        print("|5. View Appointments by Date            |")
        print("|6. View Appointment Summary             |")
        print("|7. Add New Instructor                   |")
        print("|8. Remove Instructor                    |")
        print("|9. Return to Main Menu                  |")
        print("<------------------------------------------>")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_appointments()
        elif choice == "2":
            search_appointment()
        elif choice == "3":
            view_instructor_schedules()
        elif choice == "4":
            update_instructor_schedule()
        elif choice == "5":
            view_by_date()
        elif choice == "6":
            appointment_summary()
        elif choice == "7":
            add_new_instructor()
        elif choice == "8":
            remove_instructor()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please select 1-9.")

def student_menu():
    while True:
        print("\n<------------------------------------------>")
        print("             STUDENT MENU")
        print("<------------------------------------------>")
        print("|1. Add Appointment                      |")
        print("|2. View Instructor Schedules            |")
        print("|3. View All Appointments                |")
        print("|4. Search Appointment                   |")
        print("|5. Update Student Information           |")
        print("|6. Cancel Appointment                   |")
        print("|7. View Appointments by Date            |")
        print("|8. Return to Main Menu                  |")
        print("<------------------------------------------>")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_appointment()
        elif choice == "2":
            view_instructor_schedules()
        elif choice == "3":
            view_appointments()
        elif choice == "4":
            search_appointment()
        elif choice == "5":
            update_student_information()
        elif choice == "6":
            cancel_appointment()
        elif choice == "7":
            view_by_date()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please select 1-8.")


def instructor_menu():
    while True:
        print("\n<------------------------------------------>")
        print("            INSTRUCTOR MENU")
        print("<------------------------------------------>")
        print("|1. View Recorded Student Appointments|")
        print("|2. Search Appointment Records        |")
        print("|3. Update Appointment Status         |")
        print("|4. View Appointments by Date         |")
        print("|5. Update Instructor Schedule        |")
        print("|6. instructor Schedule Summary       |")
        print("|7. Return to Main Menu               |")
        print("<------------------------------------------>")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_appointments()
        elif choice == "2":
            search_appointment()
        elif choice == "3":
            update_status()
        elif choice == "4":
            view_by_date()
        elif choice == "5":
            update_instructor_schedule()
        elif choice == "6":
            view_instructor_schedule_summary()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please select 1-7.")

def main():
    while True:
        print("\n<------------------------------------------>")
        print(" STUDENT APPOINTMENT AND SCHEDULING")
        print("       SYSTEM FOR CITE DEPARTMENT")
        print("<------------------------------------------>")
        print("1. Student Menu")
        print("2. Instructor Menu")
        print("3. Admin Menu")
        print("4. Exit")
        print("<------------------------------------------>")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_menu()
        elif choice == "2":
            instructor_menu()
        elif choice == "3":
            admin_menu()
        elif choice == "4":
            print("------------------------------------------------------------------------------------------------")
            print("THANK YOU FOR USING THE STUDENT APPOINTMENT AND SCHEDULING SYSTEM FOR CITE DEPARTMENT.")
            print("------------------------------------------------------------------------------------------------")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main() 