import importlib
from sys import argv

if __name__ == '__main__':
    assert len(argv) == 2, f"Usage: {argv[0]} <task_name>"

    module_name = f"tasks.{argv[1]}"
    print("Trying to import task module: " + module_name)
    try:
        # Import the module dynamically
        module = importlib.import_module(module_name)
        print(f"Module '{module_name}' imported successfully!")

    except ImportError:
        print(f"Error: Module '{module_name}' not found or cannot be imported.")
        exit(1)


    task = module.Task(debug=True)
    res = task.solve()

    assert 'code' in res, f"Error, code not found in response: {res}"
    if res['code'] == 0:
        print(f"✅\tSuccess: {task} has been resolved")
    else:
        print(f"❌\tOh, no! {task} has not been accepted. Try again!")
