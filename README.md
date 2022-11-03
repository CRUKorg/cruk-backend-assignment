# CRUK Node.js Recruitment Assignment

**Note - for the Python version of this exercise please click [[HERE](https://github.com/CRUKorg/cruk-backend-assignment/tree/python-version)]**

### Functional Requirements

Build a service in Node.js that can be deployed to AWS which exposes an API and can be consumed from any client. 

This service should check how many donations a user has made and send them a special thank you message (e.g. via SNS) if they make 2 or more donations. 

### Output Package Requirements

The solution has to be provided as a Github repository including full commit history.

Please follow the frequent commit practice so that your local repository indicates reasonable milestones of your implementation.

The repository MUST contain:

- Source code
    - It should be buildable/viewable.
    - It must be written in Typescript.
    - In case you need to use external libraries, please add them.
- Infrastructure as Code (We use the AWS CDK and encourage you to use this also, but we will accept the use of Cloudformation or Terraform if you feel more comfortable with these technologies). Please refrain from using the Serverless Framework for this task.
- Adequate tests.
- Any installation and deployment instructions for apps and components.
- README file with URL for testing the service online and a brief explanation on the scalability strategy.

### Rules

If you do not complete the test please indicate how you would intend to finalise it in the README. 

The team is looking to see how you approach a problem with a broad spec which could have a number of different solutions and then explaining your approach? Keep the implementation simple, but make sure you have automated tests, logging (structured logs with JSON), and include information in the README about how you'll scale the solution to thousands of users, how you'd approach logging & monitoring at scale so that you can actually debug the system as it increases in complexity.

We are not expecting the solution to be deployed, but we expect you to understand the process and best practices around the deployment process. It’s enough if you could provide to our engineers clear and easy instructions on how to deploy your application.

### FAQ's

*Any client - what are the clients?*

A client is a consumer of the API (e.g. web app, another backend service, a mobile app, etc). In this case "Any client" means for us, the API can and should be implemented independently of who/what is going to consume it.

*Does this sit behind an API Gateway?*

Whilst this is not strictly required, it’s just one of various solutions on AWS for exposing your API

*How is authentication performed?*

We are not looking at the implementation of the authentication in the code challenge.

*Will the API receives a token in the header (JWT with authentication service defined)?*

Not necessarily, as per the answer above the authentication is not required for this task.

*Will only certain roles be able to call the API (eg, AWS IAM Permissions with AWS API Gateway)?*

Again, no authorisation or permissions are expected to be set for the coding challenge. We can discuss these things during the F2F interview.

*Will I need to persist donations data in a database?*

Most candidates have used an in-memory store which saves them time to provision and deploy machines/databases. If you want to use a specific data store we don’t have any objection.

*Is there a standardised/preferred method of logging?*

We don’t expect the coding challenge to be production-ready and ship logs anywhere but having basic error handling is considered a minimum requirement. You will definitely get extra points if you handle and log successfully edge-cases and critical paths (e.g. fatal errors).

*In terms of deploying to AWS, should I include a build pipeline or can that be done manually?*

Do it manually, it's a one-time thing

*Can we implement this using AWS Lambda?*

Absolutely! show us your AWS chops

