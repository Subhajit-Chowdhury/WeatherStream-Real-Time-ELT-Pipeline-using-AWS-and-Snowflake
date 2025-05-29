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

*   **Ingest:** Reliably capture live weather data from a public, real-time source.
*   **Process:** Efficiently clean, transform, and prepare data for analytical use via serverless AWS components.
*   **Store & Load:** Securely stage data in Amazon S3 and automate its loading into a Snowflake data warehouse.
*   **Enable Analytics:** Deliver a structured, analytics-ready dataset within Snowflake, primed for querying and insightful visualization.

The core philosophy is to leverage **serverless, scalable, and cost-effective AWS services** in tandem with Snowflake's formidable data warehousing capabilities, creating a practical and contemporary data solution.

---

## 🗺️ Architecture at a Glance: The Journey of Data

Witness how WeatherStream orchestrates the flow of atmospheric data into actionable intelligence. The diagram below provides a high-level visual of the entire pipeline:

<p align="center">
  <img src="AWS2Snowflake.jpg" alt="WeatherStream Architecture Diagram" width="750"/>
</p>

> **Data Odyssey:** Public API → AWS DynamoDB (Raw Ingestion) → AWS Lambda (Transformation) → Amazon S3 (Staging) → Snowpipe (Automated Loading) → Snowflake (Analytics-Ready Warehouse)

---

## ✨ Key Features & Capabilities

*   ⏱️ **Scheduled & Continuous Ingestion:** AWS EventBridge ensures precise and regular data extraction.
*   💾 **Resilient Raw Storage:** AWS DynamoDB serves as the highly available initial store for incoming weather data.
*   🔁 **Event-Driven Real-Time Processing:** DynamoDB Streams trigger AWS Lambda for immediate, responsive data transformation.
*   ☁️ **Optimized Staging:** Amazon S3 provides a scalable and durable staging area for Snowflake ingestion.
*   ❄️ **Automated Warehouse Loading:** Snowpipe facilitates continuous, zero-touch data loading into Snowflake.
*   📊 **Analytics-Ready Data:** Strategic SQL transformations within Snowflake sculpt raw data into refined, queryable assets.
*   ⚙️ **Fully Automated ELT:** A "set-it-and-forget-it" pipeline minimizing manual intervention.
*   💰 **Cost-Efficient & Scalable:** Architected with serverless components that adapt to demand and optimize operational costs.

---

## 🏗️ The Pipeline Unveiled: Step-by-Step Workflow

Follow a single weather data point as it navigates through WeatherStream's automated system:

### 📡 **Act 1: The Sky's Signal – Data Extraction**
- Our Python-driven data scout, [`Fetch_WeatherAPI.py`](Fetch_WeatherAPI.py), diligently retrieves real-time weather data from a designated public API.
- **AWS EventBridge** acts as the pipeline's metronome, triggering this script on a precise schedule for continuous and fresh data ingestion.

<p align="center">
  <img src="AWS_EventBridge.png" alt="EventBridge: The Pipeline's Scheduled Heartbeat" width="600"/><br/>
  <em>EventBridge ensures timely and consistent data capture.</em>
</p>

- The raw, untamed JSON data is immediately and securely harbored in **AWS DynamoDB**.

---

### 🔄 **Act 2: The Alchemist's Chamber – Stream-Based Processing**
- The arrival of new records in DynamoDB instantly creates ripples via **DynamoDB Streams**, signaling our **AWS Lambda function** into action.
- This serverless artisan, the [`DDB2Snowflake.py`](DDB2Snowflake.py) script, masterfully transforms, cleans, and refines the data (e.g., JSON to CSV), then exports the polished output to **Amazon S3**.

<p align="center">
  <img src="DDB2SF_Lambda_Function.png" alt="Lambda: The Serverless Data Processor" width="600"/><br/>
  <em>Lambda function configured and poised for data transformation.</em><br/><br/>
  <img src="DDB2SF_Lambda_Function_Trigger.png" alt="DynamoDB Streams: The Instantaneous Lambda Trigger" width="600"/><br/>
  <em>DynamoDB Streams triggering the Lambda for immediate, event-driven processing.</em>
</p>

---

