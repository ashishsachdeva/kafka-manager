FROM confluentinc/cp-kafka:3.0.0
RUN apt-get update && apt-get install -y vim && apt-get install unzip
      
ADD target/universal/kafka-manager-1.3.3.8.zip /usr/local/kafka-manager/    
COPY docker/entry /usr/local/kafka-manager/
COPY docker/utils.py /usr/local/kafka-manager/

EXPOSE 9000

RUN chmod 777 /usr/local/kafka-manager/entry && mkdir /tmp/kafka-manager-logs
WORKDIR /usr/local/kafka-manager/
RUN unzip kafka-manager-1.3.3.8.zip
CMD ["bash","-c","/usr/local/kafka-manager/entry"]
