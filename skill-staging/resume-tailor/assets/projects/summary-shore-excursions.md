# Shore Excursions Group — Project Summary
**Role:** Software Engineer | **Dates:** 10/2019 – 06/2024
**Stack:** PHP, Laravel, JavaScript, MySQL, Docker, Nginx, Linux, SOAP/REST APIs

## Lead Management & Email Marketing System
- Built a Laravel/JavaScript lead management system for travel agency partners with commission tracking and reporting
- Automated lead collection by building an FTP data ingestion pipeline that pulled lead files from partner FTP sites nightly, parsed and normalized them, and loaded them into the database — eliminating manual CSV uploads entirely
- Generated email blast files in WhatCounts-compatible format, automating the full pipeline from lead ingestion to email campaign execution
- System scaled email marketing operations and directly increased subscription revenue by 50%

## Braintree Payment API Integration
- Integrated Braintree's payment API to enable foreign currency processing for international cruise passengers
- Removed foreign currency fees that had been a customer friction point, improving checkout conversion and satisfaction

## Expedia & Partner Coupon Code Integration
- Built automated coupon code integration systems for major travel distribution partners including Expedia
- Integrations ran on Linux servers and triggered sales conversions automatically without manual intervention

## SOAP API — Helicopter Time Slot Availability (TakeFlite/TFlite)
- Integrated a third-party vendor's SOAP API (TakeFlite) to provide real-time helicopter tour availability on the company website
- Automated what had previously been a manual lookup process, saving employees 10+ hours per week
- Built WSDL-based SOAP client in PHP; handled XML parsing, event scheduling, and availability display

## MySQL Performance Optimization
- Optimized slow MySQL queries used by external travel agency partners for lead uploads and commission reporting
- Applied indexing strategies and query restructuring to high-traffic utilities, significantly reducing query time on large datasets

## Client & User Management System
- Built a full-featured client management system with CSV bulk import, search/filtering, role-based access, and affiliate partner segmentation (Distinctive Voyages, Lightbox agencies)
- Included commission percentage tracking, currency type support, and agency ID management

## Tettra AI Bot
- Configured and trained Tettra's AI knowledge bot to handle common employee inquiries, reducing manager interruptions

## Docker / Nginx Development Environment
- Set up Docker-based local development environment with Nginx and SSL for the team, standardizing dev/prod parity
- Documented Docker configuration including self-signed cert setup, GitHub integration, and Docker Hub automated builds

## IVR Integration (CXone)
- Researched and began integrating CXone IVR system for phone-based customer interactions; built basic call scripts and skill routing logic
