import psutil

contador = 0
for proc in psutil.process_iter():
    if proc.name().lower() == "chrome.exe":
        contador += 1
        proc.kill()
        print("------------------------------")
    print(proc.name(), proc.pid)

print(contador)