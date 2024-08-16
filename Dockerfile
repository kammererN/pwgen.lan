#
# Docker image for pwgen.lan
#
# Clone debian image
FROM debian

# Clone git repository
RUN git clone https://github.com/kammererN/pwgen.lan.git

# Switch to app folder
WORKDIR /pwgen.lan

# Create venv
RUN python3 -m venv venv

# Activate venv
RUN source ./venv/bin/activate

# Clone venv
RUN pip install -r 'requirements.txt' 

# Expose port 5000
EXPOSE 5000

# Call Gunicorn
CMD ["gunicorn", "-w", "4", "'app:app'"]
