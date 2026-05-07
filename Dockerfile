FROM python:3.12

WORKDIR /app

# copy requirements trước để cache tốt hơn
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy toàn bộ source
COPY . .

# expose port FastAPI
EXPOSE 8000

# chạy app
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
