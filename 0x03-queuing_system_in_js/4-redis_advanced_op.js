import redis from 'redis';
import util from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function hsetNewSchool() {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

function displayHashValue() {
  client.hgetall('HolbertonSchools', (err, result) => {
    if (err) throw err;
    else {
    console.log(result);
  }
});
}

function main() {
  displayHashValue();
  hsetNewSchool();
  displayHashValue();
}
