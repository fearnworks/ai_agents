FROM python:3.9

WORKDIR /app
RUN pip install streamlit
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .

WORKDIR /app/

ENV PATH="/root/.local/bin:${PATH}"

EXPOSE 8501
EXPOSE 7000

CMD python server.py 