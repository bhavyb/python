def explore_module():
    name = input("Enter module name: ")
    try:
        module = __import__(name)
        print("Available Attributes: ",dir(module))
        print("==============================")

    except Exception as e:
        print("Error:", e)
        print("==============================")
