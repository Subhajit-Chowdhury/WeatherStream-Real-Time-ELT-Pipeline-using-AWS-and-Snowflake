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

> **WeatherStream** is a fully serverless, real-time ELT (Extract, Load, Transform) pipeline that seamlessly ingests live weather data from a public API. It leverages the power of AWS services for efficient processing and loads the refined data into Snowflake, making it instantly available for downstream analytics and visualization. This project showcases modern data engineering practices, cloud-native automation, and event-driven architecture.

---

## 📌 Project Overview & Goals

This project demonstrates the construction of a robust, end-to-end data pipeline designed to:

*   **Ingest:** Capture live weather data from a public, real-time source.
*   **Process:** Clean, transform, and prepare the data for analytical use using serverless AWS components.
*   **Store & Load:** Efficiently stage data in Amazon S3 and automatically load it into a Snowflake data warehouse.
*   **Enable Analytics:** Provide a structured, analytics-ready dataset in Snowflake for querying and visualization.

The emphasis is on leveraging **serverless, scalable, and cost-effective AWS services** alongside Snowflake's powerful data warehousing capabilities to build a practical and modern data solution.

---

## 🗺️ Architecture at a Glance: The Journey of Data

Witness how WeatherStream orchestrates the flow of atmospheric data into actionable intelligence. The diagram below provides a high-level visual of the entire pipeline:

<p align="center">
  <img src="AWS2Snowflake.jpg" alt="WeatherStream Architecture Diagram" width="750"/>
</p>

> **Data Odyssey:** Public API → AWS DynamoDB (Raw Ingestion) → AWS Lambda (Transformation) → Amazon S3 (Staging) → Snowpipe (Automated Loading) → Snowflake (Analytics-Ready Warehouse)

---

## ✨ Key Features & Capabilities

*   ⏱️ **Scheduled & Continuous Ingestion:** AWS EventBridge ensures timely and regular data extraction.
*   💾 **Resilient Raw Storage:** AWS DynamoDB acts as the initial, durable store for incoming weather data.
*   🔁 **Event-Driven Real-Time Processing:** DynamoDB Streams trigger AWS Lambda for immediate data transformation.
*   ☁️ **Optimized Staging:** Amazon S3 serves as a scalable staging area for Snowflake ingestion.
*   ❄️ **Automated Warehouse Loading:** Snowpipe ensures continuous, hands-free data loading into Snowflake.
*   📊 **Analytics-Ready Data:** SQL transformations in Snowflake prepare data for immediate querying and BI.
*   ⚙️ **Fully Automated ELT:** A "set-it-and-forget-it" pipeline with minimal manual intervention.
*   💰 **Cost-Efficient & Scalable:** Built with serverless components that scale on demand and optimize costs.

---

## 🏗️ The Pipeline Unveiled: Step-by-Step Workflow

Follow a weather data point as it navigates through our automated system:

### 📡 **Act 1: The Sky's Signal – Data Extraction**
- Our Python scout, [`Fetch_WeatherAPI.py`](Fetch_WeatherAPI.py), diligently retrieves real-time weather data from a designated public API.
- **AWS EventBridge** acts as the metronome, triggering this script on a precise schedule for continuous, fresh data ingestion.

<p align="center">
  <img src="AWS_EventBridge.png" alt="EventBridge: The Pipeline's Scheduled Heartbeat" width="600"/><br/>
  <em>EventBridge ensures timely data capture.</em>
</p>

- The raw, untamed JSON data finds its first secure harbor in **AWS DynamoDB**.

---

### 🔄 **Act 2: The Alchemist's Chamber – Stream-Based Processing**
- The arrival of new records in DynamoDB instantly creates ripples via **DynamoDB Streams**, signaling our **AWS Lambda function** into action.
- This serverless artisan, ([`DDB2Snowflake.py`](DDB2Snowflake.py)), masterfully transforms, cleans, and refines the data, then exports the polished CSV to **Amazon S3**.

<p align="center">
  <img src="DDB2SF_Lambda_Function.png" alt="Lambda: The Serverless Data Processor" width="600"/><br/>
  <em>Lambda function configured and ready for action.</em><br/><br/>
  <img src="DDB2SF_Lambda_Function_Trigger.png" alt="DynamoDB Streams: The Instantaneous Lambda Trigger" width="600"/><br/>
  <em>DynamoDB Streams triggering our Lambda for real-time processing.</em>
</p>

---

### ❄️ **Act 3: The Crystal Palace – Continuous Loading into Snowflake**
- **Snowpipe**, Snowflake's vigilant automated ingestion service, detects new data arrivals in our S3 staging area.
- It then seamlessly and efficiently loads these files into the **Snowflake Data Warehouse**.
- Finally, powerful SQL transformation scripts [`Snowflake.sql`](Snowflake.sql) are applied to model the data, making it pristine and ready for profound analytical consumption.

---

## 🛠️ Tech Stack & Tools Leveraged

