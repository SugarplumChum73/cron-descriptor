FROM fuzzers/atheris:2.0.7-python3.9

# Copy the project source code.
COPY . /src
WORKDIR /src

# Build the project.
RUN pip install .

# Change Permissions
RUN chmod +x /src/mayhem/fuzz_get_description.py