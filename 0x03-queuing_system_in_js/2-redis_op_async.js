import { createClient } from 'redis';
import redis from 'redis';
import { promisify } from 'util';

const client = createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server');
})

client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
})

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value,  redis.print)
}

async function displaySchoolValue (schoolName) {
    try {
        const data = await getAsync(schoolName)
        console.log(data);
    } catch (err) {
        console.error(err);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');