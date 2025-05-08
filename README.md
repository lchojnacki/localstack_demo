# LocalStack Django Demo

The aim of this project is to demonstrate the integration of Django with AWS
services using LocalStack - a fully functional local AWS cloud stack for
development and testing. The following AWS services are implemented:

- [x] Amazon S3: Handling static and media file storage with presigned URL support
- [x] Amazon SQS: Message queuing system integrated with Celery for asynchronous task processing
- [x] AWS Lambda: Executing serverless functions for background tasks
- [ ] Amazon DynamoDB: Storing and managing NoSQL data
- [ ] Amazon SNS: Event-driven notifications for S3 file upload events

All services run locally using LocalStack, allowing developers to build and test
AWS integrations without connecting to the actual AWS cloud.

Presentation plan:
1. What is localstack?
2. Why use it? (the same environment, better testing)
3. What services are available in free plan and how much does the paid plan cost?
4. Django: S3 storage and persistent volume (community docker image)
5. Preview of services in the healthcheck endpoint
6. Django: S3 bucket versioning
7. Django + Celery + SQS
8. Można konfigurować za pomocą terraforma, opentofu - bezkosztowa nauka
