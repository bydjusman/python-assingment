class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

# Creating objects
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Displaying the count
Counter.show_count()
