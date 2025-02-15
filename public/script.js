document.getElementById('submitStory').addEventListener('click', async () => {
    const storyInput = document.getElementById('storyInput').value;
    if (storyInput) {
      try {
        const response = await fetch('/add-story', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ story: storyInput }),
        });
        const data = await response.json();
        alert(data.message);
        document.getElementById('storyInput').value = ''; // Clear input after submission
      } catch (error) {
        alert('Error adding story!');
      }
    } else {
      alert('Please enter a story!');
    }
  });
  
  document.getElementById('fetchStory').addEventListener('click', async () => {
    try {
      const response = await fetch('/random-story');
      const data = await response.json();
      document.getElementById('randomStory').textContent = data.story || 'No stories available.';
    } catch (error) {
      alert('Error fetching random story!');
    }
  });
  