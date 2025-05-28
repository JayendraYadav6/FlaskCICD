🛠️ DevOps Project: CI/CD Pipeline with Terraform, Jenkins & Flask
 
This project demonstrates a complete CI/CD pipeline setup from scratch using Terraform, Jenkins, GitHub, and Flask. It automates infrastructure provisioning, Jenkins setup, and deploys a Python Flask app which gets updated automatically using GitHub webhooks.
 
 
---
 
🧰 Tools & Technologies Used
 
Terraform: Infrastructure as Code (IaC) for provisioning AWS resources.
 
AWS: Hosting EC2 instance and VPC setup.
 
Jenkins: For CI/CD pipeline and deployment automation.
 
GitHub Webhooks: To trigger Jenkins on code changes.
 
Flask: Simple Python web application.
 
Docker: to containerize the Flask app.
 
 ----
 
🧱 Infrastructure Provisioning with Terraform
 
The infrastructure setup includes:
 
Custom VPC, subnet, internet gateway
 
Security Groups allowing port 22 (SSH), 8080 (Jenkins), and 5002 (Flask App)
 
EC2 instance with user data to install Jenkins
 
 <img width="766" alt="image" src="https://github.com/user-attachments/assets/843deffa-26fe-4f3b-bb6e-821611406516" />



---
 
⚙️ Jenkins Setup & Configuration
 
After provisioning, Jenkins is configured with a pipeline job that:
 
1. Pulls code from GitHub
 
 
2. Installs dependencies (requirements.txt)
 
 
3. Runs the Flask app on port 5002
 
 
 
<img width="944" alt="image" src="https://github.com/user-attachments/assets/dfd7e93a-ad45-454b-a08a-472a8dd94c30" />

---
 
🚀 CI/CD Pipeline Workflow
 
A GitHub webhook is configured to trigger Jenkins whenever code is pushed.
 
Jenkins pulls the latest code, installs dependencies, and restarts the Flask app.
 
All updates are reflected in real-time on the EC2 instance (port 5002).
 
 
 
---
 
🧪 Flask App & Requirements
 
This is a simple web app created using Flask.
 
<img width="472" alt="image" src="https://github.com/user-attachments/assets/e30d5d7d-fa71-433f-a96b-6697ceb03d5a" />

---
 
🔗 How to Run This Project
 
1. Clone the Repo
 
git clone https://github.com/yourusername/your-repo.git
cd your-repo
 
2. Provision Infrastructure with Terraform
 
terraform init
terraform apply
 
3. Access Jenkins
 
SSH into the EC2 instance.
 
Open Jenkins on http://<ec2-ip>:8080.
 
 
4. Setup Jenkins Pipeline
 
Create a new pipeline job.
 
Paste the pipeline script from the repo.
 
 
5. Push to GitHub & Watch CI/CD in Action
 
Make any code change.
 
Push it to GitHub.
 
See Jenkins automatically build and deploy it to port 5002.
 
<img width="368" alt="image" src="https://github.com/user-attachments/assets/903a2888-e6ea-497b-a23e-5a3818ed079a" />

 
---
 
📸 Project Highlights
 
✅ Real-time updates via GitHub Webhooks
 
✅ Fully automated deployment
 
✅ Clean Terraform setup
 
✅ Jenkins + Flask integration
