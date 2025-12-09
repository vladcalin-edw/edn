Microsoft Teams Meeting Transcript
Project: “SavingsAI – An AI‑Driven Personal Finance Assistant”
Date: 08 Dec 2025
Time: 09:00 – 09:45 A.M. (UTC+0)
Participants:

Alice – Product Owner
Alpaca – AI Engineering Lead
Monterei – Finance Domain Lead
09:00 – 09:05 – Kickoff & Agenda

09:00:00 Alice: Welcome everyone. Today we’ll outline the “SavingsAI” project – an AI‑powered finance app that helps users save money by giving tailored advice. I’ll walk through the high‑level vision, the project structure, and next steps. Please interrupt if you have questions.

09:00:05 Alpaca: Thanks, Alice. I’ll keep the AI side concise but will dive into the ML pipeline later.

09:00:10 Monterei: And I’ll highlight the regulatory and data‑privacy constraints we need to honor.

09:00:15 Alice: Great. Let’s start with the agenda.

09:00:20 Alice: 1. Project Vision & Objectives (5 min) 2. Stakeholder & Compliance Review (5 min) 3. Technical Architecture (10 min) 4. Project Timeline & Milestones (10 min) 5. Roles & Responsibilities (5 min) 6. Action Items & Wrap‑Up (5 min)

09:00:30 Alice: Any objections?

09:00:32 Alpaca: None.

09:00:34 Monterei: All good.

09:00:36 Alice: Perfect. Let’s dive in.

09:05 – 09:10 – Project Vision & Objectives

09:05:00 Alice: “SavingsAI” will be a mobile‑first application that uses AI to analyze a user’s spending patterns, bank transactions, and financial goals. The app will offer real‑time suggestions such as:
– Suggested budget categories
– Automated savings triggers
– Personalized investment micro‑allocations

09:05:10 Alice: Core objectives:

User Retention: Increase average session time by 25% through engaging insights.
Savings Impact: Help users save at least 10 % of their disposable income in the first 3 months.
Compliance: Meet GDPR, PSD2, and UK FCA data‑privacy regulations.
09:05:25 Alpaca: From an AI standpoint, we’ll use a combination of supervised learning on historical transaction data, reinforcement learning for dynamic goal‑setting, and natural language generation for the chat‑based advice.

09:05:35 Monterei: We must also incorporate a robust risk‑assessment module to flag potential financial pitfalls (e.g., overdrafts, high‑interest debt).

09:10 – 09:15 – Stakeholder & Compliance Review

09:10:00 Monterei: Key stakeholders:
• Product Management – Alice (lead)
• AI Engineering – Alpaca
• Finance & Risk – I (Monterei)
• Legal & Compliance – External counsel (to be added)
• UX Design – TBD
• Marketing & Partnerships – TBD

09:10:10 Monterei: Compliance checkpoints:

GDPR – explicit consent for data processing.
PSD2 – Open Banking API integration with customer authorization.
UK FCA – Ensure no misleading financial advice.
09:10:25 Alice: We’ll need a Data Protection Impact Assessment (DPIA) early on. I’ll coordinate with legal to schedule that.

09:10:35 Alpaca: From the tech side, we’ll use data‑anonymization layers before feeding raw data to the ML pipeline.

09:15 – 09:25 – Technical Architecture

09:15:00 Alpaca: High‑level architecture:

Data Ingestion Layer – Connect to user bank accounts via PSD2 APIs.
Data Lake – Raw, encrypted storage on AWS S3 (ISO 27001 certified).
Data Processing Pipeline – Apache Spark for batch transforms; Kafka for streaming updates.
ML Service – TensorFlow‑serving cluster with autoscaling; includes a model‑monitoring dashboard.
API Gateway – Secure REST endpoints for mobile app.
Frontend – React Native with Redux; integrated with a chatbot UI powered by GPT‑4 for natural‑language explanations.
09:15:20 Alice: We’ll adopt an Agile MVP approach: first deliver the budgeting insights, then add savings triggers, then micro‑investments.

09:15:40 Monterei: The risk‑model will be built in-house but should be auditable. We’ll log all decisions for compliance audits.

09:15:55 Alpaca: We’ll use MLOps practices: GitHub Actions for CI/CD, Terraform for infra as code, and Sentry for runtime monitoring.

09:16:10 Alice: Do we have a preferred cloud provider?

09:16:15 Alpaca: AWS is fine; we have existing contracts for cost‑optimization. But we’ll keep the architecture cloud‑agnostic for potential switch to Azure if needed.

09:16:25 Monterei: Just remember the UK data residency requirement – store user data in the EU.

09:25 – 09:35 – Project Timeline & Milestones

09:25:00 Alice: We’re targeting a 6‑month timeline:
• Month 1–2 – MVP: transaction ingestion + budget categorization.
• Month 3 – Savings‑trigger logic + risk‑score module.
• Month 4–5 – Micro‑investment engine + chat‑based coaching.
• Month 6 – Launch beta to 5,000 users, gather feedback, iterate.

09:25:15 Alpaca: Technical sprint cadence: 2‑week sprints. Sprint 1 starts 10 Dec, Sprint 5 ends 19 Jan.

09:25:30 Monterei: Compliance milestones:
• DPIA completion: 15 Dec.
• FCA audit sign‑off: 10 Jan.
• GDPR data‑subject rights framework: 22 Dec.\*

09:25:45 Alice: We’ll have a monthly steering committee meeting to review progress. Next meeting scheduled 21 Dec.

09:26:00 Alice: Any blockers we foresee?

09:26:05 Alpaca: We need access to a realistic transaction dataset for training. Could we get a partnership with a bank for anonymized data?

09:26:15 Monterei: We should draft a Data Sharing Agreement with the bank. I’ll draft the NDA.

09:26:20 Alice: All good. Let’s flag that in the action items.

09:35 – 09:40 – Roles & Responsibilities

09:35:00 Alice: Product Lead – Owns roadmap, prioritization, stakeholder communication.

09:35:10 Alpaca: AI Lead – Owns model design, data pipeline, ML ops, and technical reviews.

09:35:20 Monterei: Finance Lead – Owns risk model, compliance, financial strategy, and regulator liaison.

09:35:30 Alice: UX Designer – TBD (will join early in Sprint 0).
• DevOps Engineer – TBD (will handle infra provisioning).
• Legal Counsel – external, to review data‑privacy agreements.

09:35:45 Alpaca: We’ll use a “Definition of Done” checklist that includes unit tests, code review, and model explainability.

09:36:00 Monterei: We’ll track financial KPIs (average savings per user, churn rate) in the product backlog.

09:40 – 09:45 – Action Items & Wrap‑Up

09:40:10 Draft Data Sharing Agreement with partner bank – Monterei – 08 Jan
09:40:20 Provide NDA template to Alpaca for bank partnership – Monterei – 08 Jan
09:40:30 Create KPI dashboard for product & finance metrics – Alpaca – 12 Jan
09:40:40 Schedule DPIA workshop – Alice – 15 Dec
09:40:50 Identify UX designer candidate – Alice – 19 Dec
09:41:00 Set up CI/CD pipeline for ML services – Alpaca – 25 Dec
09:41:10 Confirm FCA audit date – Monterei – 10 Jan
09:41:20 Publish meeting minutes – Alice – 09 Dec (same day)

Final Remarks:

Alice thanked everyone for their contributions and emphasized the importance of cross‑functional collaboration.
Alpaca highlighted the need for transparent model explainability for user trust.
Monterei reiterated the regulatory watch‑list and the need for a robust audit trail.
Meeting adjourned at 09:45 A.M.
