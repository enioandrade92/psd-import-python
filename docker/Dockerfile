# Use an Amazon Linux image that is close to the Lambda environment
FROM public.ecr.aws/lambda/python:3.12

# Install psycopg2-binary
RUN pip install psd-tools -t /python

# Use Python to zip the contents
RUN python -m zipfile -c /psd-tools.zip /python