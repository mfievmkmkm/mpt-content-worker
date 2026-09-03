FROM ghcr.io/harry0703/moneyprinterturbo:latest

WORKDIR /MoneyPrinterTurbo
COPY bootstrap.py /opt/content-os/bootstrap.py
EXPOSE 8080
CMD ["python", "/opt/content-os/bootstrap.py"]
