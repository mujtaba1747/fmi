# Use the official AWS Lambda Python image as the base image
FROM public.ecr.aws/lambda/python:3.8

# Set the working directory
WORKDIR /var/task

# ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib

# Copy the FMI build to /opt/python
COPY python/ /opt/python/

# Install additional Linux dependencies
RUN yum -y groupinstall "Development Tools" && yum -y install openssl openssl-devel libcurl libcurl-devel gcc72 gcc72-c++ which

# Copy the Lambda function code
COPY lambda_function.py /var/task/lambda_function.py

# Set the Lambda function handler
CMD ["lambda_function.lambda_handler"]
