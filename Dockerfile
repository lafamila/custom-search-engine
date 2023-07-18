FROM python:3.8.2-slim-buster as builder

RUN mkdir /se-service
COPY /src/. /se-service
WORKDIR /se-service

RUN apt-get update \
      && apt-get install -y --no-install-recommends gcc libc-dev \
      && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
      && pip install --user -r requirements.txt

RUN apt-get purge -y --auto-remove gcc libc-dev

FROM python:3.8.2-slim-buster

COPY --from=builder /se-service /se-service
COPY --from=builder /root/.local /root/.local

WORKDIR /se-service

ENV PATH=/root/.local:$PATH

CMD ["python", "./__main__.py"]