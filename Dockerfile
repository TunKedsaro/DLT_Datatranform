# FROM python:3.9-slim
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt
# COPY scripts /app/script
# ENTRYPOINT ["python", "/app/script/etl_script.py"]


# FROM python:3.9-slim
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt
# COPY scripts /app/scripts
# CMD ["tail","-f","/dev/null"]

# Use Python 3.9-slim as the base image
FROM python:3.9-slim
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file
COPY requirements.txt .
# Install dependencies and Jupyter
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install jupyter
# Copy the script folder into the container
COPY script /app/script
# Expose the port for Jupyter Notebook
EXPOSE 8888
# Set the default command to keep the container alive
CMD ["tail", "-f", "/dev/null"]
