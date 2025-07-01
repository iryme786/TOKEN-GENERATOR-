const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.post('/token', async (req, res) => {
  const { mobile, orgCode } = req.body;

  try {
    const response = await axios.post('https://webapi.classplus.co/webapi/v1/login', {
      mobile: mobile,
      orgCode: orgCode
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    });

    const token = response.data.token || response.data.data?.token;
    if (token) {
      res.json({ token });
    } else {
      res.status(400).json({ error: 'Token not found in response' });
    }
  } catch (error) {
    res.status(400).json({ error: 'Invalid request or blocked by Classplus' });
  }
});

app.get('/', (req, res) => {
  res.send('Classplus Token Generator API');
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
