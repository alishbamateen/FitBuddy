// Sample API URL to get workouts (you can replace this with any workout API endpoint)
const workoutAPI = 'https://api.example.com/workouts'; // Replace with actual API URL

document.getElementById('getExercises').addEventListener('click', async () => {
  const bodyPart = document.getElementById('bodyPart').value;

  try {
    // Fetch data from the API based on the selected body part
    const response = await fetch(`${workoutAPI}?bodyPart=${bodyPart}`);
    const data = await response.json();

    // Display the fetched exercises
    const exerciseResults = document.getElementById('exerciseResults');
    exerciseResults.innerHTML = ''; // Clear any previous results

    // Loop through the data and add each exercise to the list
    data.exercises.forEach(exercise => {
      const listItem = document.createElement('li');
      listItem.innerHTML = `<strong>${exercise.name}</strong><br>Equipment: ${exercise.equipment}`;
      exerciseResults.appendChild(listItem);
    });
  } catch (error) {
    console.error('Error fetching workout data:', error);
    alert('Failed to fetch exercises. Please try again.');
  }
});
