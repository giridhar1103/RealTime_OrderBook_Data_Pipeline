# RealTime_OrderBook_Data_Pipeline


### Running cassandra on a local machine(windows):
To run a cassandra database on our windows local machine, we can use a docker container which has cassandra installed in it. Open command prompt or powershell and enter:

```bash
docker run --name cassandra -d -p 9042:9042 cassandra
```
This code pulls cassandra from docker hub and creates a cassandra image where you can store data in a docker container.

Check cassandra's official website (https://cassandra.apache.org/) to install it according to your needs.

Now we access the bash of this cassandra container from our cmd/terminal by running the code:
```bash
docker exec -it <your_cass_container_name> bash
```
This will let you access the bash of the cassandra container. From here we can run commands to open cqlsh:

```bash
cqlsh
```

