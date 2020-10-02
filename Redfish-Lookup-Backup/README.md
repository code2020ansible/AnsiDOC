# Part 1: Redfish Serial Number Lookup

## Prerequisites

- Set up a `table.csv` file and create a directory for backups.

```sh
mkdir backup
```

## Simulating Redfish Servers

Start the docker swarm:

```sh
docker build -t rfsim .
docker-compose up
```

This starts up 3 instances of HTTP servers that respond to `/redfish/v1/Systems/1` on ports 8001, 8002, 8003

## Run the Playbook

```sh
ansible-playbook populate_redfish_serial_numbers.yml
```

> Warning: This command rewrites the `table.csv` file (but there is a backup).
