const express = require('express');
const axios = require('axios').default;
const client = require('./client')
const app = express()

app.get('/', async (req, res) => {
    const cachedData = await client.get('todos')
    if (cachedData) return res.send(JSON.parse(cachedData))

    const {data} = await axios.get('https://jsonplaceholder.typicode.com/todos');
    await client.set('todos',JSON.stringify(data))
    await client.expire('todos',30)
    res.json(data) 
})

app.listen(9000)