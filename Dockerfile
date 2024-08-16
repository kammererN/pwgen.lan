
# Clone Debian
FROM debian

# Install git, python3 & pwgen
RUN apt update
RUN apt install -y git python3 python3-pip pwgen

# Clone git repository
RUN git clone https://github.com/kammererN/pwgen.lan.git

# Switch to app folder
WORKDIR /pwgen.lan

# Clone env
RUN pip install -r 'requirements.txt' --break-system 

# Expose port 5000
EXPOSE 5000

# CD to
WORKDIR ./app

# Call Gunicorn
CMD ["gunicorn", "-w", "4", "app:app", "--bind", "0.0.0.0:8000"]
