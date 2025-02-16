const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve static files from the "frontend/public" folder
app.use(express.static(path.join(__dirname, '../frontend/public')));

// Route to serve the AI Coach page
app.get('/ai-coach', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/public/ai-coach.html'));
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});