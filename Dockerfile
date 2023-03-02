FROM pypy:latest 
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_md
RUN python -m spacy download en_core_web_sm
CMD python garden.py