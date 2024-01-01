from fastapi import FastAPI

app = FastAPI()

@app.get("/Server/{server}")
def Server_model(server: str):
    #return {"servername": server}

    import subprocess, sys
    p = subprocess.run(["powershell.exe", 
                f"C:\Python_Swagger_App\Memoryfinalpowershell.ps1 {server}"], 
                capture_output= True,text= True)
    output = p.stdout
    print(output)
    return output