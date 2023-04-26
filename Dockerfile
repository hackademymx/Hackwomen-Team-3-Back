# For more information, please refer to https://aka.ms/vscode-docker-pyhton
FROM python:3.11.2-bullseye

EXPOSE 8000

# Keeps Pyhton from generating .pyc file in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUMBUFFERED=1

# Intall pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Required in Windows and MAC OS to run the entrypoint.sh script
RUN sed -i 's/\r$//' /usr/local/bin/entrypoint.sh \
    && chmod 744 /usr/local/bin/entrypoint.sh

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-pyhton-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For mor information, please refer to https://aka.ms/vscode-docker-pyhton-debugging
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi"]
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
CMD ["gunicorn", "core.wsgi"]
