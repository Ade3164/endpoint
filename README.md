# HNG Internship Project

Welcome to my HNG Internship project repository! This project is part of my journey to becoming a skilled developer during the HNG Internship program.

## Project Overview

This project serves as the foundation for my internship journey, where I'm tasked with creating and hosting a web endpoint. The primary goal is to demonstrate my ability to create a simple web service that accepts GET requests, processes parameters, and returns specific information in JSON format.

## Features

- **Endpoint Creation:** I've created a publicly accessible endpoint that listens to GET requests.

- **GET Parameters:** The endpoint accepts two GET request query parameters: `slack_name` and `track`.

- **Data Retrieval:** The endpoint retrieves these parameters, processes them, and returns information accordingly.

- **Current Day and Time:** It displays the current day of the week and UTC time with validation of +/-2 minutes.

- **Track:** The response displays the track I've signed up for, which is "Backend" in this case.

- **GitHub Integration:** The response includes GitHub URLs to the specific file being executed and the repository containing the full source code.

- **Status Code:** It returns a status code of 200 to indicate success.

## Usage

To test this endpoint, you can make GET requests to it with the appropriate query parameters. Here's an example:

```
http://example.com/api?slack_name=example_name&track=backend
```

Replace `example_name` with your desired Slack name and `backend` with your chosen track.

## Hosting

I've hosted this endpoint on a publicly accessible server to ensure it's available for testing. You can access it using the URL [here](http://example.com/api).

## Deadline

The deadline for submissions for this project is 12th September 2023, 11:59 PM GMT + 1.

## Contact

If you have any questions or need further assistance, please feel free to reach out to me.

Thank you for checking out my HNG Internship project!

---

Feel free to customize the README further with any additional details or instructions specific to your project. This README serves as a brief overview of your project and should provide enough information for anyone interested in your work.