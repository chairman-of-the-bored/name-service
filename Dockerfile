FROM python:onbuild
EXPOSE 7777
CMD ["python", "serve.py"]