### ❄️ **Act 3: The Crystal Palace – Continuous Loading into Snowflake**
- **Snowpipe**, Snowflake's vigilant automated ingestion service, continuously monitors our S3 staging area for new data arrivals.
- Upon detection, it seamlessly and efficiently loads these files into the target tables within the **Snowflake Data Warehouse**.
- Finally, powerful SQL transformation scripts, detailed in [`Snowflake.sql`](Snowflake.sql), are applied to model the data, rendering it pristine and ready for profound analytical consumption.

---

## 🛠️ Tech Stack & Tools Leveraged

| Category                | Tool/Service                          | Role in Pipeline                                     |
|-------------------------|---------------------------------------|------------------------------------------------------|
| **Cloud Platform**      | Amazon Web Services (AWS)             | Foundation for all serverless components             |
| **Data Source API**     | Public Weather API                    | Provides the live, external weather information feed |
| **Scheduling**          | AWS EventBridge                       | Orchestrates and triggers data extraction script     |
| **Extraction Script**   | Python ([`Fetch_WeatherAPI.py`](Fetch_WeatherAPI.py))         | Fetches data; initial storage into DynamoDB          |
| **Initial Data Store**  | AWS DynamoDB                          | High-performance NoSQL database for raw JSON data    |
| **Event Streaming**     | DynamoDB Streams                      | Captures and streams data modifications in real-time |
| **Data Processing**     | AWS Lambda ([`DDB2Snowflake.py`](DDB2Snowflake.py))       | Serverless compute for data transformation & S3 load |
| **Staging Storage**     | Amazon S3                             | Scalable object storage for processed data files   |
| **Data Warehouse**      | Snowflake                             | Cloud-native data platform for advanced analytics    |
| **Continuous Ingestion**| Snowpipe (Snowflake feature)          | Automates efficient data loading from S3           |
| **Data Modeling**       | SQL (within Snowflake)                | Structures and refines data for BI and querying    |

---

## 🐍 Key Scripts Driving the Pipeline

*   **`Fetch_WeatherAPI.py`:**
    *   **🔗 View Script:** [`Fetch_WeatherAPI.py`](Fetch_WeatherAPI.py)
    *   **Responsibility:** Connects to the public weather API, retrieves current weather data, and inserts it into the AWS DynamoDB table. This script is invoked by AWS EventBridge.
*   **`DDB2Snowflake.py`:**
    *   **🔗 View Script:** [`DDB2Snowflake.py`](DDB2Snowflake.py)
    *   **Responsibility:** This AWS Lambda function, triggered by DynamoDB Streams, reads new weather records. It then transforms them (e.g., from JSON structure to a CSV format suitable for Snowflake) and uploads the processed data to a designated Amazon S3 bucket.
*   **`Snowflake.sql`:**
    *   **🔗 View Script:** [`Snowflake.sql`](Snowflake.sql)
    *   **Responsibility:** Contains Data Definition Language (DDL) for creating tables in Snowflake. It also includes Data Manipulation Language (DML) and queries for transforming the raw ingested data into an analytics-ready, well-modeled format, along with sample queries for data exploration.

---

## 📊 Visualizing the Insights: Sample Dashboard

The transformed and modeled data within Snowflake enables the creation of rich, insightful dashboards. Below is an example of what can be achieved:

<p align="center">
  <img src="SF_DWH_Result_Dashboard.png" alt="Snowflake Data Warehouse Dashboard for WeatherStream" width="800"/>
  <em>Example dashboard built in Snowflake (or a connected BI tool) showcasing analytics derived from the WeatherStream pipeline.</em>
</p>

---

## 🚀 How to Use This Project (High-Level Guide)

To replicate or adapt the WeatherStream pipeline:

1.  **Fork/Clone the Repository:** Get a local copy of the project files.
2.  **Prerequisites & Setup:**
    *   Ensure you have an active **AWS account** and a **Snowflake account**.
    *   Obtain an **API key** if required by your chosen Public Weather API.
    *   Configure necessary **IAM roles and permissions** in AWS for EventBridge, Lambda, DynamoDB, and S3 access.
