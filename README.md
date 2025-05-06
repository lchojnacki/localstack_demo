# LocalStack Django Demo

The aim of this project is to demonstrate the integration of Django with AWS
services using LocalStack - a fully functional local AWS cloud stack for
development and testing. The following AWS services are implemented:

- Amazon S3: Handling static and media file storage with presigned URL support
- Amazon SQS: Message queuing system integrated with Celery for asynchronous task processing
- AWS Lambda: Executing serverless functions for background tasks
- Amazon DynamoDB: Storing and managing NoSQL data
- Amazon SNS: Event-driven notifications for S3 file upload events

All services run locally using LocalStack, allowing developers to build and test
AWS integrations without connecting to the actual AWS cloud.
