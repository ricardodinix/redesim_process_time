FROM python
CMD [ "pip install -r requirements.txt" ]
VOLUME [ "/data" ]