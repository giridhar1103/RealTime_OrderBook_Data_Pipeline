# RealTime_OrderBook_Data_Pipeline


### Running python script to mimic a cryptocurrency api:
We will be running scripts *producer1,2,3* on our ec2 instance which will contain kafka streaming services which will mimic that of an api. [linklol](data)

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

### Connect cassandra to tableau:
To connect our cassandra database to tableau, we use a OBD Connector. Go to https://insightsoftware.com/drivers/cassandra-odbc-jdbc/ and download the trial version, follow the instructions to set it up and
then configure user DSN where we will enter the host name as "localhost", port as "9042", default keyspace name as your desired keyspace (here it is cryptoorderbook).

Next, go to tableau and create a new book, then go to new data souce. Now you can add your simba OBDC here and select your database name, schema and table name. You will see the data get updated on the right side.

*insert img*

