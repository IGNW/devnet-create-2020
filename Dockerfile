FROM python:3.8-alpine

# install ssh client and git
RUN apk add --update --no-cache openssh-client git 

# clone our private repository
RUN git clone https://github.com:IGNW/devnet-create-2020.git && cd devnet-create-2020 && git checkout jacobs-add-flask-gui-to-repo 

RUN git clone https://github.com:IGNW/dc_2020_aci_tenants.git devnet-create-2020/repos/dc_2020_aci_tenants

WORKDIR /devnet-create-2020
RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP devnet_create_2020.py
CMD ["flask", "run", "--host", "0.0.0.0"]