| Category                | Tool/Service                          | Role in Pipeline                                   |
|-------------------------|---------------------------------------|----------------------------------------------------|
| **Cloud Platform**      | Amazon Web Services (AWS)             | Foundation for serverless components               |
| **Data Source API**     | Public Weather API                    | Provides live weather information                  |
| **Scheduling**          | AWS EventBridge                       | Triggers data extraction script                    |
| **Extraction Script**   | Python ([`Fetch_WeatherAPI.py`](Fetch_WeatherAPI.py))         | Fetches data and stores in DynamoDB                |
| **Initial Data Store**  | AWS DynamoDB                          | Fast, NoSQL database for raw JSON data             |
| **Event Streaming**     | DynamoDB Streams                      | Captures data changes in DynamoDB in real-time     |
| **Data Processing**     | AWS Lambda ([`DDB2Snowflake.py`](DDB2Snowflake.py))       | Serverless compute for transformation (JSON to CSV)|
| **Staging Storage**     | Amazon S3                             | Scalable object storage for processed files        |
| **Data Warehouse**      | Snowflake                             | Cloud data platform for analytics                  |
| **Continuous Ingestion**| Snowpipe (Snowflake feature)          | Automates data loading from S3 to Snowflake      |
| **Data Modeling**       | SQL (within Snowflake)                | Transforms and structures data for BI              |

---

## 🐍 Key Scripts Driving the Pipeline

*   **`Fetch_WeatherAPI.py`:**
    *   **🔗 View Script:** [`Fetch_WeatherAPI.py`](Fetch_WeatherAPI.py)
    *   **Responsibility:** Connects to the public weather API, retrieves current weather data, and inserts it into the AWS DynamoDB table. Triggered by AWS EventBridge.
*   **`DDB2Snowflake.py`:**
    *   **🔗 View Script:** [`DDB2Snowflake.py`](DDB2Snowflake.py)
    *   **Responsibility:** This AWS Lambda function is triggered by DynamoDB Streams. It reads new weather records, transforms them (e.g., from JSON to CSV), and uploads the processed data to a designated Amazon S3 bucket.
*   **`Snowflake.sql`:**
    *   **🔗 View Script:** [`Snowflake.sql`](Snowflake.sql)
    *   **Responsibility:** Contains SQL DDL for table creation in Snowflake and DML/queries for transforming the raw ingested data into an analytics-ready, modeled format. Also includes sample queries for analysis.

---

## 📊 Visualizing the Insights: Sample Dashboard

The transformed data in Snowflake empowers the creation of insightful dashboards. Here's a glimpse of what can be achieved:

<p align="center">
  <img src="SF_DWH_Result_Dashboard.png" alt="Snowflake Data Warehouse Dashboard for WeatherStream" width="800"/>
  <em>Example dashboard showcasing analytics derived from the WeatherStream pipeline in Snowflake.</em>
</p>

---

## 🚀 How to Replicate This Project (High-Level Steps)

1.  **AWS & Snowflake Setup:**
    *   Ensure you have an AWS account and a Snowflake account.
    *   Configure necessary IAM roles and permissions in AWS for EventBridge, Lambda, DynamoDB, and S3.
2.  **Deploy Resources:**
    *   Create a DynamoDB table for raw weather data.
    *   Create S3 buckets for staging processed data.
    *   Set up the `Fetch_WeatherAPI.py` script (can be run locally initially or deployed as another Lambda if preferred for full serverless).
    *   Deploy the `DDB2Snowflake.py` script as an AWS Lambda function, configure its environment variables (S3 bucket name, API keys if needed, etc.), and set up the DynamoDB Stream trigger.
    *   Configure an AWS EventBridge rule to trigger the data extraction process.
3.  **Snowflake Configuration:**
    *   Create target tables in Snowflake (refer to `Snowflake.sql` for DDL).
    *   Set up Snowpipe to auto-ingest data from your S3 staging bucket into the Snowflake tables.
    *   Run the transformation SQL in `Snowflake.sql` to model the data.
4.  **Testing & Validation:**
    *   Trigger the pipeline and monitor data flow through each stage.
    *   Verify data in DynamoDB, S3, and finally in Snowflake.
    *   Query the data in Snowflake and (optionally) connect a BI tool like Snowflake's built-in dashboards or Tableau/PowerBI.

*(Refer to individual script comments and AWS/Snowflake documentation for detailed setup.)*

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

A data engineering enthusiast passionate about building scalable, cloud-native solutions that drive insights from data.

*   🔗 **LinkedIn:** [linkedin.com/in/subhajitch0wdhury](https://www.linkedin.com/in/subhajitch0wdhury/)
*   🐙 **GitHub:** [github.com/Subhajit-Chowdhury](https://github.com/Subhajit-Chowdhury)
*   📧 **Email:** [er.subhajitchowdhury@gmail.com](mailto:er.subhajitchowdhury@gmail.com)

---

> Dive into WeatherStream and explore the art of building efficient, real-time data pipelines with the powerful combination of AWS and Snowflake! Contributions and feedback are always welcome. ⭐️
