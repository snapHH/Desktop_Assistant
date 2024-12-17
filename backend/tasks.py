import os

def open_application(app_name):
    app_paths = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
    }

    if app_name.lower() in app_paths:
        os.system(app_paths[app_name.lower()])
        return {"status": "success", "message": f"Opened {app_name}"}
    else:
        return {"status": "error", "message": f"Application {app_name} not found"}
