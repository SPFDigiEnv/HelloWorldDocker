# This is just a simple line of code to show how to run Python in Docker - with and without bind mounting.
# Edit the file here in both cases, perhaps changing the message printed, to see that:
# without bind mounting - only the original code copied in to the container can be run, no code editing is possible outside the container
# with bind mounting - the source code can be edited and re-run each time and will be available within the running docker container
print("Hello World Docker")
