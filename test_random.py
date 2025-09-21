import win32api

location = (win32api.GetCursorPos())
print("Larry, it's over there: " + str(location))
