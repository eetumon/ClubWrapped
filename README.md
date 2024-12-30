# ClubWrapped - Member Statistics Application

## Overview
The ClubWrapped application generates fun statistics about member interactions within a community. By calculating and displaying various metrics based on predefined message data, this tool provides an entertaining way for members to engage with their communication patterns.

## Features

### Messages Sent
The application displays the total number of messages sent by each member in the year 2025. This data is derived from a predefined set of messages in the code for 2024 and user input for 2025.

Additionally, the application calculates how many more messages a member sent in 2025 compared to 2024. The increase in messages sent is determined by subtracting the number of messages sent in 2024 from those sent in 2025.

The percentage increase in messages sent is also calculated using the following formula:

\[
\text{Percentage Increase} = \frac{\text{Messages Sent in 2025} - \text{Messages Sent in 2024}}{\text{Messages Sent in 2024}} \times 100
\]

### Time Spent
The application calculates and displays the total time spent based on messages sent. This is determined by multiplying the total messages sent by a predefined constant (SECONDS PER MESSAGE), which represents the average time taken for each message.

The time spent is presented in hours and minutes format, providing a clear view of how much time members are investing in conversations.

### Best Buddy
The application identifies each member's best buddy, defined as the member who has sent the most messages to them. This determination is made by comparing message counts from all members to find out who engaged most with each specified member.

This feature highlights connections and interactions within the community, fostering relationships among members.

### Counters
The application includes counters that track how many times specific words or phrases have been logged by a Discord bot within the community. These counters provide additional context to member interactions and can reflect popular topics of conversation among members.

## Conclusion
The ClubWrapped application serves as a fun tool for generating entertaining statistics about community engagement and interaction patterns. By providing clear metrics on communication behaviors and additional counters, it enhances member engagement and enjoyment within the group.
