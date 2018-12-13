FROM ubuntu:latest
LABEL maintainer="Alexander Buitron <alex@buitron.com>"

# Create appuser
RUN groupadd -g 999 appuser && \
  useradd -r -u 999 -g appuser appuser

# Install linux dependencies
RUN apt-get update && apt-get install -y \
  wget \
  unzip \
  python3-dev \
  python3-pip \
  xvfb

# Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
  dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install && \
  rm -f /google-chrome-stable_current_amd64.deb

# Chromedriver
RUN wget https://chromedriver.storage.googleapis.com/2.44/chromedriver_linux64.zip && \
  unzip chromedriver_linux64.zip && \
  mv chromedriver /usr/bin/chromedriver && \
  chown appuser:appuser /usr/bin/chromedriver && \
  chmod +x /usr/bin/chromedriver && \
  rm -f /chromedriver_linux64.zip

COPY ./src/requirements.txt /tmp/requirements.txt

# Install python dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add source code
ADD ./src /opt/src/
WORKDIR /opt/src

RUN chown -R appuser:appuser /opt/*

# Clear cache
RUN rm -rf /var/lib/apt/lists/*

# Expose is NOT supported by Heroku
EXPOSE 5000

# Run the image as a non-root user
USER appuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD gunicorn --bind 0.0.0.0:5000 wsgi
