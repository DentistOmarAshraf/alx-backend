import redis from 'redis'
import { promisify } from 'util';

const client = redis.createClient()

client.on('connect', () => {
    console.log('Redis client connected to the server');
})

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${error.message}`)
})

const values = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
}

const flatValue = Object.entries(values).flat()

client.hset('HolbertonSchools', ...flatValue, redis.print);
client.hgetall('HolbertonSchools', (err, replay) => {
    console.log(replay);
})
