# CRUK Node.js Recruitment Assignment

**Note - for the Python version of this exercise please click [[HERE](https://github.com/CRUKorg/cruk-backend-assignment/tree/python-version)]**

## Functional Requirements

- Build a service in Node.js that can be deployed to AWS.
- The service should expose an API that can be consumed from any client.
- The service should check how many donations a user has made and send them a special thank you message if they make 2 or more donations.

## Output Package Requirements

Please check the specific Output Package requirements for the engineering role you are applying for [HERE](./docs)

### FAQ's

*Any client - what are the clients?*

A client is a consumer of the API (e.g. web app, another backend service, a mobile app, etc). In this case "Any client" means for us, the API can and should be implemented independently of who/what is going to consume it.

*Does this sit behind an API Gateway?*

Whilst this is not strictly required, it’s just one of various solutions on AWS for exposing your API.

*How is authentication performed?*

We are not looking at the implementation of the authentication in the code challenge.

*Will the API receive a token in the header (JWT with authentication service defined)?*

Not necessarily, as per the answer above the authentication is not required for this task.

*Will only certain roles be able to call the API (e.g., AWS IAM Permissions with AWS API Gateway)?*

Again, no authorization or permissions are expected to be set for the coding challenge. We can discuss these things during the F2F interview.

*Will I need to persist donations data in a database?*

Most candidates have used an in-memory store which saves them time to provision and deploy machines/databases. If you want to use a specific data store we don’t have any objection.

*Is there a standardised/preferred method of logging?*

We don’t expect the coding challenge to be production-ready and ship logs anywhere but having basic error handling is considered a minimum requirement. You will definitely get extra points if you handle and log successfully edge-cases and critical paths (e.g. fatal errors).

*In terms of deploying to AWS, should I include a build pipeline or can that be done manually?*

Do it manually, it's a one-time thing.

*Can we implement this using AWS Lambda?*

Absolutely! Show us your AWS skills.