# Medical Doctors Research — Project Summary
**Role:** Software Developer (2018–2019) → Senior Software Engineer (2024–Present)
**Stack:** PHP, Laravel, Python, AWS (Lambda, EventBridge, EC2, MSSQL), MySQL, Docker, BigCommerce

## AWS Lambda Cost Reduction (2024–Present)
- Built Python-based AWS Lambda functions triggered by EventBridge to automatically start and stop EC2 instances on a defined schedule
- Reduced EC2 runtime from 168 hours/week to 40 hours/week — a 76% reduction in compute costs
- Replaced a manual process of remembering to shut down servers

## Questionnaire & Vitamin Order System (2024–Present)
- Designed and built a PHP/Laravel questionnaire utility with full CRUD admin interface
- Allowed authorized users to define questions, answers, and logic (each answer adds/removes vitamins from a recommended order)
- Exposed RESTful API for the frontend to fetch questions and submit answers
- Integrated with Parata pill packaging machine: generated correctly formatted order files and placed them in the machine's input folder via FTP/WinSCP
- Considered allergen flagging, prescription drug interactions (iCare integration), and HIPAA compliance requirements
- Handled order creation in MOM/BigCommerce and triggered fulfillment workflow

## Automated Order Fulfillment — Bulk Shipping Updates
- Built a web-based file upload tool to bulk-update shipping dates and tracking numbers in an AWS-hosted MSSQL database
- Eliminated manual data entry for the shipping/fulfillment team

## PHP Shopping Cart (2018–2019)
- Developed an in-house PHP shopping cart with full payment processing (Authorize.net)
- Saved $5,000/year in third-party subscription and transaction fees
- Replaced a paid e-commerce platform with a custom solution tailored to business needs

## PHP Timeclock & Commission System (2018–2019)
- Built a PHP timeclock system with punch-in/out, time editing with audit logs, and a commission calculation module
- Cut payroll processing time by 50%
- Version 2 planning included: vacation/sick time tracking, GPS/IP logging, approval workflows, ADP export

## CRM Migration: Oracle → Microsoft SQL Server on AWS (2018–2019)
- Led the migration of the company CRM database from Oracle to Microsoft SQL Server hosted on AWS EC2
- Achieved zero downtime during migration
- Reduced maintenance costs to 1/10 of previous Oracle licensing and support costs

## Commission Calculation Module (2018–2019)
- Integrated multi-level marketing commission calculation logic into the Order Management System (MOM)
- Tracked genealogy, compensation tiers, and payout calculations for the sales organization

## PHP Intranet Platform (2018–2019)
- Built a company-wide PHP intranet with real-time connectivity to the AWS MSSQL database
- Automated reporting that had previously required IT to compile data manually

## E-Commerce & Website Migration
- Migrated multiple product websites to BigCommerce, including inventory export, payment processor setup, and DNS cutover
- Managed multi-site setup (MDR, Clientele Beauty, and associated product brands)
- Integrated BigCommerce with email marketing (MailChimp export workflow)

## QVC / UPS SurePost Integration
- Managed QVC's SurePost certification requirement for drop-ship vendors
- Coordinated with UPS and QVC's operations team to configure WorldShip for SurePost label generation
