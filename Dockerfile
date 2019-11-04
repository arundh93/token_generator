FROM continuumio/miniconda

RUN mkdir -p /home/privacy_service

COPY environment.yml /home/privacy_service/environment.yml

RUN conda env create -f /home/privacy_service/environment.yml

WORKDIR /home/privacy_service
COPY . /home/privacy_service

RUN chmod +x startup.sh

# expose is not working. need to do explicit port mapping while running
EXPOSE 5000
ENTRYPOINT ["/home/privacy_service/startup.sh"]
