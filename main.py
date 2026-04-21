import datetime
import calendar

class CalendarEventScheduler:
    def __init__(self):
        self.events = {}

    def add_event(self, date, event_name, start_time, end_time):
        if date not in self.events:
            self.events[date] = []
        self.events[date].append({
            'event_name': event_name,
            'start_time': start_time,
            'end_time': end_time
        })

    def remove_event(self, date, event_name):
        if date in self.events:
            self.events[date] = [event for event in self.events[date] if event['event_name'] != event_name]

    def get_events(self, date):
        if date in self.events:
            return self.events[date]
        else:
            return []

    def print_events(self, date):
        events = self.get_events(date)
        if events:
            print(f"Events on {date}:")
            for event in events:
                print(f"{event['event_name']}: {event['start_time']} - {event['end_time']}")
        else:
            print(f"No events on {date}")

    def schedule_event(self, date, event_name, start_time, end_time):
        self.add_event(date, event_name, start_time, end_time)
        self.print_events(date)

    def cancel_event(self, date, event_name):
        self.remove_event(date, event_name)
        self.print_events(date)


def main():
    scheduler = CalendarEventScheduler()

    while True:
        print("\n1. Schedule event")
        print("2. Cancel event")
        print("3. Get events")
        print("4. Print events")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            event_name = input("Enter event name: ")
            start_time = input("Enter start time (HH:MM): ")
            end_time = input("Enter end time (HH:MM): ")
            scheduler.schedule_event(date, event_name, start_time, end_time)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            event_name = input("Enter event name: ")
            scheduler.cancel_event(date, event_name)
        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): ")
            events = scheduler.get_events(date)
            if events:
                for event in events:
                    print(f"{event['event_name']}: {event['start_time']} - {event['end_time']}")
            else:
                print("No events on this date")
        elif choice == "4":
            date = input("Enter date (YYYY-MM-DD): ")
            scheduler.print_events(date)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

Bu kod Calendar Event Scheduler uchun ishlaydi. U quyidagi funktsiyalarni qo'llaydi:

* `add_event`: Tungi vaqti orasida tadbir qo'shish
* `remove_event`: Tungi vaqti orasida tadbir o'chirish
* `get_events`: Tungi vaqti orasida tadbirlarni olish
* `print_events`: Tungi vaqti orasida tadbirlarni chiqarish
* `schedule_event`: Tungi vaqti orasida tadbir qo'shish va chiqarish
* `cancel_event`: Tungi vaqti orasida tadbir o'chirish va chiqarish

Kodda Calendar Event Scheduler uchun ishlaydigan dastur yozilgan. Dastur quyidagi funktsiyalarni qo'llaydi:

* `main`: Dasturning asosiy funktsiyasi. U quyidagi funktsiyalarni qo'llaydi:
 + `schedule_event`: Tungi vaqti orasida tadbir qo'shish
 + `cancel_event`: Tungi vaqti orasida tadbir o'chirish
 + `get_events`: Tungi vaqti orasida tadbirlarni olish
 + `print_events`: Tungi vaqti orasida tadbirlarni chiqarish
 + `exit`: Dasturni tugatish
