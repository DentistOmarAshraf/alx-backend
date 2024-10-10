import redis from 'redis';

const client = redis.createClient()
const channel = 'holberton school channel'

client.on('connect', () => {
    console.log('Redis client connected to the server');
})

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
})

const publishMessage = (message, timeout) => {
    setTimeout(() => {
        client.publish(channel, message, (err, replay) => {
            if (err) {
                console.error(`Error Cannot Publish: ${message}`)
            } else {
                console.log(`About to send ${message}`)
            }
        })
    }, timeout);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);