3.  **Configure Scripts:**
    *   Update `Fetch_WeatherAPI.py` with your Weather API endpoint and key.
    *   Update `DDB2Snowflake.py` (Lambda environment variables) with your S3 bucket details.
4.  **Deploy AWS Resources:**
    *   Create the DynamoDB table.
    *   Create the S3 bucket for staging.
    *   Deploy the Lambda function (`DDB2Snowflake.py`) and configure its DynamoDB Stream trigger.
    *   Set up the EventBridge rule to schedule the `Fetch_WeatherAPI.py` execution.
5.  **Configure Snowflake:**
    *   Use `Snowflake.sql` to create target tables and any necessary views.
    *   Set up Snowpipe to ingest data from your S3 staging bucket.
6.  **Test & Iterate:**
    *   Trigger the pipeline and monitor data flow.
    *   Connect a BI tool or use Snowflake's UI to query and visualize the weather data.

*(Note: This is a high-level guide. Refer to individual script comments, AWS, and Snowflake documentation for detailed configurations and best practices, especially regarding security and IAM.)*

---

## 💡 Learning Outcomes

By exploring and implementing WeatherStream, you will gain practical experience in:

-   Designing and building **end-to-end ELT data pipelines** on the cloud.
-   Utilizing core **AWS services** for data engineering: EventBridge, DynamoDB, Lambda, S3.
-   Implementing **real-time, event-driven processing** using DynamoDB Streams and Lambda.
-   Leveraging **Snowflake** for modern data warehousing, including Snowpipe for continuous ingestion.
-   Applying **Python** for data extraction and transformation.
-   Practicing **serverless architecture** principles for scalable and cost-effective solutions.
-   Understanding **data modeling** concepts for analytical workloads.

---

## 🏁 Conclusion

WeatherStream successfully demonstrates the power and flexibility of combining AWS serverless services with Snowflake to create a modern, real-time data engineering pipeline. By ingesting live weather data, performing efficient transformations, and enabling robust analytics, this project showcases a practical approach to turning continuous data streams into valuable, timely insights. It serves as a strong example of cloud-based data solutions that are scalable, automated, and cost-effective.

---

## 🙏 Acknowledgements & Educational Foundation

The development of WeatherStream was significantly informed and inspired by the invaluable educational content from the **DateWithData** YouTube channel. Their practical demonstrations of real-time AWS-to-Snowflake pipelines provided a strong foundation and learning path for this project.

Explore their excellent resources:
*   📺 **In-Depth Video Series:** [Real-Time DE Project: AWS to Snowflake by DateWithData](https://www.youtube.com/watch?v=84aG8h6diVU&list=PLRRQG4QYcyEV14Ku1d39XQdxUbaRbv602)
*   💻 **Original Project Repository:** [datewithdata1/DE-Project-AWS2SF](https://github.com/datewithdata1/DE-Project-AWS2SF-)

> Sincere gratitude to the DateWithData team for generously sharing their expertise and fostering learning within the data engineering community.

---

## 🤝 Contributing

Contributions, issues, and feature requests are always welcome!
Feel free to check the [issues page](https://github.com/Subhajit-Chowdhury/WeatherStream/issues) *(<- Update this link if your repo name is different or you don't have issues enabled yet)* or submit a Pull Request.

---

## 📜 Licensing Information

WeatherStream is open-source software licensed under the **MIT License**.
For full details, please refer to the [LICENSE](LICENSE) file included in this repository.

---

## 📬 Contact

Created with ❤️ by **Subhajit Chowdhury © 2025**

A data engineering enthusiast passionate about designing and building scalable, cloud-native solutions that transform raw data into actionable insights.

*   🔗 **LinkedIn:** [linkedin.com/in/subhajitch0wdhury](https://www.linkedin.com/in/subhajitch0wdhury/)
*   🐙 **GitHub:** [github.com/Subhajit-Chowdhury](https://github.com/Subhajit-Chowdhury)
*   📧 **Email:** [er.subhajitchowdhury@gmail.com](mailto:er.subhajitchowdhury@gmail.com)

---

> Dive into WeatherStream and explore the art of building efficient, real-time data pipelines with the powerful combination of AWS and Snowflake! ⭐️ **Give this repo a star** if it helped you learn something new or you found it useful!
