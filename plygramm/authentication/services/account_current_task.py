def get_student_current_task(account):
    if account["role"] == "Student":
        return account["current_task"]
    return None
