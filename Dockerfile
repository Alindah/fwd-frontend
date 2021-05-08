# Building the image: docker build -t alindah/fwd_fe:1.0 . 
# Starting the container: docker run -p 8000:8000 alindah/fwd_fe:1.0
# Note: The ports we choose match the ones we expose.

FROM python:3.9-alpine
COPY . /fwd
WORKDIR /fwd
RUN pip install -r requirements.txt
ENV PORT=8000
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["fwd_fe.py"]