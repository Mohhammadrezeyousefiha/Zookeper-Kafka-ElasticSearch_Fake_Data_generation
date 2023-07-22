# Kafka Fake Data Producer and Elastic Consumer using docker and docker-compose example

- Running the kafka and zookeeper on the docker container
- Generating fake data and writing it on a kafka topic
- Putting data from kafka topic into elastic search (still not working properly I suppose!) 
- Created a producer and consumer in python language

### Installation

Install docker and docker-compose from official docker website and run the below commands

#### It will pull the official kafka and zookeeper and elastic search docker images and run it inside the kafka-network

```sh
$ cd kafka_and_zookeeper
$ sudo docker compose up -d
```
#### It will Build fake data producer code with desired structure
```sh
$ cd producer
$ ./build.sh
```
#### It will start generating fake data on a kafka topic named dataak
```sh
$ cd producer
$ ./start.sh
```

#### It will start building the docker file which puts kafka topic data into elastic search
```sh
$ cd consumer
$ ./build.sh
```

#### It will start running the docker file which puts kafka topic data into elastic search
```sh
$ cd consumer
$ ./start.sh
```

