# 🌦️ WeatherStream: Real-Time ELT Pipeline using AWS & Snowflake ❄️

<p align="center">
  <img src="https://img.shields.io/badge/AWS%20EventBridge-Scheduler-orange?logo=amazonaws&logoColor=white" alt="AWS EventBridge Badge"/>
  <img src="https://img.shields.io/badge/AWS%20DynamoDB-Raw%20Storage-blue?logo=amazonaws&logoColor=white" alt="AWS DynamoDB Badge"/>
  <img src="https://img.shields.io/badge/AWS%20Lambda-Processing-yellow?logo=amazonaws&logoColor=white" alt="AWS Lambda Badge"/>
  <img src="https://img.shields.io/badge/Amazon%20S3-Staging-red?logo=amazonaws&logoColor=white" alt="Amazon S3 Badge"/>
  <img src="https://img.shields.io/badge/Snowflake%20(Snowpipe)-Warehouse%20%26%20Ingestion-blue?logo=snowflake&logoColor=white" alt="Snowflake Badge"/>
  <img src="https://img.shields.io/badge/Python-Scripting-green?logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License Badge"/>
</p>

---

## 📌 Project Overview

This project demonstrates a modern, **end-to-end, serverless ELT (Extract, Load, Transform) data pipeline** built on AWS services to process real-time weather data. It showcases how live data from a public Weather API can be ingested, processed, stored, and loaded into Snowflake for analytics, utilizing:

-   **AWS EventBridge** for scheduled data extraction.
-   **AWS DynamoDB** for initial, resilient storage of raw weather data.
-   **AWS Lambda** triggered by DynamoDB Streams for real-time data processing and transformation.
-   **Amazon S3** for staging processed data before loading into the data warehouse.
-   **Snowflake** with **Snowpipe** for automated, continuous data ingestion and warehousing.
-   **SQL** within Snowflake for final data modeling and making data analytics-ready.

The core focus is on employing **serverless and scalable AWS services** along with Snowflake's powerful capabilities to create a cost-effective, automated, and robust data engineering solution.

---

## ⚙️ Tech Stack & Tools

| Tool/Service           | Purpose in Pipeline                                  |
|------------------------|------------------------------------------------------|
| Public Weather API     | Source of real-time weather data                     |
| AWS EventBridge        | Schedules automated data extraction                  |
| Python                 | Scripting for API interaction and Lambda function    |
| AWS DynamoDB           | Initial NoSQL database for raw data ingestion        |
| DynamoDB Streams       | Real-time capture of data changes in DynamoDB        |
| AWS Lambda             | Serverless compute for data processing & S3 transfer |
| Amazon S3              | Staging area for processed data                      |
| Snowflake              | Cloud data warehouse for analytics                   |
| Snowpipe (Snowflake)   | Continuous, automated data ingestion into Snowflake  |
| SQL                    | Data transformation and modeling within Snowflake    |

---

## ✨ Key Features

-   🔄 **Automated ELT Pipeline:** Fully automated flow from data source to analytical warehouse.
-   ⏱️ **Real-Time Data Ingestion & Processing:** Captures and processes weather data as it becomes available.
-   💾 **Resilient & Scalable Storage:** Utilizes DynamoDB and S3 for robust data handling.
-   ⚙️ **Event-Driven Architecture:** Lambda functions triggered by data events for efficient processing.
-   ❄️ **Continuous Data Loading:** Snowpipe ensures seamless data flow into Snowflake.
-   📊 **Analytics-Ready Warehouse:** Data is modeled in Snowflake for immediate querying and BI.
-   ☁️ **Fully Serverless Components:** Minimizes infrastructure management and optimizes costs.
-   💰 **Cost-Effective Solution:** Leverages pay-as-you-go services.

---

## 🏗️ Project Architecture

The overall architecture illustrates the data flow from the public Weather API through various AWS services into Snowflake:

![WeatherStream Architecture Diagram](AWS2Snowflake.jpg)

---

## 🌊 Pipeline Flow & Data Journey

The WeatherStream data engineering pipeline processes live weather data through these key stages:

