// script.js
document.getElementById('resumeForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
    
    // Get form values
    const objective = document.getElementById('objective').value;
    const contact = document.getElementById('contact').value;
    const address = document.getElementById('address').value;
    const email = document.getElementById('email').value;
    const linkedin = document.getElementById('linkedin').value;
    const skills = document.getElementById('skills').value;
    
    // You can collect other field values similarly
    
    // Create an object to hold the collected data
    const resumeData = {
      objective: objective,
      contact: contact,
      address: address,
      email: email,
      linkedin: linkedin,
      skills: skills
      // Add other fields as needed
    };
    
    // For now, let's just log the collected data
    console.log(resumeData);
    // You can do more with this data, like displaying a preview or sending it to a server
    
    // You can also reset the form after submission if needed
    // event.target.reset();
  });
  function addProject() {
    const projectsContainer = document.getElementById('projects');
  
    const newProject = document.createElement('div');
    newProject.classList.add('project');
  
    newProject.innerHTML = `
      <label for="projectName">Project Name:</label>
      <input type="text" class="projectName" name="projectName[]">
  
      <label for="projectDescription">Project Description:</label>
      <textarea class="projectDescription" name="projectDescription[]" rows="3" cols="50"></textarea>
  
      <label for="technologiesUsed">Technologies Used:</label>
      <input type="text" class="technologiesUsed" name="technologiesUsed[]">
    `;
  
    projectsContainer.appendChild(newProject);
  }
  // script.js
function addExperience() {
    const experiencesContainer = document.getElementById('workExperience');
  
    const newExperience = document.createElement('div');
    newExperience.classList.add('experience');
  
    newExperience.innerHTML = `
      <label for="jobTitle">Job Title:</label>
      <input type="text" class="jobTitle" name="jobTitle[]">
  
      <label for="companyName">Company Name:</label>
      <input type="text" class="companyName" name="companyName[]">
  
      <label for="jobDescription">Job Description:</label>
      <textarea class="jobDescription" name="jobDescription[]" rows="3" cols="50"></textarea>
  
      <label for="workDuration">Duration:</label>
      <input type="text" class="workDuration" name="workDuration[]">
    `;
  
    experiencesContainer.appendChild(newExperience);
  }