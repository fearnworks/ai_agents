FROM python:3.9

WORKDIR /app
RUN pip install streamlit
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .

WORKDIR /app/src

ENV PATH="/root/.local/bin:${PATH}"

EXPOSE 8501

CMD ["streamlit", "run", "main.py", ]