1.  **⏰ Scheduled Extraction (AWS EventBridge & Python):**
    *   An **AWS EventBridge** rule is configured to trigger a Python script ([`Fetch_WeatherAPI.py`](Fetch_WeatherAPI.py)) at regular intervals.
    *   *EventBridge Configuration Snapshot:*
        <p align="center"><img src="AWS_EventBridge.png" alt="AWS EventBridge Configuration for Scheduled Trigger" width="600"/><br/><em>EventBridge rule ensuring periodic data fetching.</em></p>

2.  **📥 Ingestion & Raw Storage (Python & AWS DynamoDB):**
    *   The `Fetch_WeatherAPI.py` script calls a **Public Weather API** to retrieve the latest weather conditions.
    *   The raw weather data, typically in JSON format, is immediately ingested and stored in an **AWS DynamoDB** table.

3.  **⚙️ Real-Time ETL Processing (DynamoDB Streams, AWS Lambda & Amazon S3):**
    *   New data written to the DynamoDB table generates an event captured by **DynamoDB Streams**.
    *   This stream event instantly triggers an **AWS Lambda function** ([`DDB2Snowflake.py`](DDB2Snowflake.py)).
    *   The Lambda function:
        *   Reads the new record(s) from the stream.
        *   Performs necessary data cleaning and transformation (e.g., converting JSON to a structured CSV format).
        *   Uploads the processed CSV file to a designated **Amazon S3** bucket, which acts as a staging area.
    *   *Lambda Function Configuration & Trigger Snapshots:*
        <p align="center">
          <img src="DDB2SF_Lambda_Function.png" alt="AWS Lambda Function Configuration" width="600"/><br/>
          <em>Lambda function setup for data processing.</em><br/><br/>
          <img src="DDB2SF_Lambda_Function_Trigger.png" alt="AWS Lambda Trigger from DynamoDB Streams" width="600"/><br/>
          <em>DynamoDB Stream configured as the Lambda trigger.</em>
        </p>

4.  **❄️ Continuous Loading (Snowpipe & Snowflake):**
    *   **Snowpipe**, Snowflake’s continuous data ingestion service, is configured to monitor the S3 staging bucket for new file arrivals.
    *   When a new CSV file (from Lambda) lands in S3, Snowpipe automatically loads its content into a predefined target table within the **Snowflake Data Warehouse**.

5.  **🛠️ Data Modeling & Analytics (Snowflake SQL):**
    *   Once data is in Snowflake, SQL scripts ([`Snowflake.sql`](Snowflake.sql)) are used to:
        *   Perform final transformations.
        *   Model the data into an analytics-friendly schema (e.g., creating views or refined tables).
        *   Enable querying for insights and reporting.

---

## 🐍✨ Core Scripts in Action

*   **`Fetch_WeatherAPI.py`:**
    *   **🔗 View Code:** [`Fetch_WeatherAPI.py`](Fetch_WeatherAPI.py)
    *   **Purpose:** This Python script is responsible for making calls to the external public Weather API, retrieving the current weather data, and writing these raw records into the AWS DynamoDB table. It is designed to be triggered by AWS EventBridge.
*   **`DDB2Snowflake.py`:**
    *   **🔗 View Code:** [`DDB2Snowflake.py`](DDB2Snowflake.py)
    *   **Purpose:** Executed as an AWS Lambda function, this Python script is triggered by new items appearing in the DynamoDB Stream. It processes these items, transforms them into a CSV format, and then uploads the resulting file to an Amazon S3 bucket for staging.
*   **`Snowflake.sql`:**
    *   **🔗 View Code:** [`Snowflake.sql`](Snowflake.sql)
    *   **Purpose:** Contains the SQL Data Definition Language (DDL) for creating the necessary tables in Snowflake. It also includes Data Manipulation Language (DML) or query examples for transforming the data loaded by Snowpipe into a more structured, analytics-ready format.

---

## 📊 Visualizing the Outcome: Sample Dashboard

The data pipeline culminates in an analytics-ready dataset in Snowflake, which can be used to build insightful dashboards:

