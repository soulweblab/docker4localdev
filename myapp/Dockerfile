ARG python_tag
FROM tiangolo/uwsgi-nginx-flask:$python_tag

WORKDIR /app/

# Install app requirements
COPY ./app/ ./
RUN pip install --no-cache-dir -r requirements.txt
