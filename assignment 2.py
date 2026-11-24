def format_section(func):
    def wrapper(self, *args, **kwargs):
        print("\n" + "=" * 50)
        print("REPORT SECTION")
        print("=" * 50)
        result = func(self, *args, **kwargs)
        print("=" * 50)
        return result
    return wrapper


class Report:
    
    report_count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.sections = []

        Report.report_count += 1
        self.report_id = Report.report_count

    
    def __str__(self):
        return f"Report ID: {self.report_id} | Title: {self.title} | Author: {self.author}"

    
    def __len__(self):
        return len(self.sections)

    
    @classmethod
    def get_report_count(cls):
        return cls.report_count

    
    @format_section
    def add_section(self, heading, content):
        self.sections.append((heading, content))
        print("Section added successfully!")

    
    def display_report(self):
        print("\n" + "#" * 60)
        print("REPORT")
        print("#" * 60)

        print("Report ID :", self.report_id)
        print("Title     :", self.title)
        print("Author    :", self.author)

        print("-" * 60)

        for heading, content in self.sections:
            print("\n" + heading.upper())
            print("-" * len(heading))
            print(content)

        print("\n" + "#" * 60)



def create_report():
    print("\n===== CREATE NEW REPORT =====")

    title = input("Enter report title: ")
    author = input("Enter author name: ")

    report = Report(title, author)

    print("\nReport created successfully!")
    print(report)

    return report


# Main program
report = None

while True:
    print("\n========== DYNAMIC REPORT GENERATOR ==========")
    print("1. Create New Report")
    print("2. Add Report Section")
    print("3. Display Report")
    print("4. Display Number of Sections")
    print("5. Display Total Reports Created")
    print("6. Exit")
    print("===============================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        report = create_report()

    elif choice == "2":
        if report is None:
            print("Please create a report first!")
        else:
            heading = input("Enter section heading: ")
            content = input("Enter section content: ")

            report.add_section(heading, content)

    elif choice == "3":
        if report is None:
            print("Please create a report first!")
        else:
            report.display_report()

    elif choice == "4":
        if report is None:
            print("Please create a report first!")
        else:
            print("Number of sections:", len(report))

    elif choice == "5":
        print("Total reports created:",
              Report.get_report_count())

    elif choice == "6":
        print("Thank you for using Dynamic Report Generator!")
        break

    else:
        print("Invalid choice! Please try again.")
