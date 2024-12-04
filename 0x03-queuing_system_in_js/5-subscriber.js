import redis from 'redis';

const clint = redis.createClient();

clint.on('connect', () => {
    console.log('Redis client connected to the server');
    clint.subscribe('holberton school channel');
});

clint.on('message', (channel, message) => {
    console.log(`${message}`);
    if(message === "KILL_SERVER"){
        clint.unsubscribe(channel);
        clint.quit();
    }
});
clint.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});
