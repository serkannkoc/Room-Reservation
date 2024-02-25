# Room Reservation System with Microservices Architecture

This project implements an HTTP server that acts as a room reservation system using a microservices architecture.

## Project Overview

The system consists of three independent services:

![](https://github.com/serkannkoc/Room-Reservation/blob/master/architecture.png)

<ol>
    <li>Room Server: Manages room information and availability.</li>
    <li>Activity Server: Manages activity information and schedules.</li>
    <li>Reservation Server: Acts as a proxy server, handling user requests and interacting with Room and Activity servers.</li>
</ol>

Users interact solely with the Reservation Server, which relays their requests to the relevant server and returns the combined response.

## Technologies Used

- Python 3.11
- TinyDB (database for each server)
- socket (socket programming)

## Additional Information

For detailed information about the project design and implementation decisions please refer to the report included in this repository.

<b>Please note:</b> This README provides a high-level overview. Refer to the code and report for further details.
