def UserDoesNotExists(email: str):
    msg = f"User does not exists with email: {email}"
    return {"message": msg}
