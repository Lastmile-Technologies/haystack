FROM deepset/haystack:cpu

USER root

#
### Install dependencies
##RUN pip install -r requirements.txt
#
## Create pipelines directory
RUN mkdir -p /opt/models
COPY models /opt/models
COPY rest_api/rest_api/controller /opt/venv/lib/python3.10/site-packages/rest_api/controller
COPY FILEUPLOADTEST.py /opt/FILEUPLOADTEST.py
#
## Copy pipelines config file
#COPY rest_api/rest_api/pipeline /opt/pipelines
#
## Expose ports
#EXPOSE 8000
#
## Set working directory
WORKDIR /opt/haystack
#
## Run Haystack API
##CMD ["haystack-api8"]