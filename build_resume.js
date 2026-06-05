const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  TabStopType, TabStopPosition, LevelFormat, BorderStyle,
  WidthType, Footer, PageNumber, ExternalHyperlink
} = require("docx");
const fs = require("fs");

// ── Helpers ──────────────────────────────────────────────────────────────────

function sectionHeader(text) {
  return new Paragraph({
    spacing: { before: 160, after: 60 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "000000", space: 1 } },
    children: [new TextRun({ text, bold: true, size: 22, font: "Calibri" })]
  });
}

function jobHeader(title, company, dateRange, pageBreak = false) {
  // Company left, date right — on same line via tab stop
  return [
    new Paragraph({
      pageBreakBefore: pageBreak,
      spacing: { before: pageBreak ? 0 : 120, after: 0 },
      tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
      children: [
        new TextRun({ text: company, bold: true, size: 22, font: "Calibri" }),
        new TextRun({ text: "\t" + dateRange, size: 22, font: "Calibri" }),
      ]
    }),
    new Paragraph({
      spacing: { before: 0, after: 40 },
      children: [new TextRun({ text: title, italics: true, size: 22, font: "Calibri" })]
    })
  ];
}

function bullet(text) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { before: 20, after: 20 },
    children: [new TextRun({ text, size: 22, font: "Calibri" })]
  });
}

function plain(text, opts = {}) {
  return new Paragraph({
    spacing: { before: 40, after: 40 },
    children: [new TextRun({ text, size: 22, font: "Calibri", ...opts })]
  });
}

// ── Document ─────────────────────────────────────────────────────────────────

