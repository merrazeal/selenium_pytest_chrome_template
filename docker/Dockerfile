FROM python:3.11

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PYTHONPATH=/app

WORKDIR /app

COPY ./docker/requirements.txt /

RUN pip install --upgrade pip --no-cache-dir \
    && pip install -r /requirements.txt --no-cache-dir

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor | tee /etc/apt/trusted.gpg.d/google.gpg >/dev/null \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install google-chrome-stable \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

COPY ./docker/wrap_chrome_binary /opt/bin/wrap_chrome_binary

RUN chmod +x /opt/bin/wrap_chrome_binary \
  && /opt/bin/wrap_chrome_binary

RUN CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+)(\.[0-9]+){3}.*/\1/") \
    && echo "Geting ChromeDriver latest version from https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_MAJOR_VERSION}" \
    && CHROME_DRIVER_VERSION=$(wget -qO- https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_MAJOR_VERSION} | sed 's/\r$//') \
    && CHROME_DRIVER_URL=https://storage.googleapis.com/chrome-for-testing-public/$CHROME_DRIVER_VERSION/linux64/chromedriver-linux64.zip \
    && echo "Using ChromeDriver from: $CHROME_DRIVER_URL" \
    && echo "Using ChromeDriver version: $CHROME_DRIVER_VERSION" \
    && wget --no-verbose -O /tmp/chromedriver_linux64.zip $CHROME_DRIVER_URL \
    && rm -rf /opt/selenium/chromedriver \
    && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
    && rm /tmp/chromedriver_linux64.zip \
    && mv /opt/selenium/chromedriver-linux64/chromedriver /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
    && chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
    && ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver

RUN mkdir -p /app/tmp/downloads && mkdir -p /app/tmp/screenshots

COPY ./src /app

CMD ["pytest", "-s"]
