# Part 1: Redfish Serial Number Lookup

## Simulating Redfish Servers

On any host (just be sure `table.csv` has the right IP address), run:

```sh
docker build -t rfsim .
docker-compose up
```

## Run the Playbook

On the host with Ansible installed, run:

```sh
mkdir backups  # if the directory does not already exist
ansible-playbook populate_redfish_serial_numbers.yml
```

> Warning: This command rewrites the `table.csv` file (but there is a backup).
