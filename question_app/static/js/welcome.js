const getStartedBtn = document.getElementById('get-started-btn');

getStartedBtn.addEventListener('click', () => {
  // Simulate a button click animation (optional)
  getStartedBtn.style.transform = 'scale(0.9)';
  setTimeout(() => {
    getStartedBtn.style.transform = 'scale(1)';
  }, 100);

  // Redirect user to a new page or section
  window.location.href = "register_user/";  // Replace with your actual URL
});