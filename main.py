import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# 현재 폴더 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # 같은 폴더에 있는 idea-board.html 파일을 읽어서 전송
    file_path = os.path.join(BASE_DIR, "idea-board.html")
    
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return "<h1>파일을 찾을 수 없습니다. idea-board.html 파일이 있는지 확인하세요.</h1>"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
