from FastAPIApp import app
import uvicorn

if __name__ == "__main__":
    print("open app by: http://127.0.0.1:3000/")
    uvicorn.run(app, host="0.0.0.0", port=3000)
