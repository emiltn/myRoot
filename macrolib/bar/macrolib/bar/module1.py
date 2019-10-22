#print("Importing: bar.module1")

def multiply(o, value):
    o.x *= value

def main():
    print("This works: bar.module1")

if __name__ == "__main__":
    print("Running as main: 'bar.module1'")
