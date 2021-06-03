FROM python:3.7
# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get upgrade -y --only-upgrade && \
    apt-get install -y --no-install-recommends netcat
# Creation of the workdir
RUN mkdir /dj_elk
WORKDIR /dj_elk
# Add requirements.txt file to container
ADD requirements.txt /dj_elk/
# Install requirements
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
# Add the current directory(the web folder) to Docker container
ADD . /dj_elk/
COPY boot-strap.sh ./
RUN chmod +x /dj_elk/boot-strap.sh
ENTRYPOINT ["sh","/dj_elk/boot-strap.sh"]