<p align="center">
  <img src="SF_DWH_Result_Dashboard.png" alt="Snowflake Data Warehouse Dashboard for WeatherStream" width="800"/>
  <em>Example of a dashboard visualizing weather data, powered by the WeatherStream pipeline and Snowflake.</em>
</p>

---

## 🚀 How to Replicate or Extend This Project (High-Level)

To set up a similar WeatherStream pipeline:

1.  **Prerequisites:**
    *   An active AWS account with permissions for EventBridge, Lambda, DynamoDB, S3, and IAM.
    *   A Snowflake account with privileges to create stages, pipes, and tables.
    *   Access credentials/API key for a public Weather API.
2.  **AWS Setup:**
    *   Configure the `Fetch_WeatherAPI.py` script with your Weather API details.
    *   Create an AWS EventBridge rule to schedule the execution of `Fetch_WeatherAPI.py` (e.g., via a Lambda function or a system running the script).
    *   Create an AWS DynamoDB table to store the raw weather data. Enable DynamoDB Streams on this table.
    *   Deploy the `DDB2Snowflake.py` script as an AWS Lambda function, configuring its environment variables (S3 bucket name, region, etc.) and setting the DynamoDB Stream as its trigger.
    *   Create an Amazon S3 bucket to serve as the staging area for processed data.
3.  **Snowflake Setup:**
    *   In Snowflake, create an external stage pointing to your S3 staging bucket.
    *   Define a target table structure (refer to `Snowflake.sql` for DDL).
    *   Create a Snowpipe that uses the external stage to automatically load new data from S3 into your target table.
    *   Use `Snowflake.sql` to apply transformations and create analytical views or tables.
4.  **Security & Configuration:**
    *   Ensure all AWS services have correctly configured IAM roles and policies for secure access.
    *   Manage API keys and sensitive credentials securely (e.g., using AWS Secrets Manager or environment variables in Lambda).
5.  **Test & Monitor:**
    *   Trigger the pipeline and monitor the flow of data through each stage.
    *   Verify data in DynamoDB, S3 files, and Snowflake tables.

*(This is a high-level guide. Detailed configuration will depend on your specific Weather API and AWS/Snowflake environment.)*

---

## 🙏 Acknowledgements & Educational Foundation

The development of WeatherStream was significantly informed and inspired by the invaluable educational content from the **DateWithData** YouTube channel. Their practical demonstrations of real-time AWS-to-Snowflake pipelines provided a strong foundation and learning path for this project.

Explore their excellent resources:
*   📺 **In-Depth Video Series:** [Real-Time DE Project: AWS to Snowflake by DateWithData](https://www.youtube.com/watch?v=84aG8h6diVU&list=PLRRQG4QYcyEV14Ku1d39XQdxUbaRbv602)
*   💻 **Original Project Repository:** [datewithdata1/DE-Project-AWS2SF](https://github.com/datewithdata1/DE-Project-AWS2SF-)

> Sincere gratitude to the DateWithData team for generously sharing their expertise and fostering learning within the data engineering community.

---

## 📜 Licensing Information

WeatherStream is open-source software licensed under the **MIT License**.
For full details, please refer to the [LICENSE](LICENSE) file included in this repository.

---

## 👨‍💻 About the Developer

**Subhajit Chowdhury © 2025**

A data engineering enthusiast passionate about designing and building scalable, cloud-native solutions that transform raw data into actionable insights.

*   🔗 **LinkedIn:** [linkedin.com/in/subhajitch0wdhury](https://www.linkedin.com/in/subhajitch0wdhury/)
*   🐙 **GitHub:** [github.com/Subhajit-Chowdhury](https://github.com/Subhajit-Chowdhury)
*   📧 **Email:** [er.subhajitchowdhury@gmail.com](mailto:er.subhajitchowdhury@gmail.com)

---

> Dive into WeatherStream and explore the art of building efficient, real-time data pipelines with the powerful combination of AWS and Snowflake! Contributions, feedback, and questions are always welcome. ⭐️
