FROM python:3.10-slim

WORKDIR /usr/src/app

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Set uvicorn as entrypoint
ENTRYPOINT ["uvicorn"]

# Pass app module as argument
CMD ["app:app"]





# Second way

#FROM python:latest
#
#WORKDIR /usr/src/app
#
#COPY requirements.txt ./
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY . .
#
#CMD ["python", "app.py"]