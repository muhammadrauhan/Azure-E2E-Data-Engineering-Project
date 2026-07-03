# Azure-E2E-Data-Engineering-Project

## Project Overview
This **Azure End-to-End Data Engineering Project** demonstrates how to design and implement a modern, production-style data engineering pipeline on Microsoft Azure. The project focuses on building an automated ETL/ELT workflow that extracts customer and sales data from an on-premises SQL Server database, ingests it into Azure, performs scalable data transformations, and delivers business-ready insights through an interactive Power BI dashboard.

## Architecture
<img width="950" height="472" alt="AzureDataEngineering-E2E" src="https://github.com/user-attachments/assets/3acf1dde-b200-470e-86b0-eea3fa524920" />

## Technologies Used
- **Azure Data Factory (ADF):** Cloud-based data integration service for building, orchestrating, and automating ETL/ELT data pipelines.
- **Azure Data Lake Storage (ADLS) Gen2:** Scalable, secure, and high-performance data lake for storing raw and transformed data.
- **Azure Databricks:** Cloud-based platform for data engineering transformations.
- **Azure Databricks Access Connector:** Managed identity service that enables secure, passwordless access between Azure Databricks and Azure Storage.
- **Apache Spark:** Open-source unified analytics engine for large-scale data processing.
- **PySpark:** Python API for Spark, used for performing data processing tasks.
- **Azure Synapse Analytics:** Enterprise-scale data warehouse for storing curated data and enabling fast analytical queries.
- **Power BI:** Business intelligence and data visualization tool for creating interactive dashboards and KPI reports.
- **Azure Active Directory (Microsoft Entra ID):** Identity and access management service used for authentication, authorization, and secure resource access.
- **Azure Key Vault:** Secure secrets management service for storing and protecting credentials.

## What You'll Learn
1. Configure Azure Databricks and securely access data in Azure Storage.
2. Process and transform data using Databricks notebooks (`bronze`, `silver`, `gold`) called Medallion Architecture.
3. Automate data pipelines with Azure Data Factory.
4. Query and optimize data in Synapse Analytics for analytics.
5. Create a dashboard using Power BI.
 
## Prerequisites
- Azure account (free trial available).
- Basic understanding of data engineering concepts.
