FROM python:3.5
RUN apt update
RUN apt install -y git
WORKDIR /usr/src/app
RUN git clone https://github.com/DMTF/Redfish-Interface-Emulator
COPY modifications/emulator-config.json ./Redfish-Interface-Emulator/infragen/populate-config.json
COPY modifications/ComputerSystem.py ./Redfish-Interface-Emulator/api_emulator/redfish/templates/ComputerSystem.py
RUN sed -i 's/MarkupSafe==1.0/MarkupSafe==1.1.1/' ./Redfish-Interface-Emulator/packageSets/Env-Local-Python3.5.2_requirements.txt
RUN pip install -r ./Redfish-Interface-Emulator/packageSets/Env-Local-Python3.5.2_requirements.txt
WORKDIR /usr/src/app/Redfish-Interface-Emulator
CMD [ "python", "./emulator.py"]
