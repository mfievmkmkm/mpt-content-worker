FROM ghcr.io/harry0703/moneyprinterturbo:latest

WORKDIR /MoneyPrinterTurbo
USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends fonts-dejavu-core \
    && cp /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf /MoneyPrinterTurbo/resource/fonts/DejaVuSans-Bold.ttf \
    && rm -rf /var/lib/apt/lists/*
COPY bootstrap.py /opt/content-os/bootstrap.py
EXPOSE 8080
CMD ["python", "/opt/content-os/bootstrap.py"]
