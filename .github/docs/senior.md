# CRUK Node.js Recruitment Assignment - Senior level

### Functional Requirements

Build a simple service in Node.js that can be deployed to AWS which exposes an API and can be consumed from any client.

This service should check how many donations a user has made and send them a thank you message (e.g. via SNS) if they make 2 or more donations.

### Output Package Requirements

The solution has to be provided as a Github repository including full commit history.

Please follow the frequent commit practice so that your local repository indicates reasonable milestones of your implementation.

The repository MUST contain:
- Source code
    - It should be buildable/viewable.
    - It must be written in Typescript.
    - In case you need to use external libraries, please add them.
- Basic tests.

This repository SHOULD contain:
- Infrastructure as Code. 
We use the AWS CDK and encourage you to use this also, but we will accept the use of Cloudformation or Terraform if you feel more comfortable with these technologies.
- README file with URL for testing the service online and a brief explanation on the scalability strategy.
- Any installation and deployment instructions for apps and components.

### Guidelines

If you do not complete the test please indicate how you would intend to finalize it in the README.

The team is looking to see how you approach a problem with a broad spec which could have a number of different solutions and then explaining your approach. Keep the implementation simple, but make sure you have basic tests, logging (structured logs with JSON), and include information in the README about how you'll scale the solution to thousands of users, how you'd approach logging & monitoring at scale so that you can actually debug the system as it increases in complexity.

We are not expecting the solution to be deployed, but we expect you to understand the process and best practices around the deployment process. It’s enough if you could provide to our engineers clear and easy instructions on how to deploy your application.
