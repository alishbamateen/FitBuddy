const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

// In-memory database (you can use a real database later)
let stories = [];

app.use(bodyParser.json());
app.use(express.static('public'));  // Serve static files (HTML, CSS, JS)

// Endpoint to add a new story
app.post('/add-story', (req, res) => {
  const { story } = req.body;
  if (story) {
    stories.push(story);
    res.status(200).send({ message: 'Story added successfully!' });
  } else {
    res.status(400).send({ message: 'Story content is required' });
  }
});

// Endpoint to get a random story
app.get('/random-story', (req, res) => {
  if (stories.length > 0) {
    const randomStory = stories[Math.floor(Math.random() * stories.length)];
    res.status(200).send({ story: randomStory });
  } else {
    res.status(404).send({ message: 'No stories available' });
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
