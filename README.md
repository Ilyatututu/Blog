# Blog

## Установка

git clone https://github.com/Ilyatututu/Blog.git
cd Blog
python3 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
uvicorn main:app --reload