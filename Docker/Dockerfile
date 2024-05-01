# Use a base image with Java installed
FROM openjdk:11-jdk

# Set the working directory
WORKDIR /app

# Copy the Java application JAR file to the container
COPY target/app.jar .

# Expose the port that the Java application will run on (if applicable)
EXPOSE 8080

# Set the command to run the Java application
CMD ["java", "-jar", "app.jar"]