const doc = new Document({
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "•",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 180 } } }
      }]
    }]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 720, right: 1080, bottom: 900, left: 1080 }
      }
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          tabStops: [{ type: TabStopType.RIGHT, position: 10080 }],
          border: { top: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 1 } },
          spacing: { before: 80 },
          children: [
            new TextRun({ text: "edpol03@gmail.com  |  305-215-5503  |  Hollywood, FL  |  ", size: 22, font: "Calibri", color: "444444" }),
            new ExternalHyperlink({
              link: "https://linkedin.com/in/edwardpol",
              children: [new TextRun({ text: "LinkedIn.com/in/EdwardPol", size: 22, font: "Calibri", color: "0563C1", underline: {} })]
            }),
            new TextRun({ text: "\tPage ", size: 22, font: "Calibri", color: "444444" }),
            new TextRun({ children: [PageNumber.CURRENT], size: 22, font: "Calibri", color: "444444" }),
            new TextRun({ text: " of ", size: 22, font: "Calibri", color: "444444" }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 22, font: "Calibri", color: "444444" }),
          ]
        })]
      })
    },
    children: [

      // ── Name & Title ──────────────────────────────────────────────────────
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 40 },
        children: [new TextRun({ text: "Edward Pol", bold: true, size: 36, font: "Calibri" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 80 },
        children: [new TextRun({ text: "Software Engineer", size: 24, font: "Calibri" })]
      }),

      // ── Highlights ────────────────────────────────────────────────────────
      sectionHeader("HIGHLIGHTS"),
      bullet("Built production REST APIs in PHP/Laravel across payment processing (Braintree), third-party SOAP integrations, and custom order fulfillment workflows, delivering customer-facing features end-to-end across multiple production systems."),
      bullet("Cut infrastructure costs 76% by engineering Python/AWS Lambda automations triggered by EventBridge, reducing EC2 instance runtime from 168 to 40 hours per week."),
      bullet("Delivered a Laravel lead management platform that boosted subscription revenue by 50%, automating partner FTP data ingestion through to email campaign execution with zero manual intervention."),
      bullet("Maintained production-quality PHP on high-stakes applications using GitLab CI/CD pipelines, PHPUnit automated test suites, and Docker-based environments, serving military and government agency clients."),
      bullet("Optimized MySQL performance through indexing and query restructuring on high-traffic lead upload and commission reporting utilities, supporting external travel agency partners at scale."),

      // ── Professional Experience ───────────────────────────────────────────
      sectionHeader("PROFESSIONAL EXPERIENCE"),

      // MDR 2024-Present
      ...jobHeader("Senior Software Engineer", "Medical Doctors Research", "07/2024 – Present"),
      bullet("Developed Python-based AWS Lambda functions triggered by EventBridge to automatically start and stop EC2 instances on a schedule, reducing EC2 runtime from 168 to 40 hours per week — a 76% reduction in instance costs."),
      bullet("Built a questionnaire utility in PHP/Laravel/MySQL with RESTful APIs enabling processing of custom vitamin orders."),
      bullet("Integrated website questionnaire with Blister Packaging Machine to automate custom orders."),
      bullet("Created an automated order fulfillment system with web-based file upload functionality to bulk update shipping dates and tracking numbers in an AWS-hosted MSSQL database."),

      // Inseego
      ...jobHeader("Senior Software Engineer", "Inseego", "07/2025 – 10/2025"),
      bullet("Enhanced legacy application for military and government agencies using PHP, MySQL, and Docker, implementing bug fixes and feature additions to streamline equipment purchasing workflows for cell phones and related hardware."),
      bullet("Worked in an Agile software engineering team using GitLab CI/CD pipelines to automate testing, integration, and deployment workflows. Testing with PHPUnit."),

      // Shore Excursions
      ...jobHeader("Software Engineer", "Shore Excursions Group", "10/2019 – 06/2024"),
      bullet("Developed and deployed a Laravel/JavaScript lead management system with commission reporting and generated files for email campaigns. Boosted subscriptions by 50%."),
      bullet("Eliminated manual lead collection by building a data ingestion pipeline that integrated with client FTP sites, scaling email marketing operations and increasing revenue generation."),
      bullet("Configured and trained Tettra’s AI Bot to handle employee inquiries, reducing managers’ workload."),
      bullet("Integrated Braintree’s API to remove foreign currency fees and enhance customer satisfaction."),
      bullet("Automated coupon code systems on Linux for partners, including Expedia, directly increasing sales conversions."),
      bullet("Integrated vendor’s SOAP API into company site using PHP, automating real-time helicopter time slot availability and eliminating manual lookup processes, saving employees 10+ hours weekly."),
      bullet("Optimized MySQL query performance through indexing and query tuning on high-traffic lead upload and commission reporting utilities used by external travel agency partners."),

      // Insurance Care Direct
      ...jobHeader("Laravel Developer", "Insurance Care Direct", "05/2019 – 10/2019", true),
      bullet("Built a Laravel/Vue.js application empowering insurance professionals with integrated tools for sales, marketing, education, and lead management."),
      bullet("Revamped site user experience, driving higher customer engagement and improved site accessibility."),

      // MDR 2018
      ...jobHeader("Software Developer", "Medical Doctors Research", "07/2018 – 05/2019"),
      bullet("Integrated commission calculation module into the Order Management System for a multi level marketing company."),
      bullet("Led a cross-functional IT team of 3, overseeing resource allocation and deliverable quality."),
      bullet("Developed an in-house PHP shopping cart with payment processing, saving $5,000 annually in fees."),
      bullet("Built a PHP timeclock system with a commission module, cutting payroll processing time in half."),
      bullet("Automated company-wide reporting by building a PHP intranet platform with real-time AWS MSSQL database connectivity, eliminating manual data compilation."),
      bullet("Successfully migrated CRM database from Oracle to Microsoft SQL Server on AWS EC2 with zero downtime, reducing maintenance costs to 1/10."),

      // Feeduciary
      ...jobHeader("Software Developer (Freelance)", "Feeduciary.com", "01/2018 – 12/2018"),
      bullet("Developed a Laravel-based marketplace from scratch, enabling fiduciary agents to create profiles with fee structures, facilitating client-agent comparisons and selections."),
      bullet("Implemented Google Maps API integration for location display and ImageMagick for image optimization, tested and developed using Postman."),
      bullet("Designed intuitive UI/UX that streamlined workflows and navigation for both fiduciary agents and clients."),

      // Rex3
      ...jobHeader("Laravel Developer", "Rex3", "08/2017 – 07/2018"),
      bullet("Built automation microservices for page layout, significantly accelerating print production timelines."),
      bullet("Developed RESTful API integration between Salesforce and print platforms, enabling automated generation of customer materials."),
      bullet("Created an intranet system for FedEx label generation and printing, accelerating shipping workflows."),

      // Clientele
      ...jobHeader("IT Manager and Developer", "Clientele Cosmetics Corp.", "2008 – 08/2017"),
      bullet("Led a 3-person IT team maintaining company infrastructure and internal systems, ensuring high availability and optimal performance."),
      bullet("Migrated in-house CRM to Oracle to centralize enterprise data across order management, commissions, accounting, shipping, production, inventory control, Bill of Materials and customer records."),
      bullet("Partnered with offshore developers to maintain Oracle instance stability, supporting business-critical workflows with minimal downtime."),
      bullet("Implemented automated daily backup system with off-site storage, ensuring secure protection and disaster recovery for company and customer data."),
      bullet("Created self-service analytics tools allowing users to run sales, inventory, and marketing reports on demand, eliminating IT bottlenecks and reducing turnaround time."),

      // ── Education ─────────────────────────────────────────────────────────
      sectionHeader("EDUCATION"),
      plain("Bachelor of Science  |  Electrical Engineering  |  University of Miami"),

      // ── Skills ────────────────────────────────────────────────────────────
      sectionHeader("SKILLS"),
      plain("Software design, PHP, PHP 8, Laravel, HTML, CSS, JavaScript, Docker, Python, MySQL, AWS"),

    ]
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("Edward_Pol_Resume_Lendable.docx", buf);
  console.log("Done.");
});
